import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn import tree

data = pd.read_csv('heart_training_headings.txt', sep=" ", header='infer')

Y = data['output']
X = data.drop(['output'],axis=1)

clf = tree.DecisionTreeClassifier(criterion='gini',
             min_samples_leaf = 5)
clf = clf.fit(X, Y)

dot_data = tree.export_graphviz(clf,feature_names=X.columns, class_names=['0','1'], filled=True, 
                                out_file=None)  

testData = pd.read_csv('heart_testing_headings.txt', sep=" ", header='infer')

testY = testData['output']
testX = testData.drop(['output'],axis=1)

predY = clf.predict(testX)
predictions = pd.concat([testX,pd.Series(predY,name='output')], axis=1)

print('Accuracy: %.2f' % (accuracy_score(testY, predY)))

tp, tn, fp, fn = 0,0,0,0

for i in range(len(testX)):
    p = clf.predict([testX.iloc[i]])
    if testY[i] == 1 and p == 1:
        tp += 1
    elif testY[i] == 1 and p == 0:
        fn += 1
    elif testY[i] == 0 and p == 1:
        fp += 1
    elif testY[i] == 0 and p == 0:
        tn += 1

accuracy = (tp + tn)/(tp+tn+fp+fn)
print("TP = {}".format(tp))
print("TN = {}".format(tn))
print("FP = {}".format(fp))
print("FN = {}".format(fn))
