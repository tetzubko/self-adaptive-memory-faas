import json
import boto3
import base64
import re
import numpy as np

lambda_func = boto3.client('lambda')
lambda_name = ""
values = []


def lambda_handler(event, context):
    global lambda_name
    lambda_name = event['functionId']
    search_memory_interval(128, 10240)
    return {'statusCode': 200, 'body': json.dumps("response")}


def search_memory_interval(interval_start, interval_end):
    if (interval_end > interval_start):

        middle = int((interval_end + interval_start) / 2)
        print("middle:  ", middle)

        duration_middle = get_duration(middle)
        value_middle = [duration_middle, middle, duration_middle * middle / 1024]
        values.append(value_middle)

        duration_start = get_duration(interval_start)
        value_start = [duration_start, interval_start, duration_start * interval_start / 1024]
        values.append(value_start)

        if (duration_middle/duration_start >= 0.99): # if the duration is almost the same, stay on the left interval
            print("comparing  ", duration_start, duration_middle)
            print("left part:  ", interval_start, middle)
            return search_memory_interval(interval_start, middle)
        else:
            print("right part: ", middle, interval_end)
            return search_memory_interval(middle, interval_end)

    print("memory is:   ", interval_start)
    print(values)
    return


def get_duration(memory: int):
    set_lambda_memory_level(memory)
    return invoke_lambda()


def invoke_lambda():
    durations = []
    for _ in range(5):
        response = lambda_func.invoke(
            FunctionName=lambda_name,
            InvocationType='RequestResponse',
            LogType='Tail',
        )
        log = base64.b64decode(response["LogResult"])
        m = re.search('\tBilled Duration: (\d+)', log.decode("utf-8"))
        durations.append(int(m.group(1)))

    return np.percentile(durations, 90)  # 90 perc


def set_lambda_memory_level(memory: int):
    lambda_func.update_function_configuration(
        FunctionName=lambda_name,
        MemorySize=memory
    )


def linear_search(interval_start: int, interval_end: int):
    current_memory = interval_start

    memory_cost_min = interval_start
    cost_min = get_duration(lambda_name, interval_start) * interval_start

    while (current_memory <= interval_end):
        current_cost = get_duration(lambda_name, current_memory) * current_memory
        print("current_cost:  ", current_cost)
        print("cost_min:  ", cost_min)
        if (current_cost <= cost_min):
            memory_cost_min = current_memory
            cost_min = current_cost
        current_memory = current_memory + 128

    set_lambda_memory_level(memory_cost_min)