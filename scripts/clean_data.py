import numpy as np
import pandas as pd
from tqdm import tqdm

# We need to remove the stockid and the volume column
# We also need to add the time 00:00:00 with the date and rename that columns to time
import os

_, _, files = next(os.walk("../data/separated_stocks/"))
file_count = len(files)
print(f"The total number of CSV files is {file_count}")

count = 0
pbar = tqdm(total=1081)
while count < 1081:
    df = pd.read_csv(f"../data/separated_stocks/stock_{count}")
    cols = ["stockid", "volume"]
    df.drop(columns=cols, inplace=True)
    df.rename(columns={"date": "time"}, inplace=True)
    df["time"] = df["time"].astype(str) + " 00:00:00"
    df.to_csv(f"../data/cleaned_stocks/stock_{count}")
    pbar.update(1)
    count += 1
