from excel import *
from forecast import *
import numpy as np

fCount = 4

def init():
    clean()

def forecast(method):
    rows = readRows()

    # Moving Averages
    if(method=='mvg'):
        a_mvg_n3 = moving_avg(rows, 3)
        a_mvg_n6 = moving_avg(rows, 6)
        output(a_mvg_n3, 'Moving_Average_N3')
        output(a_mvg_n6, 'Moving_Average_N6')
        error(mape(rows, a_mvg_n3),'Moving_Average_N3')
        error(mape(rows, a_mvg_n6),'Moving_Average_N6')

    # Exponential Smoothing
    if(method=='exp'):
        a_exps = []
        for i in range(1, 11): a_exps.append(exp_smoothing(rows, i / 10))
        for i in range(0, 10):
            name = 'Exponential_Smoothing_a' + str(((i+1)/10))
            output(a_exps[i], name)
            error(mape(rows, a_exps[i]), name)

    # Exponential Smoothing
    if(method=='reg'):
        a_reg = reg_analysis(rows)
        output(a_reg,'Regression_Analysis')
        error(mape(rows, a_reg), 'Regression_Analysis')

   
def output(result, name):
    data = getDataFrame()
    values = data.values
    rRows = []
    for rIndex in range(0, len(data) - 1):
        rounded = np.round(result[rIndex][0:fCount])
        temp = np.concatenate((values[rIndex][0:2], rounded), axis=None)
        rRows.append(temp)

    vdf = pd.DataFrame(data=rRows, columns=data.columns[0:fCount+2])

    oPath = 'output/' + name + '.xlsx'

    try:
        vdf = vdf.drop(columns=['Unnamed: 0'])
        vdf.to_excel(oPath)
    except:
        vdf.to_excel(oPath)

def error(errs, name):
    data = getDataFrame()
    values = data.values
    rRows = []

    for rIndex in range(0, len(data) - 1):
        temp = np.concatenate((values[rIndex][0:2], errs[rIndex]), axis=None)
        rRows.append(temp)

    cols = np.concatenate((data.columns[0:2],['error']))
    vdf = pd.DataFrame(data=rRows, columns=cols)


    oPath = 'output/' + name + '_Error.xlsx'

    try:
        vdf = vdf.drop(columns=['Unnamed: 0'])
        vdf.to_excel(oPath)
    except:
        vdf.to_excel(oPath)





