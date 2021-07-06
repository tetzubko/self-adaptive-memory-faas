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
    memory = optimal_algorithm()
    set_lambda_memory_level(memory)

    return {'statusCode': 200, 'body': json.dumps("set memory to: ")}


def optimal_algorithm():
    aws_compute_coef = 0.00001667
    values = []
    start_memory = 128
    end_memory = 10240
    step_increment = 128
    max_attempts = 5
    attempts_counter = 0
    coeficient = 0.5

    set_lambda_memory_level(start_memory)
    max_duration = int(invoke_lambda())

    set_lambda_memory_level(end_memory)
    max_cost = invoke_lambda() * end_memory

    left_value = coeficient * max_duration / max_duration + (1 - coeficient) * max_duration * start_memory / max_cost

    value = [max_duration, start_memory, max_duration * start_memory * aws_compute_coef / 1024000, left_value]
    values.append(value)

    global_min = {
        "value": left_value,
        "memory": start_memory
    }  # first possible global minimum

    while (attempts_counter <= max_attempts):

        current_memory = start_memory + step_increment
        set_lambda_memory_level(current_memory)
        current_duration = int(invoke_lambda())
        right_value = coeficient * current_duration / max_duration + (1 - coeficient) * current_duration * current_memory / max_cost

        value = [current_duration, current_memory, current_duration * current_memory * aws_compute_coef / 1024000, right_value]
        values.append(value)

        if left_value < right_value:
            if left_value <= global_min["value"]:  # it is a new global minimum
                print("===== Setting new global_min:  ", start_memory)
                global_min["memory"] = start_memory
                global_min["value"] = left_value
                attempts_counter = 0
            else:
                print("===== this minimum is bigger than global one")
                attempts_counter += 1  # this minimum is bigger than existing one

        left_value = right_value
        start_memory = current_memory

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
