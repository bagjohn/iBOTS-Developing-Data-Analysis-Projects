import argparse
from pathlib import Path
import pandas as pd

p=argparse.ArgumentParser('CSV merger')
p.add_argument('input', type=str, help='Input path to folder containing csvs')
p.add_argument('output', type=str, help='Output csv filepath')

args=p.parse_args()

# Merge the task data

csv_paths=list(Path(args.input).glob('*.csv'))

dfs=[]
for i, p in enumerate(csv_paths):
    df=pd.read_csv(p)
    dfs.append(df)

df0=pd.concat(dfs)
df0=df0.set_index('trial')
df0=df0.sort_index()

df0.to_csv(args.output)
print('csv files merged')