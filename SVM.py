import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import datasets
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing

data=datasets.load_breast_cancer()
Y=data.target
X=data.data
scaler=preprocessing.StandardScaler().fit(X)
X=scaler.transform(X)

X_tt, X_val, Y_tt, Y_val = train_test_split(X, Y, test_size=0.2)
X_train, X_test, Y_train, Y_test = train_test_split(X_tt, Y_tt, random_state=1)


gamma=10.0
C=np.logspace(0.0001,1,300)
Cb=0
scoreb=1000000
confb=[[0,0],[0,0]]
for c in C:
    kernel_svc=svm.SVC(C=c,kernel='linear')
    kernel_svc.fit(X_train, Y_train)

    Y_predict=kernel_svc.predict(X_test)
    conf= confusion_matrix(Y_test, Y_predict)

    score =2*conf[1,0]+conf[0,1]

    if(score<scoreb):
        scoreb=score
        Cb=c
        confb=conf

print confb
print scoreb, Cb
