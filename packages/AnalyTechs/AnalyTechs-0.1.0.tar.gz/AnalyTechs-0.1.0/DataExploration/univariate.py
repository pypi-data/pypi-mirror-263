import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Entropy Based Binning
def entr_plot(data, bin_name, numval, catval):
    data[bin_name] = pd.cut(data[numval],  bins=3, right=False)
    data.groupby(bin_name)[catval].value_counts().unstack().plot(kind='bar')
    plt.xlabel(numval)
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()
    
# Equal Width Based - Unsupervised
def equal_width(data, bins):
    width = (max(data) - min(data)) / bins
    boundaries = [min(data) + x * width for x in range(1, bins)]
    bin = np.split(np.sort(data), np.searchsorted(np.sort(data), boundaries))
    return bin

def ewidth_plot(data):
    ew1 = [f'{x[0]} - {x[-1]}' for x in data]
    ew2 = [sum(x) for x in data]
    
    plt.bar(ew1, ew2)
    plt.xlabel('Values')
    plt.ylabel('Width')
    plt.show()
        

# Equal Frequency Based - Unsupervised
def equal_freq(data, bins):
    freq = sorted(data)
    size = len(data) // bins
    boundaries = [freq[x * size] for x in range(1, bins)]
    bin = np.split(freq, np.searchsorted(freq, boundaries))
    return bin

def  efreq_plot(data):
    ef1 = [f'{x[0]} - {x[-1]}' for x in data]
    ef2 = [sum(x) for x in data]

    plt.bar(ef1, ef2)
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.show()

# Encoding - Binary
def binary_encoding(data, values):
    encode = pd.get_dummies(data[values])
    encoded = encode.astype(int)
    return encoded


# Missing Values - Imputation
def impute_values(data):
    find_missing = data.columns[data.isna().any()].tolist()

    for values in find_missing:
        random_values = data[values].dropna().sample(data[values].isnull().sum(), random_state=0)
        random_values.index = data[data[values].isnull()].index
        data.loc[data[values].isnull(), values] = random_values
    return data

