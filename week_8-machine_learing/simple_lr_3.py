import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
X = data.ix[:,:1] #[['TV']]
y = data.ix[:,3:4]

X_train = X[0:160]
y_train = y[0:160]
X_test = X[161:]
y_test = y[161:]

from sklearn import linear_model
#model = linear_model.LinearRegression()
model = linear_model.Lasso(alpha = 0.1)

model.fit(X_train,y_train)

print (model.score(X_test, y_test))
print (model.intercept_)
print (model.coef_)

plt.scatter(X_train, y_train, color='blue')
plt.scatter(X_test, y_test, color='red')
plt.plot(X[151:], model.predict(X[151:]), color='green',linewidth=3)

plt.show()
