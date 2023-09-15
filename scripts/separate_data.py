import pandas as pd 
from tqdm import tqdm

df = pd.read_csv("../data/main_csv/all_stocks.csv")
groups = df.groupby('stockid')
dfs_dict= {name: group for name, group in groups}
    
count = 0 
for df in dfs_dict.values(): 
    df.to_csv(f"../data/separated_stocks/stock_{count}",index=False)
    count += 1