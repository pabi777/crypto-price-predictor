from os import name
import pandas as pd
header = ['serial', 'icon', 'Name', 'Symbol',
          'Price (USD)', 'Market Cap', 'Vol (24H)', 'Total Vol', 'Chg (24H)', 'Chg (7D)']

df = pd.read_csv('data/livedata.csv', names=header)

df = df.iloc[]
print(df)
