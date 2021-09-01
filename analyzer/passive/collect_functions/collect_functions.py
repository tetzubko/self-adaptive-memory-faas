import json
import boto3
import re
import os

lambda_client = boto3.client('lambda')
sqs = boto3.client('sqs')
db_client = boto3.client('dynamodb')
stack_name = ""


def lambda_handler(event, context):
    global stack_name
    stack_name = event["stack_name"]
    lambdas = []

    response = lambda_client.list_functions()
    r = find_lambdas(response, stack_name)
    lambdas = lambdas + r

    while "NextMarker" in str(response):
        m = re.search("NextMarker':.'([^']*)", str(response))
        if (m):
            response = lambda_client.list_functions(Marker=str(m.group(1)))
            r = find_lambdas(response, stack_name)
            lambdas = lambdas + r

    response = lambda_client.list_functions()
    r = find_lambdas(response, stack_name)
    lambdas = lambdas + r

    # filter out lambdas, which were already analysed
    analysed_functions = get_analysed_lambdas()

    for x in lambdas:
        if (x not in analysed_functions):
            body = {
                "stack_name": stack_name,
                "lambda_name": x
            }
            sqs.send_message(
                QueueUrl=os.environ['SQS_URL'],
                MessageBody=json.dumps(body)
            )

    return {'statusCode': 200, 'body': json.dumps("")}


def find_lambdas(response, stack_name):
    return re.findall("'FunctionName': '(" + stack_name + "-[^']*)", str(response))


def get_analysed_lambdas():
    response = db_client.scan(
        TableName=os.environ['DB_NAME'],
        AttributesToGet=[
            'functionID'
        ]
    )

    analysed_functions = []
    for item in response["Items"]:
        analysed_functions.append(item["functionID"]["S"])
    return analysed_functions