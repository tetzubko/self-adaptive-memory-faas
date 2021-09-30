import json
import boto3
import re

def lambda_handler(event, context):

    return {'statusCode': 200, 'body': json.dumps("analyzer")}
