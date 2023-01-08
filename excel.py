import pandas as pd
import numpy as np
from forecast import *

def clean():
    df = pd.read_excel('resources/data.xlsx', sheet_name=[0])[0]
    abc = abc_analysis(df)
    writeData(abc.values, ['sum', 'category'], 'output/abc.xlsx', df)
    df_abc = pd.read_excel('output/abc.xlsx', sheet_name=[0])[0]
    df_abc = df_abc[(df_abc['category'] == 'A')]
    df_abc = df_abc.drop(columns=['category', 'sum', 'Unnamed: 0'])
    df_abc.to_excel('resources/clean.xlsx')

def getDataFrame():
    df = pd.read_excel('resources/clean.xlsx', sheet_name=[0])
    return df[0]

def readRows():
    return getDataFrame().values

def readCols():
    return  getDataFrame().columns   

def writeData(values, cols, out, org):
    data = org.values
    rows = []

    for rIndex in range(0, len(data) - 1):
        row = np.concatenate((data[rIndex][0:2], values[rIndex]), axis=None)
        rows.append(row)

    colsFixed = np.concatenate((org.columns, cols), axis=None)

    vdf = pd.DataFrame(data=rows, columns=colsFixed)

    vdf.to_excel(out)
    

    


