import json
import boto3
import re
from datetime import datetime
import time
import pandas as pd

lambda_client = boto3.client('lambda')
logs_client = boto3.client('logs', region_name='us-east-1')
lambda_name = ""
db_client = boto3.client('dynamodb')
table_name = "tetianaAnalysedFunctions"
analyzed_memories = []

def lambda_handler(event, context):
    global lambda_name
    print("received event 2:  ", event)
    lambda_name = event['Records'][0]['body']
    # lambda_name = event['lambdaName']

    values = collect_data_from_logs()
    optimal_memory=None
    if(values):
        optimal_memory = perform_analysis_linear(values)
    if(optimal_memory):
        set_lambda_memory_level(int(optimal_memory))
        add_to_analysed_functions(str(optimal_memory))
        send_notification(str(optimal_memory))

    return {'statusCode': 200, 'body': json.dumps("sucess")}

def query_logs (query):
    log_group = '/aws/lambda/' + lambda_name
    dt = datetime.now()
    seconds = int(dt.strftime('%s'))
    try:

        start_query_response = logs_client.start_query(
            logGroupName=log_group,
            startTime=seconds - 30 * 24 * 60 * 60,
            endTime=seconds,
            queryString=query,
        )

    except logs_client.exceptions.ResourceNotFoundException:
        return None

    query_id = start_query_response['queryId']
    response = None
    while response == None or response['status'] == 'Running':
        time.sleep(5)
        response = logs_client.get_query_results(
            queryId=query_id
        )
    return response

def get_logs_with_error():
    query = "fields @requestId as requestsWithError| filter @message like /ERROR/"
    response = query_logs(query)

    if response == None:
        print("---------- log group not found for:  ", lambda_name)
        return None

    requestsWithError = []
    if response["results"]:
        for log in response["results"]:
            for record in log:
                if "requestsWithError" in record['field']:
                    requestsWithError.append(record['value'])
    return requestsWithError


def collect_data_from_logs():
    requestsWithError = get_logs_with_error()

    if requestsWithError == None:
        return None

    query = "stats avg(@duration) as avgDuration by @memorySize as memory | filter @type in ['REPORT'] | filter @requestId not in " + str(requestsWithError)
    response = query_logs(query)
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


def perform_analysis_linear(values: []):
    aws_compute_coef = 0.00001667
    print("----- values:")
    print(values)
    global analyzed_memories
    df = pd.DataFrame(values)
    df.sort_values(by=['allocated_memory_mb'], inplace=True)

    memory_prev = df.iloc[0]["allocated_memory_mb"]
    duration_prev = df.iloc[0]["billed_duration"]
    # value = [duration_prev, memory_prev, duration_prev * memory_prev * aws_compute_coef / 1024000]
    # analyzed_memories.append(value)

    memory_found=0
    step_increment = 128

    print("===== Setting first global_min: ", memory_prev)
    global_min = {
        "duration": duration_prev,
        "memory": memory_prev
    }  # first possible global minimum

    for x in range(0, 7):
        memory = memory_prev + step_increment
        if not (memory in df['allocated_memory_mb'].values):
            print("analysed function:  ", lambda_name)
            print("we need to set this lambda level: ", memory)
            set_lambda_memory_level(int(memory))
            return

        duration = df.loc[df['allocated_memory_mb'] == memory, 'billed_duration'].values[0]
        value = [duration, memory, duration * memory * aws_compute_coef / 1024000]
        analyzed_memories.append(value)

        if (duration/duration_prev > 0.9 and not memory_found):  # the duration stopped decreasing actively, see the value it had before
            print("stopped on:  ", memory_prev)
            global_min["memory"] = memory_prev
            memory_found=1

        duration_prev = duration
        memory_prev = memory

    return global_min["memory"]


def set_lambda_memory_level(memory: int):
    lambda_client.update_function_configuration(
        FunctionName=lambda_name,
        MemorySize=memory
    )

def add_to_analysed_functions(memory: str):
    values_str = str(analyzed_memories)

    db_client.put_item(
        TableName=table_name,
        Item={
            'functionID': {
                'S': lambda_name,
            },
            'allocatedMemory': {
                'S': memory,
            },
            'values': {
                'S': values_str,
            }
        })
    print("add to analysed  ", lambda_name, memory)

def send_notification(optimal_memory: str):
    sns_client = boto3.client('sns')
    sns_client.publish(
        TopicArn='arn:aws:sns:us-east-1:277644480311:tetianaAllocatedMemoryChanged',
        Message='New memory of ' + optimal_memory + ' is allocated to ' + lambda_name,
        Subject='Allocated Memory Change'
    )