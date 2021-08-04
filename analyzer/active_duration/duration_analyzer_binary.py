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
    aws_compute_coef = 0.00001667
    if (interval_end > interval_start):

        middle = int((interval_end + interval_start) / 2)
        print("middle:  ", middle)

        duration_middle = get_duration(middle)
        value_middle = [duration_middle, middle, duration_middle * middle * aws_compute_coef / 1024000]
        values.append(value_middle)

        duration_start = get_duration(interval_start)
        value_start = [duration_start, interval_start, duration_start * interval_start * aws_compute_coef / 1024000]
        values.append(value_start)

        print("comparing  ", duration_start, duration_middle)
        if (duration_middle/duration_start > 0.99): # if the duration is almost the same, stay on the left interval
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