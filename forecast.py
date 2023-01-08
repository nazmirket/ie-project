import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

from abc_analysis import abc_analysis as ABC

def moving_avg(data, n):
  result = []

  for rIndex in range(0, len(data)):
      row = data[rIndex][3:]
      
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

  for rIndex in range(0, len(data)):
    row = data[rIndex][2:]
      
    x = []
    y = []

    for i in range(1,12):
      x.append([i])
      y.append([row[i-1]])        

    model = LinearRegression().fit(x, y)
    preds = model.predict(x)
    result.append(preds)
      
  return result
  


def abc_analysis(df):
    subframe = df.iloc[:, 2:14]
    subframe['sum'] = df.iloc[:, 2:14].sum(axis=1)
    result = ABC(subframe['sum'])

    subframe['category'] = np.empty(len(subframe))

    for i in result['Aind']: 
      subframe.at[i,'category'] = 'A'

    for i in result['Bind']: 
      subframe.at[i,'category'] = 'B'

    for i in result['Cind']: 
      subframe.at[i,'category'] = 'C'
    
    return subframe

def mape():
  return



