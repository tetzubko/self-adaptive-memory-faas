# self-adaptive-memory-faas

## Deployer

Module responsible for deploying functions to AWS Lambda infrastructure. 
It is based on [Serverless](https://www.serverless.com/framework/docs/providers/aws/guide/quick-start/) framework and utilizes 
AWS Lambda serverless infrastructure. 

In order to deploy new version of function run:
`serverless deploy`

In order to invoke a function run:
`serverless invoke -f memory -l`, where `memory` is the name of the function

In order to call an endpoint execute:
`curl --request GET --url https://vru6pouq2i.execute-api.eu-central-1.amazonaws.com/dev/memory`, where `memory` is the request name for the function

## Load Generator

Module responsible for sending (concurrent) requests to the Lambda function. 
It is based on [K6](https://k6.io/docs/) tool. In order to run load generator use command similar to:
`k6 run --vus 10 --duration 20s script.js`.