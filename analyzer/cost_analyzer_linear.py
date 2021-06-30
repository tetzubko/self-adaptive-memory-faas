import json
import boto3
import base64
import re
import numpy as np

lambda_func = boto3.client('lambda')
lambda_name = ""

def lambda_handler(event, context):
    global lambda_name
    lambda_name = event['functionId']
    memory = linear_algorithm()
    set_lambda_memory_level(memory)

    return {'statusCode': 200, 'body': json.dumps("set memory to: ")}


def linear_algorithm():
    aws_compute_coef = 0.00001667
    values = []
    memory_prev = 128
    attempts_counter = 0
    max_attempts = 5
    step_increment = 128

    set_lambda_memory_level(memory_prev)
    duration_prev = invoke_lambda()
    value = [duration_prev, memory_prev, duration_prev * memory_prev * aws_compute_coef / 1024000]
    values.append(value)

    print("===== Setting first global_min: ", memory_prev)
    global_min = {
        "duration": duration_prev,
        "memory": memory_prev
    } # first possible global minimum

    while (attempts_counter <= max_attempts):

        memory = memory_prev + step_increment
        set_lambda_memory_level(memory)
        duration = int(invoke_lambda())

        value = [duration, memory, duration * memory * aws_compute_coef / 1024000]
        values.append(value)

        if duration * memory > duration_prev * memory_prev:
            if duration_prev * memory_prev <= global_min["memory"] * global_min["duration"]:  # it is a new global minimum
                print("===== Setting new global_min:  ", memory_prev)
                global_min["memory"] = memory_prev
                global_min["duration"] = duration_prev
                attempts_counter = 0
            else:
                print("===== this minimum is bigger than global one")
                attempts_counter += 1  # this minimum is bigger than existing one

        duration_prev = duration
        memory_prev = memory

    print(values)
    return global_min["memory"]


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

    return np.percentile(durations, 90)


def set_lambda_memory_level(memory: int):
    lambda_func.update_function_configuration(
        FunctionName=lambda_name,
        MemorySize=memory
    )
