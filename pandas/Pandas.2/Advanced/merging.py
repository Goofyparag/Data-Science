import pandas as pd 

data = {
    'Name':['Musa', 'Gautam', 'Devanshu', 'HariOm','Shihab','Salaar','Harsh','Raunak'],
    'Age': [19, 20, 20, 22,21,30,32,56],
    'Salaries':[75000,80000,120000,40000,60000,125000,115000,150000],
    'Perfomance Score': [78,68,79,56,98,83,91,100]
}

data2 = {
    'Name':['Musa', 'Gautam', 'Devanshu', 'HariOm','Shihab','Salaar','Harsh','Raunak'],
    'Age': [19, 25, 20, 26,25,33,32,56],
    'Salaries':[75000,80000,120000,40000,60000,125000,115000,150000],
    'Perfomance Score': [78,68,79,56,98,83,91,100]
    
}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

df_m = pd.merge(data, data2, on='Age', how='inner')
print('inner join')
print(df_m)