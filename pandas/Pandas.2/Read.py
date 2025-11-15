import pandas as pd

RF = pd.read_csv("sales_data_sample.csv", encoding="latin1")
# RF = pd.read_excel('SampleSuperstore.xlsx')
RF = pd.read_json('Sample_Data.json')

print(RF)


