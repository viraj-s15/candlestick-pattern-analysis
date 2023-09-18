import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../data/with_patterns/stock_0.csv")
columns = df.columns
columns = columns[5:]

sentiment = ["both","upward","upward","downward","upward","upward","downward","reversal","upward","upward","downward","both","downward"]

mapping = dict(zip(columns,sentiment))

print(mapping)