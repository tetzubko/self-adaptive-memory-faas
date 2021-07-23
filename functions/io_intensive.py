import json
import os
import subprocess


def lambda_handler(event, context):
    # bs = 'bs=' + event['bs']
    # count = 'count=' + event['count']
    bs = 'bs=' + str(512)
    count = 'count=' + str(50)
    print(bs)
    print(count)
    out_fd = open('/tmp/io_write_logs', 'w')
    a = subprocess.Popen(['dd', 'if=/dev/zero', 'of=/tmp/out', bs, count], stderr=out_fd)
    a.communicate()

    output = subprocess.check_output(['ls', '-alh', '/tmp/'])
    print(output)

    output = subprocess.check_output(['du', '-sh', '/tmp/'])
    print(output)

    with open('/tmp/io_write_logs') as logs:
        result = str(logs.readlines()[2]).replace('\n', '')
        return {
        'statusCode': 200,
        'body': result
        }