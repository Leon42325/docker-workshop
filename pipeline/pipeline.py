import sys
import pandas as pd

print('arguments:', sys.argv)
month = sys.argv[1] if len(sys.argv) > 1 else 'unknown'

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f'output_{month}.parquet')

print(f'Hello pipeline! Month: {month}')