import json
import boto3
import base64
import re
import numpy as np

lambda_func = boto3.client('lambda')
lambda_name = "arn:aws:lambda:eu-central-1:277644480311:function:cpu_intensive"


def lambda_handler(event, context):
    memory = liner_algorithm()
    set_lambda_memory_level(lambda_name, memory)
    return {'statusCode': 200, 'body': json.dumps("response")}


def liner_algorithm():
    # max counter value, increment step
    memory_prev = 128  # can be user-defined
    counter = 0
    global_min = {
        "duration": None,
        "memory": None
    }

    set_lambda_memory_level(lambda_name, memory_prev)
    duration_prev = invoke_lambda(lambda_name)

    while (counter <= 5):

        memory = memory_prev + 128  # step can be dependent on the ratio
        set_lambda_memory_level(lambda_name, memory)
        duration = int(invoke_lambda(lambda_name))

        print("duration_prev:    ", duration_prev)
        print("memory_prev:    ", memory_prev)
        print("duration:    ", duration)
        print("memory:    ", memory)
        print(counter)

        if (duration /duration_prev  <= 0.99):  # if the new duration is smaller than the previous one
            if (counter != 0):
                if(duration / global_min["duration"] <= 0.99):  # it is a new global minimum, if the new minimum is smaller than existing one
                    print("===== Setting new global_min memory:  ", memory)
                    print("===== Setting new global_min duration:  ", duration)
                    global_min["memory"] = memory
                    global_min["duration"] = duration
                    counter = 0
            else:
                global_min["memory"] = memory
                global_min["duration"] = duration
        else:
            counter += 1

        duration_prev = duration
        memory_prev = memory

    return global_min["memory"]


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

    print(durations)

    return np.percentile(durations, 90)  # 90 perc


def set_lambda_memory_level(function_name: str, memory: int):
    lambda_func.update_function_configuration(
        FunctionName=function_name,
        MemorySize=memory
    )