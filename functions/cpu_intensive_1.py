import json
from datetime import datetime
import math

def lambda_handler(event, context):
    cpu_intensive(8)
    return {
        'statusCode': 200,
        'body': json.dumps('works')
    }

def cpu_intensive(number):
    start = datetime.now()

    result = 0
    for x in range(number ** 7):
        result += math.tan(x) * math.atan(x)

    end = datetime.now()
    print("Duration =", end - start)

    return result
