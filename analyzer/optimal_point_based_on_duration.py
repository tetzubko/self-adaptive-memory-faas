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
    memory_prev = 128
    values = []
    step_increment = 128

    set_lambda_memory_level(memory_prev)
    duration_prev = invoke_lambda()

    value = [duration_prev, memory_prev, duration_prev * memory_prev * aws_compute_coef / 1024000]
    values.append(value)

    memory = memory_prev + step_increment
    set_lambda_memory_level(memory)
    duration = int(invoke_lambda())

    value = [duration, memory, duration * memory * aws_compute_coef / 1024000]
    values.append(value)

    for x in range(0, 15):
        if(1- (duration/duration_prev) < 0.1):  # the duration stopped decreasing actively, see the value it had before
            print("stopped on:  ", memory_prev)

        duration_prev = duration
        memory_prev = memory

        memory = memory_prev + step_increment
        set_lambda_memory_level(memory)
        duration = int(invoke_lambda())

        value = [duration, memory, duration * memory * aws_compute_coef / 1024000]
        values.append(value)

    print(values)

    return memory


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