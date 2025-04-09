import numpy as np 
import pandas as pd

f500 = pd.read_csv('f500.csv', index_col=0)
f500.index.name = None


fifth_row = f500.iloc[4]
company_value = f500.iloc[0,0]
