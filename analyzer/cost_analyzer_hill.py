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
    memory = hill_algorithm(600)
    set_lambda_memory_level(memory)
    return {'statusCode': 200, 'body': json.dumps("response")}


def hill_algorithm(memory: int):
    current_memory = memory
    step = 128
    attempts_counter=0
    max_attempts=5
    value = {
        "min_cost": float('inf'),
        "memory": "",
    }

    while (attempts_counter <= max_attempts):
        if (current_memory - step < 128):
            return current_memory

        duration_neighbbour_left = get_duration(current_memory - step)
        current_duration = get_duration(current_memory)

        cost_left = duration_neighbbour_left * (current_memory - step)/1024
        cost_current = current_duration * current_memory/1024

        current_value = [current_duration, current_memory, cost_current]
        left_value = [duration_neighbbour_left, current_memory - step,  cost_left]
        values.append(left_value)
        values.append(current_value)

        if(cost_current <= cost_left): # cost is decreasing, increase mem
            current_memory += int(random.uniform(1, 2) * step)
            print("------ cost is decreasing, increase memory:  ", current_memory)
            attempts_counter = attempts_counter if attempts_counter==0 else attempts_counter+1
        else: # cost is increasing, decrease mem
            current_memory -= int(random.uniform(1, 2) * step)
            print("------ cost is increasing, decrease memory:  ", current_memory)
            attempts_counter = attempts_counter if attempts_counter==0 else attempts_counter+1
            if (cost_left < value["min_cost"]):
                print("comparing", cost_left, value["min_cost"])
                value["min_cost"] = cost_left
                value["memory"] = duration_neighbbour_left
                attempts_counter = 0
    print(values)
    return value["min_cost"]

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
