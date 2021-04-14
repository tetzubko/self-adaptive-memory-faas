import time
import boto3
import re
from deployer import redeployer

new_memory_max = 0
new_memory_min = 0
values = []

def redeploy_sls(memory: float):
    redeployer.test()
    print("Redeploying with: ", memory)
   # os.system('cd ../deployer/self-adaptive-memory-allocation && sls deploy --memory ' + str(memory))


def parsing_log(log: str):
    value = {
        "timestampInvoked": "",
        "billed_duration": "",
        "used_memory_mb": "",
        "allocated_memory_mb": ""
    }

    log_parts = re.split("\t", log)
    for item in log_parts:
        item_parts = re.split(":", item)

        if (item_parts[0] == 'Billed Duration'):
            value["billed_duration"] = int(re.findall(r'\d+', item_parts[1])[0])
        elif (item_parts[0] == 'Memory Size'):
            value["allocated_memory_mb"] = int(re.findall(r'\d+', item_parts[1])[0])
        elif (item_parts[0] == 'Max Memory Used'):
            value["used_memory_mb"] = int(re.findall(r'\d+', item_parts[1])[0])

    return value


def collect_data_from_logs(func_name: str, start: int, end: int):
    global new_memory_max
    global new_memory_min
    global values

    client = boto3.client('logs', region_name='eu-central-1')
    log_group = '/aws/lambda/' + func_name

    response = client.filter_log_events(
        logGroupName=log_group,
        startTime=start,
        endTime=end,
        filterPattern = "REPORT"
    )

    if response["events"]:
        for log in response["events"]:

            value = parsing_log(log['message'])
            value["timestampInvoked"] = log['timestamp']
            if value not in values:
                print(value)
                values.append(value)

            if value["allocated_memory_mb"] == 0.5*new_memory_max or value["allocated_memory_mb"] == 2*new_memory_min:
                print("skip")
                continue # when it is old logs, when memory is still not increased

            elif value["used_memory_mb"] >= value["allocated_memory_mb"] * 0.6:
                new_memory_max = value["allocated_memory_mb"] * 2
                redeploy_sls(value["allocated_memory_mb"] * 2)

            elif value["used_memory_mb"] <= value["allocated_memory_mb"] * 0.3:
                new_memory_min = value["allocated_memory_mb"] * 0.5
                redeploy_sls(value["allocated_memory_mb"] * 0.5)

def main():
    while (True):
        redeployer.test()
        start_time = int(round(time.time() * 1000)) - 10 * 1000 # 5 seconds ago
        end_time = int(round(time.time() * 1000))  # current
        time.sleep(2)
        collect_data_from_logs("self-adaptive-memory-allocation-dev-memory", start_time, end_time)


if __name__ == "__main__":
    main()
