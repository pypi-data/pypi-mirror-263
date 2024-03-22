import sys, os
sys.path.append(os.path.abspath("."))

from lambdafaker import lambdafaker
from faker_education import SchoolProvider
from faker import Faker


#directory_path = 'tests/exports'
#[os.remove(os.path.join(directory_path, file)) for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

lambdafaker.invoke_lambda("tests/test_function.yaml")
#lambdafaker.invoke_lambda("tests/test_function_minimal.yaml")
