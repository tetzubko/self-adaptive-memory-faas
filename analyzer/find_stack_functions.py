import json
import boto3
import base64
import re

client = boto3.client('lambda')
sqs = boto3.client('sqs')


def lambda_handler(event, context):
    stackName = event["stackName"]
    lambdas = []
    response = client.list_functions()

    while "NextMarker" in str(response):
        m = re.search("NextMarker':.'([^']*)", str(response))
        if (m):
            response = client.list_functions(Marker=str(m.group(1)))
            r = findLambdas(response, stackName)
            lambdas = lambdas + r

    for x in lambdas:
        print(x)
        # sqs.send_message(
        #     QueueUrl='https://sqs.us-east-1.amazonaws.com/277644480311/tetianaMemoryAllocation',
        #     MessageBody=x
        # )

    return {'statusCode': 200, 'body': json.dumps("")}


def findLambdas(response, stackName):
    return re.findall("'FunctionName': '(" + stackName + "-[^']*)", str(response))