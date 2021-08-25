import json
import boto3
import os
from datetime import datetime
import time
import pandas as pd
import re

lambda_client = boto3.client('lambda')
logs_client = boto3.client('logs', region_name='us-east-1')
db_client = boto3.client('dynamodb')
table_name = os.environ['DB_NAME']
lambda_name = ""
stack_name = ""
analyzed_memories = []
initial_memory = 128
optimal_memory = None


def lambda_handler(event, context):
    global lambda_name, stack_name, optimal_memory
    # lambda_name = event['Records'][0]['body']
    lambda_name = event['lambdaName']
    stack_name = event['stack_name']

    logs = collect_available_logs()
    if logs:
        optimal_memory = perform_cost_minimization(logs)  # if logs are available
    if optimal_memory:
        set_memory(int(optimal_memory))
        add_to_analysed_functions(str(optimal_memory))
        send_notification(optimal_memory)

    return {'statusCode': 200, 'body': json.dumps(lambda_name + " was assigned")}


def query_logs(query):
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
        print("------- log group not found for function:  ", lambda_name)
        return None

    requestsWithError = []
    if response["results"]:
        for log in response["results"]:
            for record in log:
                if "requestsWithError" in record['field']:
                    requestsWithError.append(record['value'])
    return requestsWithError


def collect_available_logs():
    requestsWithError = get_logs_with_error()

    if requestsWithError == None:  # if no log group were found
        return None

    query = "stats avg(@duration) as avgDuration by @memorySize as memory | filter @type in ['REPORT'] | filter @requestId not in " + str(
        requestsWithError)
    response = query_logs(query)
    log_values = []

    if response["results"]:
        for log in response["results"]:
            value = {
                "duration": "",
                "allocated_memory": "",
            }
            for record in log:
                if "avgDuration" in record['field']:
                    value["duration"] = float(record['value'])

                elif "memory" in record['field']:
                    value["allocated_memory"] = float(record['value']) / 10 ** 6
            log_values.append(value)

    return log_values


def perform_cost_minimization(values: []):
    aws_compute_coef = 0.00001667
    global analyzed_memories, initial_memory
    df = pd.DataFrame(values)
    df.sort_values(by=['allocated_memory'], inplace=True)

    memory_prev = df.iloc[0]["allocated_memory"]
    initial_memory = memory_prev
    duration_prev = df.iloc[0]["duration"]
    value = [duration_prev, memory_prev, duration_prev * memory_prev * aws_compute_coef / 1024000]
    analyzed_memories.append(value)

    attempts_counter = 0
    max_attempts = 3
    step_increment = 128

    print("------- setting first global_min: ", memory_prev)
    global_min = {
        "duration": duration_prev,
        "memory": memory_prev
    }  # first possible global minimum

    while (attempts_counter <= max_attempts):
        memory = memory_prev + step_increment
        if not (memory in df['allocated_memory'].values):
            print("need to set this memory level: " + str(memory) + " to " + lambda_name)
            set_memory(int(memory))
            return

        duration = df.loc[df['allocated_memory'] == memory, 'duration'].values[0]
        if duration * memory > duration_prev * memory_prev:
            if duration_prev * memory_prev <= global_min["memory"] * global_min["duration"]:
                print("------- Setting new global_min:  ", memory_prev)
                global_min["memory"] = memory_prev
                global_min["duration"] = duration_prev
            else:
                print("------- this minimum is bigger than global one: ", memory)
                attempts_counter += 1

        duration_prev = duration
        memory_prev = memory

        value = [duration_prev, memory_prev, duration_prev * memory_prev * aws_compute_coef / 1024000]
        analyzed_memories.append(value)

    print("------- analyzed_memories:", analyzed_memories)
    print(global_min["memory"])

    return global_min["memory"]


def set_memory(memory: int):
    lambda_client.update_function_configuration(
        FunctionName=lambda_name,
        MemorySize=memory
    )

def add_to_analysed_functions(memory: str):
    values_str = str(analyzed_memories)

    db_client.put_item(
        TableName=table_name,
        Item={
            'stackName': {
                'S': stack_name,
            },
            'functionID': {
                'S': lambda_name,
            },
            'initialMemory': {
                'S': str(initial_memory),
            },
            'allocatedMemory': {
                'S': memory,
            },
            'values': {
                'S': values_str,
            }
        })
    print("------- add to analysed  ", lambda_name, memory)


def send_notification(optimal_memory):
    if(initial_memory > optimal_memory):
        sns_client = boto3.client('sns')
        sns_client.publish(
            TopicArn=os.environ['SNS_ARN'],
            Message='New memory of ' + str(optimal_memory) + ' is allocated to ' + lambda_name,
            Subject='Allocated Memory Change'
        )