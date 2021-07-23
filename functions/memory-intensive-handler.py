import json

def lambda_handler(event, context):
    memoryConsumingFunction()
    body = {
        "message": "Function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def memoryConsumingFunction():
    d = {}
    for i in range(0, 1000000):
        d[i] = 1  #'A' * 1024