import argparse
import sys
from reports import get_report

def parse_args():
    parser = argparse.ArgumentParser(description="Generate employee salary reports")
    parser.add_argument("files", nargs="+", help="Paths to CSV data files")
    parser.add_argument("--report", required=True, help="Report type to generate")
    return parser.parse_args()

def main():
    args = parse_args()
    
    try:
        report = get_report(args.report)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


    report.generate(args.files)

if __name__ == "__main__":
    main()
