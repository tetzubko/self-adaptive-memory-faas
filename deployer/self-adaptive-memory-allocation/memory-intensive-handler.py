import json

def testFunction(event, context):
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
    i = 0;
    for i in range(0, 10000000):
        d[i] = 'A' * 1024
        if i % 10000 == 0:
            print(i)