import numpy as np 
import pandas as pd
from tqdm import tqdm


# We need to remove the rows where the value of all of the candlestick patterns in false
# Essentially, if all the values are false, means none of the patterns had matched
import os

_, _, files = next(os.walk("../data/with_patterns/"))
file_count = len(files)
print(f"The total number of CSV files is {file_count}")
os.mkdir('../data/no_nan/')

count = 0
pbar = tqdm(total=1081)
while count < 1081:
    pbar.update(1)
    df = pd.read_csv(f"../data/with_patterns/stock_{count}.csv")
    cols = df.columns
    cols = cols[5:]
    df[cols] = df[cols].apply(lambda x: pd.factorize(x)[0])
    # using boolean indexing
    temp = df.copy()
    temp = temp.iloc[:,5:]
    mask = temp[cols] == 0
    df_new = df.copy()
    df_new.iloc[:,5:] = temp[~mask]
    remove_nan = df_new.copy().iloc[:,5:]
    remove_nan = remove_nan.dropna(how='all')
    remove_nan = remove_nan.fillna(0)
    df_new.iloc[:,5:] = remove_nan
    df_new = df_new.dropna(subset=cols)
    df_new.reset_index()
    df_new['time']= df_new['time'].str.replace(' 00:00:00','')
    df_new = df_new.sort_values(by="time")
    df_new.to_csv(f'../data/no_nan/stock_{count}.csv',index=False)
    count += 1