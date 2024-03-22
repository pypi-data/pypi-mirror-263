# Lambda Faker
lambdafaker is a versatile Python package that empowers you to effortlessly create realistic but synthetic payload data and trigger your lambda function with it. If you need to generate test data for software development, this tool simplifies the process with an intuitive schema definition in YAML format.

### Key Features
**Schema Definition:** Define your target schema using a simple YAML file. Specify the structure of your lambda payload attribute names and fake data generation code.

**Faker and Randomization:** Leverage the power of the Faker library and random data generation to create authentic-looking fake data that mimics real-world scenarios.

### Installation
```bash 
pip install lambdafaker
```

### Sample Yaml File
```
version: 1
config:
  locale: en_US                 # faker locale Default:en_US
  on_error: RAISE_ERROR         # RAISE_ERROR, SKIP Default:RAISE_ERROR
  python_import:                # Optional, list of python packages to use in data generation
    - datetime
aws:
  region: us-east-1
  credentials_profile: default  #the profile name in your local .aws/config file Default:default
lambda_function:
  function_name: my_function
  invocation_count: 10          # Optional Default:1
  invocation_type: Event        # Event / RequestResponse Default:Event
  batch: 1                      # Optional Default:1
  sleep: 1000                   # Optional Default:0 No Sleep
  payload:
    first_name: fake.first_name()
    last_name: fake.last_name()
    is_alive: fake.pybool()
    age: fake.random_int(18, 90)
    dob: fake.date_of_birth()
    address:
      street_address: fake.street_address()
      city: fake.city()
      state: fake.state_abbr()
      postal_code: fake.postcode()
    phone_numbers:
      - type: "\"home\""
        number: fake.phone_number()
      - type: "\"office\""
        number: fake.phone_number()
    children:
      - fake.first_name()
      - fake.first_name()
      - fake.first_name()
```

### Sample Code
```python
from lambdafaker import lambdafaker

lambdafaker.invoke_lambda("tests/test_function.yaml")
```

### Sample CLI Command
You can use lambdafaker in your terminal for adhoc needs or shell script to automate lambda function invocation. \
Faker custom providers and custom functions are not supported in CLI.
```bash
lambdafaker --config test_function.yaml
```


### Custom Functions and Faker Providers
With Lambda Faker, you have the flexibility to provide your own custom functions to generate column data. This advanced feature empowers developers to create custom fake data generation logic that can pull data from a database, API, file, or any other source as needed. You can also supply multiple functions in a list, allowing for even more versatility. The custom function you provide should return a single value, giving you full control over your synthetic data generation.

```python
from lambdafaker import lambdafaker
from faker import Faker
from faker_education import SchoolProvider #import custom faker provider

fake = Faker()
def get_level():
    return f"level {fake.random_int(1, 5)}"


lambdafaker.invoke_lambda("test_function.yaml", fake_provider=SchoolProvider, custom_function=get_level)
#multiple fake provider or custom function in a list is also works
```
Add get_level() function and custom faker provider to your yaml file
```
version: 1
lambda_function:
  function_name: my_function
  payload:
    first_name: fake.first_name()
    last_name: fake.last_name()
    is_alive: fake.pybool()
    age: fake.random_int(18, 90)
    dob: fake.date_of_birth()
    level: get_level()            # custom function
    school: fake.school_name()    # customer faker provider
```


### Faker Functions List
https://faker.readthedocs.io/en/master/providers.html#

### Bug Report & New Feature Request
https://github.com/necatiarslan/aws-lambda-faker/issues/new


### Todo
- Aws Profile support

### Nice To Have
- 

Follow me on linkedin to get latest news \
https://www.linkedin.com/in/necati-arslan/

Thanks, \
Necati ARSLAN \
necatia@gmail.com