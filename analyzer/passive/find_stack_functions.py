import json
import boto3
import base64
import re

lambda_client = boto3.client('lambda')
sqs = boto3.client('sqs')
db_client = boto3.client('dynamodb')


def lambda_handler(event, context):
    stackName = event["stackName"]
    lambdas = []

    response = lambda_client.list_functions()
    r = findLambdas(response, stackName)
    lambdas = lambdas + r

    while "NextMarker" in str(response):
        m = re.search("NextMarker':.'([^']*)", str(response))
        if (m):
            response = lambda_client.list_functions(Marker=str(m.group(1)))
            r = findLambdas(response, stackName)
            lambdas = lambdas + r

    response = lambda_client.list_functions()
    r = findLambdas(response, stackName)
    lambdas = lambdas + r

    # filter out lambdas, which were already analysed
    analysed_functions = getAnalysedLambdas()

    for x in lambdas:
        if (x not in analysed_functions):
            print(x)
            sqs.send_message(
                QueueUrl='https://sqs.us-east-1.amazonaws.com/277644480311/tetianaMemoryAllocation',
                MessageBody=x
            )

    return {'statusCode': 200, 'body': json.dumps("")}


def findLambdas(response, stackName):
    return re.findall("'FunctionName': '(" + stackName + "-[^']*)", str(response))


def getAnalysedLambdas():
    response = db_client.scan(
        TableName='tetianaAnalysedFunctions',
        AttributesToGet=[
            'functionID'
        ]
    )

    analysed_functions = []
    for item in response["Items"]:
        analysed_functions.append(item["functionID"]["S"])
    return analysed_functions