import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections
from collections import Counter

# Read the dataset
df = pd.read_csv("/Users/eugeniachow/downloads/wordle.csv")

# Get values of third column
first = df.iloc[:,3]

c = (Counter(first))


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

d = collections.Counter(c)

plt.bar(d.keys(), d.values())

plt.show()