import pandas as pd 

data = {
    'Name':['Musa', 'Gautam', 'Devanshu', 'HariOm','Shihab','Salaar','Harsh','Raunak'],
    'Age': [19, 20, 20, None,21,30,32,56],
    'Salaries':[75000,80000,120000,40000,60000,125000,115000,150000],
    'Perfomance Score': [78,68,79,56,98,83,91,100]
}

df = pd.DataFrame(data)
print(df)

df.interpolate(method='linear', inplace=True) 
print("\nAfter Interpolation:",df) 

#Polynomial interpolation
df.interpolate(method='polynomial', order=2, inplace=True)    

print("\nAfter Polynomial Interpolation:", df)

# Time series interpolation
df['Date'] = pd.date_range(start='2023-01-01', periods=len(df), freq='D')   
df.set_index('Date', inplace=True)  