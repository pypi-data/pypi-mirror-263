import yaml
from os import path
from . import util
from . import aws

class Config:
    _instance = None
    file_path:str

    def __new__(cls, file_path:str):
            if cls._instance is None:
                cls._instance = super(Config, cls).__new__(cls)
                if not path.isabs(file_path):
                    file_path = path.abspath(file_path)

                util.log(f"received config is {file_path}")
                cls._instance.file_path = file_path
                cls._instance.load_config_file()
                cls._instance.validate_config()

            return cls._instance
    
    @staticmethod
    def get_current():
        if Config._instance is None:
            raise Exception(f"Config is not initialized yet")
        
        return Config._instance

    def load_config_file(self):
        if path.isfile(self.file_path):
            with open(self.file_path, "r") as file:
                self.config = yaml.safe_load(file)
        else:
            raise Exception(f"{self.file_path} file not found")
    
    def validate_config(self):
        if "lambda_function" not in self.config:
            raise Exception(f"Config file should have lambda_function node")
        
        lambda_function = self.config["lambda_function"]
        if "function_name" not in lambda_function:
            raise Exception(f"Function should have a function_name node")
        
        function_name = lambda_function["function_name"]

        if "invocation_count" not in lambda_function:
            util.log(f"{function_name} invocation count set to 10")

        if "payload" not in lambda_function:
            raise Exception(f"{function_name} function should have a payload node")

        if len(lambda_function["payload"]) == 0:
            raise Exception(f"{function_name} function should have at least 1 attribute")
        
        util.log(f"config file is validated")

    def get_locale(self):
        if "config" in self.config and "locale" in self.config["config"]:
            return self.config["config"]["locale"]
        else:
            return "en_US"

    def get_on_error(self):
        if "config" in self.config:
            if isinstance(self.config["config"], list) and "on_error" in self.config["config"]:
                return self.config["config"]["on_error"]
        else:
            return "RAISE_ERROR"

    def get_region(self):
        if "aws" in self.config and "region" in self.config["aws"]:
            return self.config["aws"]["region"]
        else:
            return None

    def get_profile(self):
        if "aws" in self.config and "profile" in self.config["aws"]:
            return self.config["aws"]["profile"]
        else:
            return "default"

    def get_function(self):
        return self.config["lambda_function"]["function_name"]

    def get_batch(self):
        if "lambda_function" in self.config and "batch" in self.config["lambda_function"]:
            return self.config["lambda_function"]["batch"]
        return 1
    
    def get_sleep(self):
        if "lambda_function" in self.config and "sleep" in self.config["lambda_function"]:
            return self.config["lambda_function"]["sleep"]
        return 0
    
    def get_invocation_count(self):
        if "lambda_function" in self.config and "invocation_count" in self.config["lambda_function"]:
            return self.config["lambda_function"]["invocation_count"]
        else:
            return 1

    def get_invocation_type(self):
        if "lambda_function" in self.config and "invocation_type" in self.config["lambda_function"]:
            return self.config["lambda_function"]["invocation_type"]
        else:
            return "Event"

    def get_payload(self):
        return self.config["lambda_function"]["payload"]

    def get_attributes(self):
        return self.config["dynamodb_table"]["attributes"]

    def get_python_import(self):
        if "config" in self.config and "python_import" in self.config["config"]:
            return self.config["config"]["python_import"]

        return []
