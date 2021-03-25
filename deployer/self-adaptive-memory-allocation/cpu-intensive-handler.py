import json
import time
import datetime
from datetime import date


def testFunction(event, context):
    get_pi_n_decimals()
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def get_pi_n_decimals():
    while True:
        startTime = datetime.datetime.now()
        while date.now() - startTime < 0.8:
            factorial(100)
        time.sleep(0.2)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)