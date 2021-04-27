# self-adaptive-memory-faas

## Deployer

## Load Generator

Module responsible for sending (concurrent) requests to the Lambda function. 
It is based on [K6](https://k6.io/docs/) tool. In order to run load generator use command similar to:
`k6 run --vus 10 --duration 20s script.js`

Output to influxdb
`k6 run --vus 1 --duration 5m script.js --out influxdb=http://localhost:8086/myk6db`