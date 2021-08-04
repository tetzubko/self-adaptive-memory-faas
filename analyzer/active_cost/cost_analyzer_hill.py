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
    memory = hill_algorithm(1024)
    print(values)
    set_lambda_memory_level(memory)
    return {'statusCode': 200, 'body': json.dumps("response")}


def hill_algorithm(memory: int):
    aws_compute_coef = 0.00001667
    current_memory = memory
    step = 128
    attempts_counter=0
    max_attempts=5
    value = {
        "min_cost": float('inf'),
        "memory": "",
    }

    while (attempts_counter <= max_attempts):
        if(current_memory+step>10240):
            current_memory-=step
        elif (current_memory - step < 128):
            current_memory+=step

        memory_left=current_memory - step
        duration_neighbbour_left = get_duration(memory_left)
        current_duration = get_duration(current_memory)

        cost_left = duration_neighbbour_left * (memory_left)* aws_compute_coef / 1024000
        cost_current = current_duration * current_memory * aws_compute_coef / 1024000

        current_value = [current_duration, current_memory, cost_current]
        left_value = [duration_neighbbour_left, memory_left,  cost_left]
        values.append(left_value)
        values.append(current_value)

        if(cost_current <= cost_left): # cost is decreasing, increase mem
            print(current_memory, memory_left)
            print(cost_current * 1024000 / aws_compute_coef, cost_left * 1024000 / aws_compute_coef)
            current_memory += int(random.uniform(1, 2) * step)
            # print("------ cost is decreasing, increase memory:  ", current_memory, current_memory-step)
            attempts_counter = attempts_counter if attempts_counter==0 else attempts_counter+1
        else: # cost is increasing, decrease mem
            print(current_memory, memory_left)
            print(cost_current * 1024000 / aws_compute_coef, cost_left * 1024000 / aws_compute_coef)
            current_memory -= int(random.uniform(1, 2) * step)
            attempts_counter = attempts_counter if attempts_counter == 0 else attempts_counter + 1
            # print("------ cost is increasing, decrease memory:  ", current_memory, current_memory-step)
            if (cost_left < value["min_cost"]):
                print("comparing", cost_left* 1024000 / aws_compute_coef, value["min_cost"]* 1024000 / aws_compute_coef)
                value["min_cost"] = cost_left
                value["memory"] = memory_left
                attempts_counter += 1
    return value["memory"]

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
        MemorySize=int(memory)
    )
