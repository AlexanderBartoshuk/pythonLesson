import numpy as np 
import pandas as pd

f500 = pd.read_csv('f500.csv', index_col=0)
f500.index.name = None


fifth_row = f500.iloc[4]
company_value = f500.iloc[0,0]

laptops = pd.read_csv('laptops.csv', index_col=0)

def clean_col(col):
    col = col.strip()
    col = col.replace('Operating system', 'os')
    col = col.replace('','_')
    col = col.replace('(','')
    col = col.replace(')','')    
    col = col.lower()
    return col

new_colums = [clean_col(c) for c in laptops.colums]
laptops.colums = new_colums

    