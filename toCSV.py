import numpy as np
import pandas as pd

data_txt = np.loadtxt('datas_train.txt')
data_txtDF = pd.DataFrame(data_txt)
data_txtDF.to_csv('datas_train.csv', index=False)
