import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

train=pd.read_csv("heart_training.txt",sep=' ',header=None)
test=pd.read_csv("heart_testing.txt", sep=' ', header=None)


train = np.asarray(train)
test = np.asarray(test)

train_X=train[:,:-1]
test_X = test[:,:-1]

train_Y=train[:,-1]
test_Y=test[:,-1]

#Source: https://scikit-learn.org/stable/modules/preprocessing.html
m_m = MinMaxScaler()
train_X = m_m.fit_transform(train_X)
test_X = m_m.fit_transform(test_X)

def testKNN(train_X, test_X, test_Y, k):
    #Source for KNN: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
    neigh = KNeighborsClassifier(n_neighbors = k)
    neigh.fit(train_X, train_Y)
    return neigh.score(test_X, test_Y)

acc_vals = [0 for k in range(244)]

for k in range(1, 244):
   acc_vals[k] = testKNN(train_X, test_X, test_Y, k)
    
#Source: https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
plt.plot([k for k in range(244)],acc_vals)
plt.axis([1,244,0.45,0.85])
plt.show()

k = 7
tp, tn, fp, fn = 0,0,0,0
neigh = KNeighborsClassifier(n_neighbors = k)
neigh.fit(train_X, train_Y)
for i in range(len(test_X)):
    p = neigh.predict([test_X[i]])
    if test_Y[i] == 1 and p == 1:
        tp += 1
    elif test_Y[i] == 1 and p == 0:
        fn += 1
    elif test_Y[i] == 0 and p == 1:
        fp += 1
    elif test_Y[i] == 0 and p == 0:
        tn += 1

accuracy = (tp + tn)/(tp+tn+fp+fn)
print("TP = {}".format(tp))
print("TN = {}".format(tn))
print("FP = {}".format(fp))
print("FN = {}".format(fn))
print("Accuracy: {}".format((tp + tn)/(tp + tn + fp + fn)))
