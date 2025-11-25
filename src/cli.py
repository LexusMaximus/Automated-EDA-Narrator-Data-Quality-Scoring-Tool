# simple command line entry
"""
Command-line interface (CLI) for running the Automated EDA Narrator pipeline.

This script allows users to execute the DatasetPipeline on a CSV file from the terminal.
It generates a Markdown report containing:
- Narrative insights from the dataset
- Data quality scores
- Summary statistics

Usage:
    python src/cli.py <csv_path> [--out <output_file>]

Example:
    python src/cli.py data/sample.csv --out reports/sample_report.md
"""

import argparse
from orchestrator import DatasetPipeline

def main():
    """
    Parse command-line arguments and execute the DatasetPipeline.

    Steps:
    1. Parses the required 'csv' argument and optional '--out' argument.
    2. Runs the DatasetPipeline on the given CSV file.
    3. Outputs the Markdown report to a file if '--out' is specified, 
       otherwise prints the report to the terminal.

    Command-line Arguments:
        csv (str): Path to the CSV file to analyze.
        --out (str, optional): Output Markdown file path. Defaults to None.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Run Automated EDA Narrator")
    parser.add_argument("csv", help="Path to CSV file")
    parser.add_argument("--out", help="Output markdown path", default=None)
    args = parser.parse_args()

    pipeline = DatasetPipeline(args.csv)
    md = pipeline.run()

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Wrote report to {args.out}")
    else:
        print(md)

if __name__ == "__main__":
    main()
