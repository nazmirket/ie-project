from excel import *
from forecast import *
import numpy as np

def init():
    clean()

def forecast():
    rows = readRows()

    mavg_n3 = moving_avg(rows, 3)
    mavg_n6 = moving_avg(rows, 6)

    exp_sm = []
    for i in range(1, 10): exp_sm.append(exp_smoothing(rows, i / 10))

    lreg = reg_analysis(rows)


    selected = lreg

    data = getDataFrame()
    values = data.values
    rRows = []
    for rIndex in range(0, len(data) - 1):
        temp = np.concatenate((values[rIndex][0:3], selected[rIndex]), axis=None)
        temp.resize(len(data.columns))
        rRows.append(temp)

    vdf = pd.DataFrame(data=rRows, columns=data.columns)


    try:
        vdf = vdf.drop(columns=['Unnamed: 0'])
        vdf.to_excel('output/forecast.xlsx')
    except:
        vdf.to_excel('output/forecast.xlsx')








