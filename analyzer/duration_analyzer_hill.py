import json
import boto3
import base64
import re
import random
import numpy as np

lambda_func = boto3.client('lambda')
lambda_name = ""
values = []

def lambda_handler(event, context):
    global lambda_name
    lambda_name = event['functionId']
    memory = algorithm(1024)  # can be random number
    set_lambda_memory_level(lambda_name, memory)
    return {'statusCode': 200, 'body': json.dumps("response")}


def algorithm(memory: int):
    step = 128
    attempts_counter = 0
    max_attempts = 5
    current_memory = memory
    current_duration = get_duration(lambda_name, current_memory)
    global_min = {
        "duration": current_duration,
        "memory": current_memory
    }

    while (attempts_counter <= max_attempts):
        if (current_memory + step > 10240):
            current_memory -= step
        elif (current_memory - step < 128):
            current_memory += step

        duration_neighbbour_left = get_duration(lambda_name, current_memory - step)
        memory_neighbbour_left = current_memory - step
        create_value(duration_neighbbour_left, memory_neighbbour_left, duration_neighbbour_left*memory_neighbbour_left)

        current_duration = get_duration(lambda_name, current_memory)
        create_value(current_duration, current_memory, current_duration * current_memory)

        if (current_duration/duration_neighbbour_left <= 0.99):  # duration is decreasing, increase memory
            current_memory += int(random.uniform(1, 2) * step)
            print("===== duration is decreasing, memory increased to:  ", current_memory, duration_neighbbour_left, current_duration)
        else: # duration is increasing or stays almost the same
            print("------ duration is increasing, decrease memory to:  ", current_memory, duration_neighbbour_left, current_duration)
            attempts_counter = attempts_counter if attempts_counter==0 else attempts_counter+1
            if(current_duration / global_min["duration"] < 0.99):
                print("===== setting new global min duration:  ", current_duration, global_min["duration"])
                print(current_memory)
                global_min["duration"] = current_duration
                global_min["memory"] = current_memory
                attempts_counter += 1
            current_memory -= int(random.uniform(1, 2) * step)
    print(values)
    print("selected memory: ", global_min["memory"])

    return global_min["memory"]

def create_value(duration: int, memory: int, cost):
    aws_compute_coef = 0.00001667
    value = [duration, memory, cost * aws_compute_coef / 1024000]
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