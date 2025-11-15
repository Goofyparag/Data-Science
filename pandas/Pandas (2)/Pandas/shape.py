"""
1- How big is your data set
2- what are the name of colums

shape and columns
"""



import pandas as pd 

data = {
    'Name':['Musa', 'Gautam', 'Devanshu', 'HariOm','Shihab','Salaar','Harsh','Raunak'],
    'Age': [19, 20, 20, 22,21,30,32,56],
    'Salaries':[75000,80000,120000,40000,60000,125000,115000,150000],
    'Perfomance Score': [78,68,79,56,98,83,91,100]
}

df = pd.DataFrame(data)

print(f'Shape: \n {df.shape}')
print(f'Column: \n {df.columns}')