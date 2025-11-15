import pandas as pd 

data = {
    'Name':['Musa', 'Gautam', 'Devanshu', None,'Shihab','Salaar','Harsh','Raunak'],
    'Age': [19, 20, 20, None,21,30,32,56],
    'Salaries':[75000,80000,120000,None,60000,125000,115000,150000],
    'Perfomance Score': [78,68,79,56,98,None,91,100]
}

df = pd.DataFrame(data)
print(df)


# #Dropna
# df.dropna(inplace=True)  # Drop rows with any NaN values
# print(df)

# Fillna 
df.fillna(0, inplace=True)  # Fill NaN values with 0
print(df)

df['Age'].fillna(df['Age'].mean(), inplace=True)  # Fill NaN in 'Age' with the mean of the column
print(df)