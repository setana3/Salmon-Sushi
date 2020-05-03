import pandas as pd 
import os

file = os.listdir('./')[1]

print(file)


df = pd.read_csv(file,sep=',')

#datafram row, column
print(df.shape)

#dataframe index 
print(df.index)

#dataframe clumns 
print(df.columns)

#dataframe data types 
print(df.dtypes)


