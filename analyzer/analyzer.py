import os
import time
import boto3
import pandas as pd
from datetime import datetime

new_memory = 0

def redeploy_sls(memory: int):
    print("redeploying with: ", memory)
    os.system('cd ../deployer/self-adaptive-memory-allocation && sls deploy --memory ' + str(memory))


def collect_data_from_logs(func_name: str, start: int, end: int):
    global new_memory
    client = boto3.client('logs', region_name='eu-central-1')

    # query = "fields @timestamp, @billedDuration, @duration, @maxMemoryUsed, @memorySize"
    query = "fields @timestamp, @billedDuration, @maxMemoryUsed, @memorySize, @message | filter @type in ['REPORT']"

    log_group = '/aws/lambda/' + func_name

    start_query_response = client.start_query(
        logGroupName=log_group,
        startTime=start,
        endTime=end,
        queryString=query,
    )

    query_id = start_query_response['queryId']

    response = None

    while response == None or response['status'] == 'Running':
        print('Waiting for query to complete ...')
        time.sleep(1)
        response = client.get_query_results(
            queryId=query_id
        )

    values = []
    if response["results"]:
        for log in response["results"]:
            value = {
                "timestampInvoked": "",
                "timestampAnalyzed": "",
                "billed_duration": "",
                "used_memory_mb": "",
                "allocated_memory_mb": ""
            }
            for record in log:
                if "timestamp" in record['field']:
                    value["timestampInvoked"] = record['value']

                elif "billedDuration" in record['field']:
                    value["billed_duration"] = float(record['value'])

                elif "maxMemoryUsed" in record['field']:
                    value["used_memory_mb"] = float(record['value']) / 10 ** 6

                elif "memorySize" in record['field']:
                    value["allocated_memory_mb"] = float(record['value']) / 10 ** 6

            value["timestampAnalyzed"] = datetime.now().strftime("%H:%M:%S")
            values.append(value)

            if value["allocated_memory_mb"] <= new_memory:
                print("---- this think should do continue from the loop: ", new_memory)
                continue # when it is old logs, which still did not see memory increase

            elif value["used_memory_mb"] > value["allocated_memory_mb"] * 0.6:
                print("Memory allocated: ", value["allocated_memory_mb"])
                print("Memory used: ", value["used_memory_mb"])
                new_memory = value["allocated_memory_mb"] * 2
                print("new_memory is: ", new_memory)
                redeploy_sls(value["allocated_memory_mb"] * 2)

        df = pd.DataFrame(values)
        df.set_index("timestampInvoked", inplace=True)
        df.index = pd.to_datetime(df.index, unit='ns')
        # df = df.resample(str(180) + 's').mean()
        #
        # df.reset_index(inplace=True)
        # df = df.dropna(how='any')
        # df.reset_index(inplace=True, drop=True)
        # df["action"] = func_name
        print(df)
        return df
    else:
        return pd.DataFrame(values)


def main():
    while (True):
        print("--- in main")
        dt = datetime.now()
        seconds = int(dt.strftime('%s'))
        time.sleep(1)
        collect_data_from_logs("self-adaptive-memory-allocation-dev-memory", seconds - 1 * 60, seconds)


if __name__ == "__main__":
    main()
