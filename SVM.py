import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import datasets
from sklearn.datasets import make_classification
#from sklearn.model_selection import train_test_split

data=datasets.load_breast_cancer()
Y=data.target

#X_train, X_test, Y_train, Y_test=train train_test_split()

C=1.0
gamma=1.0
kernel_svc=svm.SVC(C=C,kernel='rbf',gamma=gamma)
kernel_svc.fit
