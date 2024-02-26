import argparse

p=argparse.ArgumentParser(description='Trial value extractor')

p.add_argument('input', type=str, help='Input filepath')
p.add_argument('output', type=str, help='Output filepath')

args=p.parse_args()


import sys
import pandas as pd


# Command-line inputs
# input_csv_path = sys.argv[1]
# output_csv_path = sys.argv[2]

# Load the csv file and extract active trials
df = pd.read_csv(args.input)
df_valid = df[df.valid].copy()

# Save the new dataframe as a csv file
df_valid.to_csv(args.output, index=False)