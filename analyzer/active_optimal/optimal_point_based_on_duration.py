import json
import boto3
import base64
import re
import numpy as np

lambda_func = boto3.client('lambda')
lambda_name = ""
value = ""

def lambda_handler(event, context):
    event = json.loads(event['body'])
    global lambda_name
    global value
    lambda_name = event['functionId']
    value = event['value']
    memory = optimal_algorithm()
    set_lambda_memory_level(memory)

    return {'statusCode': 200, 'body': json.dumps("set memory to: " + str(memory))}


def optimal_algorithm():
    aws_compute_coef = 0.00001667
    memory_prev = 128
    values = []
    step_increment = 128
    duration_relation = 0.9

    set_lambda_memory_level(memory_prev)
    duration_prev = invoke_lambda()

    value = [duration_prev, memory_prev, duration_prev * memory_prev * aws_compute_coef / 1024000]
    values.append(value)

    memory = memory_prev + step_increment
    set_lambda_memory_level(memory)
    duration = int(invoke_lambda())

    value = [duration, memory, duration * memory * aws_compute_coef / 1024000]
    values.append(value)

    while(not (duration/duration_prev > duration_relation)):  # the duration stopped decreasing actively, see the value it had before
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
    payload= '{"value": "'+ str(value) + '"}'

    for _ in range(5):
        response = lambda_func.invoke(
            FunctionName=lambda_name,
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=str.encode(payload)
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