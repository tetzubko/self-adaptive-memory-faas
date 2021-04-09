import os
import time
import boto3
import pandas as pd
from datetime import datetime


def redeploy_sls(memory: int):
    os.system('cd ../deployer/self-adaptive-memory-allocation && sls deploy --memory ' + str(memory))


def collect_data_from_logs(func_name: str, start: int, end: int):
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
        time.sleep(5)
        response = client.get_query_results(
            queryId=query_id
        )

    #  add loop while no results print time and attempt
    # while not response["results"]:
    #     print("Attempt at: ", datetime.now().strftime("%H:%M:%S"))
    #     time.sleep(1)

    values = []
    if response["results"]:
        for log in response["results"]:
            value = {
                "timestampInvoked": "",
                "billed_duration": "",
                "used_memory_mb": "",
                "allocated_emory_mb": "",
                "timestampAnalyzed": ""
            }
            for record in log:
                if "timestamp" in record['field']:
                    value["timestampInvoked"] = record['value']

                elif "billedDuration" in record['field']:
                    value["billed_duration"] = float(record['value'])

                elif "maxMemoryUsed" in record['field']:
                    value["used_memory_mb"] = float(record['value']) / 10 ** 6

                elif "memorySize" in record['field']:
                    value["allocated_emory_mb"] = float(record['value']) / 10 ** 6

            if value["billed_duration"]:
                value["timestampAnalyzed"] = datetime.now().strftime("%H:%M:%S")
                values.append(value)
            if value["used_memory_mb"] > value["allocated_emory_mb"] * 0.6:
                print("Memory allocated: " + value["allocated_emory_mb"] + "  Memory used: " + value["used_memory_mb"])
                redeploy_sls(value["allocated_emory_mb"] * 2)

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
    dt = datetime.now()
    seconds = int(dt.strftime('%s'))
    while (True):
        time.sleep(1)
        collect_data_from_logs("self-adaptive-memory-allocation-dev-memory", seconds - 1 * 120, seconds)


if __name__ == "__main__":
    main()
