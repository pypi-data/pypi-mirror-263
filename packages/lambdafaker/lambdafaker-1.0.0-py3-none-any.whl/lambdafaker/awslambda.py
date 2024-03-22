import boto3
from . import util
from . import config
import json

def get_lambda_client():
    region = config.Config.get_current().get_region()

    if region != None:
        dynamodb = boto3.client("lambda", region_name=region)
    else:
        dynamodb = boto3.client("lambda", region_name=region)

    return dynamodb

def invoke(function_name, payload, invocation_type, lambda_client=None):
    if lambda_client is None:
        lambda_client = get_lambda_client()
    
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType=invocation_type,
        Payload=json.dumps(payload)
    )   

    if invocation_type == "RequestResponse":
        return response