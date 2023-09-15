import Pattern 
from tqdm import tqdm
import pandas as pd

def add_patterns(df) -> None:
    Pattern.doji(df)
    Pattern.DarkCloudCover(df)
    Pattern.Marubozu(df)
    Pattern.dragonfly_doji(df)
    Pattern.Engulf(df)
    Pattern.gravestone_doji(df)
    Pattern.Hammer_Hanging_Man(df)
    Pattern.Harami(df)
    Pattern.longleg_doji(df)
    Pattern.Inv_Hammer(df)

df = pd.read_csv("../data/cleaned_stocks/stock_0")
add_patterns(df)
df.head()

# applying this to all the csv files
count = 0
pbar = tqdm(total=1081)
while count < 1081:
    pbar.update(1)
    df = pd.read_csv(f"../data/cleaned_stocks/stock_{count}")
    add_patterns(df)
    df.to_csv(f"../data/with_patterns/stock_{count}",index=False)
    count+=1