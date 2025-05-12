import argparse
from main import main

def process():
    input_file = 'text.txt'
    config_path = 'config.yaml'
    trace = False

    main(input_file=input_file, config_file=config_path, trace_enabled=trace)

if __name__ == "__main__":
    process()