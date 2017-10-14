import pandas as pd
import csv

# file = input('Enter file path: ')
file = "C:\\Users\BADRINAR\Desktop\Test_data.csv"

df = pd.read_csv(file, skiprows=149, nrows=150)
dtype = df.dtypes
print(type(dtype))


# print(header)