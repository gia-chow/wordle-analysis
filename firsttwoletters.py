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
# word_list = word_column.to_list()
# print(word_list)

first_two_letters = ' '.join([f"{w[:2].upper()}" for w in word_column])

print(first_two_letters)


