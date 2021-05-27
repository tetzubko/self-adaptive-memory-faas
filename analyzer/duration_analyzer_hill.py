import json
import boto3
import base64
import re
import random
import numpy as np
import pandas as pd

lambda_func = boto3.client('lambda')
lambda_name = ""
values = []

def lambda_handler(event, context):
    global lambda_name
    lambda_name = event['functionId']
    memory = algorithm(1000)  # can be random number
    set_lambda_memory_level(lambda_name, memory)
    return {'statusCode': 200, 'body': json.dumps("response")}


def algorithm(memory: int):
    step = 128
    attempts_counter = 0
    current_memory = memory
    current_duration = get_duration(lambda_name, current_memory)
    global_min = {
        "duration": current_duration,
        "memory": current_memory
    }

    while (attempts_counter < 3):
        if (current_memory == 128):
            raise Exception("current_memory is 128, stop")

        duration_neighbbour_left = get_duration(lambda_name, current_memory - step)
        memory_neighbbour_left = current_memory - step
        create_value(duration_neighbbour_left, memory_neighbbour_left, duration_neighbbour_left*memory_neighbbour_left)
        print("===== duration_neighbbour_left:  ", duration_neighbbour_left)
        print("===== current_duration:  ", current_duration)

        current_duration = get_duration(lambda_name, current_memory)
        create_value(current_duration, current_memory, current_duration * current_memory)

        duration_neighbbour_right = get_duration(lambda_name, current_memory + step)
        memory_neighbbour_right = current_memory + step
        create_value(duration_neighbbour_right, current_memory + step, memory_neighbbour_right*duration_neighbbour_right)
        print("===== duration_neighbbour_right:  ", duration_neighbbour_right)

        if (duration_neighbbour_left <= 0.99 * current_duration):  # duration is increasing
            current_memory -= int(random.uniform(1, 2) * step)
            print("===== memory decreased to:  ", current_memory)
        elif (duration_neighbbour_right <= 0.99 * current_duration):  # duration is decreasing
            current_memory += int(random.uniform(1, 2) * step)
            print("===== memory increased to:  ", current_memory)
        else:
            if(current_duration / global_min["duration"] < 0.99):
                print("===== setting new global min duration:  ", current_duration)
                print("global_min[duration]   ", global_min["duration"])
                global_min["duration"] = current_duration
                global_min["memory"] = current_memory
            else:
                attempts_counter += 1
    print(values)
    print("selected memory: ", global_min["memory"])

    return global_min["memory"]

def create_value(duration: int, memory: int, cost):
    value = [duration, memory, cost / 1024]
    values.append(value)

def get_duration(function_name: str, memory: int):
    set_lambda_memory_level(function_name, memory)
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

    return np.percentile(durations, 90)  # 90 perc


def set_lambda_memory_level(function_name: str, memory: int):
    lambda_func.update_function_configuration(
        FunctionName=function_name,
        MemorySize=memory
    )