import pandas as pd 

data = {
    'Name':['Musa', 'Gautam', 'Devanshu', 'HariOm'],
    'Age': [19, 20, 20, 22],
    'City': ['Bhopal','dont know','dont know','dont know']
}


df = pd.DataFrame(data)
print(df)


df.to_json("output.csv", index=False)

# print(df.info())