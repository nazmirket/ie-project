import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error

from abc_analysis import abc_analysis as ABC

def moving_avg(data, n):
  result = []

  for rIndex in range(0, len(data)):
      row = data[rIndex][2:]
      
      avgs = []
      i = 0

      while i < len(row) - n + 1:
        part = row[i:i+n]
        sum = np.sum(part)
        avg = sum / n
        avgs.append(avg)
        i += 1
      
      result.append(avgs)
  return result

def exp_smoothing(data, a):
  result = []

  for rIndex in range(0, len(data)):
      row = data[rIndex][2:]

      preds = [row[0]]
      for i in range(1,len(row)-1):
         pred = (a*row[i]) + ((1-a) * preds[i-1])
         preds.append(pred)

      result.append(preds)
      
  return result



def reg_analysis(data):
  result = []

  for rIndex in range(0, len(data) - 1):
    row = data[rIndex][2:]
      
    x = []
    y = []

    for i in range(1, len(row) + 1):
      x.append([i])
      y.append([row[i-1]])        

    model = LinearRegression().fit(x, y)
    preds = model.predict(x)
    result.append(preds)
      
  return result
  


def abc_analysis(df):
    print(df)
    subframe = df.iloc[:,2:]
    subframe['sum'] = df.iloc[:, 2:].sum(axis=1)
    result = ABC(subframe['sum'])

    subframe['category'] = np.empty(len(subframe))

    for i in result['Aind']: 
      subframe.at[i,'category'] = 'A'

    for i in result['Bind']: 
      subframe.at[i,'category'] = 'B'

    for i in result['Cind']: 
      subframe.at[i,'category'] = 'C'
    
    return subframe



def original(data, l):
  result = []
  for rIndex in range(0, len(data)):
      result.append(data[rIndex][2:(l+2)]) 
  return result


def mape(data, frc):
  org = original(data, 4)
  errs = []
  for i in range(0,len(frc)):
    o = org[i]
    f = frc[i][0:4]
    errs.append(mean_absolute_percentage_error(o, f))
  return errs



