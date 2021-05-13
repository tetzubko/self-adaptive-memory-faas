import json
import time

def lambda_handler(event, context):
    cpu_intensive()
    return {
        'statusCode': 200,
        'body': json.dumps('works')
    }

def cpu_intensive():
    numbers = [5_000_00 + x for x in range(20)]
    start_time = time.time()
    for number in numbers:
        sum(i * i for i in range(number))

    duration = time.time() - start_time
    print(f"Duration {duration} seconds")