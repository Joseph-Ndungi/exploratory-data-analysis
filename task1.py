import csv
import pandas as pd

# Read three csv files and combine them into one dataframe
df1 = pd.read_csv('IT Salary Survey EU  2020.csv')
df2 = pd.read_csv('IT Salary Survey EU 2018.csv')
df3 = pd.read_csv('T Salary Survey EU 2019.csv')
df = pd.concat([df1, df2, df3])

df.head()

#no of rows and columns
df.shape

#data types
df.dtypes

#check for null values
df.isnull().sum()

#summary statistics
df.describe()

