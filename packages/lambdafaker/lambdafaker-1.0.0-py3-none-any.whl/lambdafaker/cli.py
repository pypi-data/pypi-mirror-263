import argparse
from . import lambdafaker

def main():
    parser = argparse.ArgumentParser(description=get_description())
    parser.add_argument('--config', required=True, help='Config yaml file path')

    args = parser.parse_args()

    if args.config is not None:
        config_file_path = args.config
    else:
        print("Missing --config parameter. Use --help for more detail.")
        return

    lambdafaker.invoke_lambda(config_file_path)

def get_description():
    return "more detail: https://github.com/necatiarslan/aws-lambda-faker/blob/main/README.md"

if __name__ == '__main__':
    main()



