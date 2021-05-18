import json
import boto3
import base64
import re
import numpy as np

lambda_func = boto3.client('lambda')
lambda_name = "arn:aws:lambda:eu-central-1:277644480311:function:cpu_intensive"


def lambda_handler(event, context):
    search_memory_interval(128, 10240)
    return {'statusCode': 200, 'body': json.dumps("response")}


def search_memory_interval(interval_start, interval_end):
    if (interval_end - interval_start > 0):

        middle = int((interval_end + interval_start) / 2)
        print("middle:  ", middle)

        duration_middle = get_duration(lambda_name, middle)
        duration_start = get_duration(lambda_name, interval_start)

        if (duration_start / duration_middle <= middle / interval_start):
            print("part one:  ", interval_start, middle)
            search_memory_interval(interval_start, middle)
        else:
            print("part two: ", middle, interval_end)
            search_memory_interval(middle, interval_end)
    else:
        print("memory is:   ", interval_start)


def get_duration(function_name: str, memory: int):
    set_lambda_memory_level(function_name, memory)
    print("memory:     ", memory)
    return invoke_lambda(function_name)


def invoke_lambda(function_name: str):
    durations = []
    for _ in range(5):
        response = lambda_func.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            LogType='Tail',
        )
        log = base64.b64decode(response["LogResult"])
        m = re.search('\tBilled Duration: (\d+)', log.decode("utf-8"))
        durations.append(int(m.group(1)))

    print("duration:   ", np.percentile(durations, 90))

    return np.percentile(durations, 90)  # 90 perc


def set_lambda_memory_level(function_name: str, memory: int):
    lambda_func.update_function_configuration(
        FunctionName=function_name,
        MemorySize=memory
    )