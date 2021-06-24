import json
import boto3
import re
from datetime import datetime
import time
import pandas as pd

lambda_func = boto3.client('lambda')
lambda_name=""

def lambda_handler(event, context):
    client = boto3.client('lambda')
    response = client.list_functions()

    while "UPP-Develop-deployRequest" not in str(response):
        m = re.search("NextMarker':.'([^']*)", str(response))
        if (m):
            response = client.list_functions(Marker=str(m.group(1)))

    set_lambda_name(str(response))
    values = collect_data_from_logs()
    optimal_memory = perform_analysis_linear(values)
    set_lambda_memory_level(int(optimal_memory))

    return {'statusCode': 200, 'body': json.dumps("response")}

def set_lambda_name(lambda_list: str):
    global lambda_name
    id = re.search("UPP-Develop-deployRequest.([^']*)", lambda_list).group(1)
    lambda_name = "UPP-Develop-deployRequest-"+id

# when sure refactor logs functions
def get_logs_with_error():
    client = boto3.client('logs', region_name='us-east-1')
    query = "fields @requestId as requestsWithError| filter @message like /ERROR/"
    log_group = '/aws/lambda/' + lambda_name

    dt = datetime.now()
    seconds = int(dt.strftime('%s'))

    start_query_response = client.start_query(
        logGroupName=log_group,
        startTime=seconds - 30 * 24 * 60 * 60,
        endTime=seconds,
        queryString=query,
    )

    query_id = start_query_response['queryId']

    response = None

    while response == None or response['status'] == 'Running':
        print('Waiting for query to complete ...')
        time.sleep(5)
        response = client.get_query_results(
            queryId=query_id
        )

    requestsWithError = []
    if response["results"]:
        for log in response["results"]:
            for record in log:
                if "requestsWithError" in record['field']:
                    requestsWithError.append(record['value'])
    return requestsWithError



def collect_data_from_logs():
    requestsWithError = get_logs_with_error()

    client = boto3.client('logs', region_name='us-east-1')
    query = "stats avg(@duration) as avgDuration by @memorySize as memory | filter @type in ['REPORT'] | filter @requestId not in "+str(requestsWithError)
    print("query:  " + query)
    log_group = '/aws/lambda/' + lambda_name

    dt = datetime.now()
    seconds = int(dt.strftime('%s'))

    start_query_response = client.start_query(
        logGroupName=log_group,
        startTime=seconds - 30 * 24 * 60 * 60,
        endTime=seconds,
        queryString=query,
    )

    query_id = start_query_response['queryId']

    response = None

    while response == None or response['status'] == 'Running':
        print('Waiting for query to complete ...')
        time.sleep(5)
        response = client.get_query_results(
            queryId=query_id
        )

    values = []
    if response["results"]:
        for log in response["results"]:
            value = {
                "billed_duration": "",
                "allocated_memory_mb": "",
            }
            for record in log:
                if "avgDuration" in record['field']:
                    value["billed_duration"] = float(record['value'])

                elif "memory" in record['field']:
                    value["allocated_memory_mb"] = float(record['value']) / 10 ** 6
            values.append(value)

    return values


def perform_analysis_linear(values:[]):
    analyzed_memories = []
    df = pd.DataFrame(values)
    df.sort_values(by=['allocated_memory_mb'], inplace=True)

    memory_prev = df.iloc[0]["allocated_memory_mb"]
    duration_prev = df.iloc[0]["billed_duration"]
    value = [duration_prev, memory_prev, duration_prev * memory_prev / 1024]
    analyzed_memories.append(value)

    attempts_counter = 0
    max_attempts = 5
    step_increment = 128

    print("===== Setting first global_min: ", memory_prev)
    global_min = {
        "duration": duration_prev,
        "memory": memory_prev
    }  # first possible global minimum

    while (attempts_counter <= max_attempts):
        memory = memory_prev + step_increment
        if not (memory in df['allocated_memory_mb'].values):
            print("we need to set this lambda level: ", memory)
            set_lambda_memory_level(int(memory))
            return

        duration = df.loc[df['allocated_memory_mb'] == memory, 'billed_duration'].values[0]
        if duration * memory > duration_prev * memory_prev:
            if duration_prev * memory_prev <= global_min["memory"] * global_min["duration"]:  # it is a new global minimum
                print("===== Setting new global_min:  ", memory_prev)
                global_min["memory"] = memory_prev
                global_min["duration"] = duration_prev
            else:
                print("===== this minimum is bigger than global one: ", memory)
                attempts_counter += 1  # this minimum is bigger than existing one

        duration_prev = duration
        memory_prev = memory

        value = [duration, memory, duration * memory / 1024]
        analyzed_memories.append(value)

    print(analyzed_memories)

    return global_min["memory"]

def set_lambda_memory_level(memory: int):
    lambda_func.update_function_configuration(
        FunctionName=lambda_name,
        MemorySize=memory
    )