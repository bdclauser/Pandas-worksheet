import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## working with csv exercises

## Example of working in a csv and cleaning up data using multiple lines.

df = pd.read_csv('data/btc-market-price', header=None)
df.columns = ['Timestap', 'Price']
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('timestamp', inplace=True)

## Example of working with a csv and cleaning it up with one line.

df = pd.read_csv(
  'data/btc-market-price.csv',
  header=None,
  names['Timestamp', 'Price'],
  index_col=0,
  parse_dates=True
)
