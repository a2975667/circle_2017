import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
X = data.ix[:,:1] #[['TV']]
y = data.ix[:,3:4]
y_list = y['Sales'].values.tolist()

plt.hist(y_list)
plt.show()
