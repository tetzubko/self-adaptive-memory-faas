import json
import boto3
import base64
import re
import numpy as np

lambda_func = boto3.client('lambda')
lambda_name = "arn:aws:lambda:eu-central-1:277644480311:function:UPP-feature-memConfigFunction-configureMemory-jb8lL1nBuFie"
value = ""

def lambda_handler(event, context):

    return {'statusCode': 200, 'body': json.dumps("set memory to: ")}


def invoke_lambda():
    value1 = """{
        "functionId": "arn:aws:lambda:eu-central-1:277644480311:function:cpu_intensive",
        "value": "3"
    }"""
    value2 = """{
        "functionId": "arn:aws:lambda:eu-central-1:277644480311:function:cpu_intensive",
        "value": "6"
    }"""
    value3 = """{
        "functionId": "arn:aws:lambda:eu-central-1:277644480311:function:cpu_intensive",
        "value": "9"
    }"""
    values = [value1, value2, value3]

    for i in range (len(values)):
        response = lambda_func.invoke(
            FunctionName=lambda_name,
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=str.encode(values[i])
        )
        print(response)