import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

x = np.array([
    [1,2],
    [1,1],
    [3,2],
    [4,3],
    [5,3],
    [6,4],
    [8,6],
    [9,6]
])

y = np.array([2,4,5,7,9,10,12,13])

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

reg = LinearRegression()
reg.fit(x_train,y_train)

y_pred_test = reg.predict(x_test)
y_pred_all = reg.predict(x)

r2 = r2_score(y_test, y_pred_test)
print(reg.intercept_)
print(reg.coef_)
print(r2)

plt.scatter(y,y_pred_all)
plt.plot([y.min(),y.max()],[y.min(),y.max()])
plt.show()