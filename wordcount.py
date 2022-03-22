import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections
from collections import Counter

# Read the dataset
df = pd.read_csv("/Users/eugeniachow/downloads/wordle.csv")

# Get values of third column
word_column = df.iloc[:,2]

# Convert column into list
word_list = word_column.to_list()
# print(word_list)

c = Counter()
for words in word_list:
    for letters in set(words):
        c[letters]+=1
# print(c)

# Plot results on bar chart
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

d = collections.Counter(c)

plt.bar(d.keys(), d.values())

plt.show()