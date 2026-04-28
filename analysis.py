print("PROGRAM STARTED")

import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt


data = pd.read_csv('data/data.csv')
labels = pd.read_csv('data/labels.csv')

print(data.shape, labels.shape)

merged = pd.concat([data, labels], axis=1)
print('\nMerged shape:', merged.shape)

print('duplicate:', merged.duplicated().sum())

merged= merged.dropna()

print('after cleaning:', merged.shape)

merged.to_csv('cleaned_dataset.csv', index=False)

print('\nNUMPY ANALYSIS:')

numeric_data = data.select_dtypes(include=[np.number])

mean_values = numeric_data.iloc[:, :5].mean()

print('First 5 gene means:')
print(mean_values)

plt.figure(figsize=(10,5))

plt.plot(mean_values.values)
plt.title('Mean Expression of First 5 Genes')
plt.xlabel('Gene Index')
plt.ylabel('Expression Level')


conn = sqlite3.connect('gene_data.db')

merged.iloc[:, :1000].to_sql('gene_expression', conn, if_exists='replace', index=False)


query = '''
SELECT * FROM gene_expression
LIMIT 10
'''

sql_result= pd.read_sql(query, conn)
print('\nSQL RESULT:')
print(sql_result)

conn.close()

merged.iloc[:, :100].to_excel('gene_expression_sample.xlsx', index=False)
print('\nExcel file saved.')

plt.savefig("gene_plot.png")

print("PROGRAM FINISHED")
