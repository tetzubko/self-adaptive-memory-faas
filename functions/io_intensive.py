import json
import urllib.parse
import boto3

s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

def lambda_handler(event, context):
    # Get the object from the event and show its content type
    bucket = "tetianaiobound"  # event['Records'][0]['s3']['bucket']['name']
    key = "100000_Sales_Records.csv"  # urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        nlines = 0
        for _ in response['Body'].iter_lines(): nlines += 1
        print(nlines)

        s3_resource.Object("tetianaiobound", "100000_Sales_Records_copy.csv").copy_from(
            CopySource={'Bucket': bucket, 'Key': key})

        s3.put_object(Body=b'test data', Bucket=bucket, Key='new_file.txt')
        s3.put_object(Body=b'new test data new test data new test data new test data ', Bucket=bucket, Key='new_file.txt')
        s3.delete_object(Bucket=bucket, Key='new_file.txt')
        s3.delete_object(Bucket=bucket, Key='100000_Sales_Records_copy.csv')


        return response['ContentType']
    except Exception as e:
        print(e)
        print(
            'Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(
                key, bucket))
        raise e