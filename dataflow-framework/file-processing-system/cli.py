import argparse
from main import single_file_mode, watch_mode

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='Process a single file')
    parser.add_argument('--watch', action='store_true', help='Watch mode for real-time processing')
    return parser.parse_args()

def main():
    args = parse_args()

    if args.input:
        single_file_mode(args.input)
    elif args.watch:
        watch_mode()
    else:
        print("Please provide either --input <file> or --watch")

if __name__ == "__main__":
    main()
