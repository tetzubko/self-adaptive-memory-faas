import json
import boto3
import base64
import re
import random
import numpy as np

lambda_func = boto3.client('lambda')
lambda_name = "arn:aws:lambda:eu-central-1:277644480311:function:cpu_intensive_3"


def lambda_handler(event, context):
    algorithm(2656)
    return {'statusCode': 200, 'body': json.dumps("response")}


def algorithm(memory: int):
    current_memory = memory
    step = 128

    while (1):
        if (current_memory == 128):
            raise Exception("current_memory is 128")

        current_duration = get_duration(lambda_name, current_memory)
        duration_neighbbour_left = get_duration(lambda_name, current_memory - step)
        duration_neighbbour_right = get_duration(lambda_name, current_memory + step)

        compare_1 = duration_neighbbour_left - current_duration - (current_memory - (current_memory - step))
        compare_2 = current_duration - duration_neighbbour_right - (current_memory + step - current_memory)

        print("compare_1", compare_1)
        print("compare_2", compare_2)

        if (compare_1 > 0 and compare_2 > 0):
            current_memory += int(random.uniform(1, 2)*step)
            print("------ both comapre are bigger 0 current_mem incresed to:  ", current_memory)
        elif (compare_1 < 0 and compare_2 > 0):
            print("------ error state compare_1<0 and compare_2>0 mem stays:  ", current_memory)
        elif (compare_1 < 0 and compare_2 < 0):
            current_memory -= int(random.uniform(1, 2)*step)
            print("------ current_mem decreased to:  ", current_memory)
        elif (compare_1 > 0 and compare_2 < 0):
            if(compare_1-compare_2 > 150):
                current_memory -= int(random.uniform(1, 2)*step) # random is so it does not stay in the endless loop
            else:
                print("current interval is good to stop:  ", current_memory)
                break
        elif(compare_1==0 or compare_2==0):
            print("point equals 0:  ", current_memory)
            break
        else:
            print("--------- smth else ")


def get_duration(function_name: str, memory: int):
    set_lambda_memory_level(function_name, memory)
    return invoke_lambda(function_name)


def invoke_lambda(function_name: str):
    durations = []
    for _ in range(10):
        response = lambda_func.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            LogType='Tail',
        )
        log = base64.b64decode(response["LogResult"])
        m = re.search('\tBilled Duration: (\d+)', log.decode("utf-8"))
        durations.append(int(m.group(1)))

    print("durations", durations)
    durations.sort()
    durations.pop()
    durations.pop(0)
    print(sum(durations) / len(durations))

    return int(sum(durations) / len(durations))  # 90 perc


def set_lambda_memory_level(function_name: str, memory: int):
    lambda_func.update_function_configuration(
        FunctionName=function_name,
        MemorySize=memory
    )
