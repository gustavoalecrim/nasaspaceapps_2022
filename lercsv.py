import pandas as pd
import os

os.chdir('/home/egca/Documentos/Dev/python/base_dados')

df = pd.read_csv('ASCENDS-AVOCET-CH4_DC8_20170720_R0.csv')
print(df.head(10))

#coluna rótulo: 'churned'
# número de clientes:
len(df)

