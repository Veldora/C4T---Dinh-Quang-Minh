# -*- coding: utf-8 -*-


from sklearn.svm import LinearSVC
from sklearn.externals import joblib
import glob
import os
from Last_session.config import *
import numpy as np

def train_svm():
    pos_feat_path = 'data/features/pos'
    neg_feat_path = 'data/features/neg'

    # Classifiers supported
    clf_type = 'LIN_SVM'

    fds = []
    labels = []
    # Load the positive features
    for feat_path in glob.glob(os.path.join(pos_feat_path,"*.feat")):
        fd = joblib.load(feat_path)
        temp1 = np.reshape(fd[0], (1, -1))
        temp2 = np.reshape(fd[1], (1, -1))
        temp = np.zeros((1, (len(temp1[0, :]) + len(temp2[0, :]))))
        temp[0, 0:len(temp1[0,:])] = temp1[0, :]
        temp[0, len(temp1[0, :]):] = temp2[0, :]
        fds.append(temp[0, :])
        labels.append(1)

    # Load the negative features
    for feat_path in glob.glob(os.path.join(neg_feat_path,"*.feat")):
        fd = joblib.load(feat_path)
        temp1 = np.reshape(fd[0], (1, -1))
        temp2 = np.reshape(fd[1], (1, -1))
        temp = np.zeros((1, (len(temp1[0, :]) + len(temp2[0, :]))))
        temp[0, 0:len(temp1[0, :])] = temp1[0, :]
        temp[0, len(temp1[0, :]):] = temp2[0, :]
        fds.append(temp[0, :])
        labels.append(0)
    print (np.array(fds).shape,len(labels))
    if clf_type is "LIN_SVM":
        clf = LinearSVC()
        print ("Training a Linear SVM Classifier")
        clf.fit(fds, labels,None)
        # If feature directories don't exist, create them
        if not os.path.isdir(os.path.split(model_path)[0]):
            os.makedirs(os.path.split(model_path)[0])
        fd_name = os.path.split(model_path)[1].split(".")[0] + ".model"
        fd_path = os.path.join(model_path, fd_name)
        joblib.dump(clf, fd_path)
        print ("Classifier saved to {}".format(model_path))
        
#训练SVM并保存模型
train_svm()