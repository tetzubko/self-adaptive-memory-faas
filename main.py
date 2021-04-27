from analyzer import analyzer
import time
import boto3

def main():
    client = boto3.client('lambda')

    response = client.invoke(
        FunctionName="arn:aws:lambda:eu-central-1:385973373219:function:cpu_intensive",
        InvocationType='RequestResponse',
        LogType='Tail',
    )

    # while (True):
    #     start_time = int(round(time.time() * 1000)) - 10 * 1000 # 5 seconds ago
    #     end_time = int(round(time.time() * 1000))  # current
    #     time.sleep(2)
    #     analyzer.collect_data_from_logs("self-adaptive-memory-allocation-dev-memory", start_time, end_time, 'eu-central-1')


if __name__ == "__main__":
    main()