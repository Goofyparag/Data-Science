import pandas as pd 

data = {
    'Name':['Musa', 'Gautam', 'Devanshu', 'HariOm','Shihab','Salaar','Harsh','Raunak'],
    'Age': [19, 20, 20, 22,21,30,32,56],
    'Salaries':[75000,80000,120000,40000,60000,125000,50000,150000],
    'Perfomance Score': [78,68,79,56,98,83,91,100]
}

df = pd.DataFrame(data)

high_sal = df[df['Salaries'] > 70000]
print(f"\nMore then 70K salry: {high_sal}\n")

# filtered

filtered = df[(df['Salaries'] > 70000) & (df['Age'] >= 19)]
print(f'\nMore then 70k Salary & 19year Age: {filtered}\n ')