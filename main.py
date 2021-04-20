from deployer import redeployer
from analyzer import analyzer
import time

def main():
    while (True):
        start_time = int(round(time.time() * 1000)) - 10 * 1000 # 5 seconds ago
        end_time = int(round(time.time() * 1000))  # current
        time.sleep(2)
        analyzer.collect_data_from_logs("self-adaptive-memory-allocation-dev-memory", start_time, end_time)


if __name__ == "__main__":
    main()