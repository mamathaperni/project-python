# pandas
# the most important things in pands are dadaframes.
# dataframes are 2 dimensional table of data with rows and columns.
# each column is a series and each row is a index.
# dataframes are mutable, meaning you can change them after they are created.

import pandas as pd

# 3 people and there age:
#  people:p1,p2,p3
# age: 25,30,35

# first we put these data into a simple dictionary for creating a dataframe

d={'people':['p1','p2','p3'],'Age':[25,30,35]}

print(pd.DataFrame(d))

#   people  Age
# 0     p1   25
# 1     p2   30
# 2     p3   35


# to read excel file
import pandas as pd

# Read an Excel file
df = pd.read_excel("sample_practice.xlsx")

# To see the first few rows of your data
print(df.head())


# to read csv file




