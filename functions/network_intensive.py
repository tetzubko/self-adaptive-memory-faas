import json
from time import time
import json
from urllib.request import urlopen


def lambda_handler(event, context):
    #event = json.loads(event['body'])
    link = "https://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=3000000&lang=en"#event['link'] # https://github.com/jdorfman/awesome-json-datasets

    start = time()
    f = urlopen(link)
    data = f.read().decode("utf-8")
    network = time() - start

    start = time()
    json_data = json.loads(data)
    str_json = json.dumps(json_data, indent=4)
    latency = time() - start
    print(str_json)
    return {'network': str(network), "latency": str(latency)}