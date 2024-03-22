from distutils.log import Log
from faker import Faker
import random
import json
from os import path
import datetime, time
from . import config, util, awslambda

def invoke_lambda(config_file_path, **kwargs):
    configurator = config.Config(config_file_path)
    function_name = configurator.get_function()
    batch = configurator.get_batch()
    sleep = configurator.get_sleep()
    lambda_client = awslambda.get_lambda_client()
    on_error = configurator.get_on_error()
    invocation_count = configurator.get_invocation_count()
    invocation_type = configurator.get_invocation_type()

    iteration = 1
    items_inserted = 0
    for _ in range(invocation_count):
        util.progress_bar(iteration, invocation_count, "Invoking Lambda Function")
        try:
            payload = generate_json(config_file_path, **kwargs)
            awslambda.invoke(function_name, payload, invocation_type, lambda_client)
            items_inserted += 1
            if sleep > 0 and items_inserted % batch == 0:
                time.sleep(sleep / 1000)
        except Exception as e:
            if on_error == "RAISE_ERROR":
                raise Exception(f"Lambda Function {function_name} invocation error !!!\n{payload}\n{e}")
        
        iteration += 1
    
    util.log(f"{function_name} lambda function invoked {items_inserted} times")

def generate_json(config_file_path, **kwargs):
    configurator = config.Config(config_file_path)
    payload_config = configurator.get_payload()
    python_import = configurator.get_python_import()
    locale = configurator.get_locale()
    fake = Faker(locale)

    if "fake_provider" in kwargs:
        if not isinstance(kwargs["fake_provider"], list):
            fake.add_provider(kwargs["fake_provider"])
        else:
            for provider in kwargs["fake_provider"]:
                fake.add_provider(provider)

    def generate_data(node):
        if isinstance(node, dict):
            return {key: generate_data(value) for key, value in node.items()}
        elif isinstance(node, list):
            return [generate_data(item) for item in node]
        elif isinstance(node, str) and node == 'None':
            return None
        elif isinstance(node, str):
            return generate_fake_value(fake, node, python_import, **kwargs)
        else:
            return node

    fake_data = generate_data(payload_config)
    
    return fake_data

def generate_fake_value(fake: Faker, command, python_import, **kwargs):
    result = None
    
    variables = {
        "random": random,
        "fake": fake,
        "result": result,
        "command": command
        }
    
    if "custom_function" in kwargs:
        if isinstance(kwargs["custom_function"], list):
            for func in kwargs["custom_function"]:
                variables[func.__name__] = func
        else:
            func = kwargs["custom_function"]
            variables[func.__name__] = func
    
    if python_import and isinstance(python_import, list):
            for library_name in python_import:
                variables[library_name] = __import__(library_name)
    
    exec(f"result = {command}", variables)
    result = variables["result"]

    if isinstance(result, (datetime.date, datetime.datetime)):
        result = result.isoformat()

    return result