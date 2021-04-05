import uuid

import Functions as Functions
import numpy as np

class DecisionLeaf():


    def __init__(self, data=None, currentAttrib=None):
        self.currentAttrib = currentAttrib
        self.D = data
        clusters, cluster_centers = Functions.Functions.k_means(self.D.T[self.currentAttrib])
        self.a = cluster_centers[0] 
        self.b = cluster_centers[1]

    def classes(self):
        classes = [ 0 for x in range(self.D.shape[0]) ]
        j = 0
        for i in self.D:
            if i[self.currentAttrib] <= self.a or i[self.currentAttrib] > self.b:
                classes[j] = 1
            j = j + 1
        return classes

    def evaluer(self):
        tp = 0
        tn = 0
        fp = 0
        fn = 0

        for i in self.D:
            if i[self.currentAttrib] <= self.a or i[self.currentAttrib] > self.b:
                if i[self.D.shape[1]-1] == 1:
                    tp = tp + 1
                else:
                    fp = fp + 1
            else:
                if i[self.D.shape[1]-1] == 0:
                    tn = tn + 1
                else:
                    fn = fn + 1

        exactitude = (tp + tn) / (tp+tn+fp+fn)
        exactitude_ponderee = ( (tp/(tp+fn)) + (tn/(tn+fp)) ) / 2
        precision = tp/(tp+fp)
        rappel = tp/(fn+tp)
        return tp, tn, fp, fn, exactitude, exactitude_ponderee, precision, rappel

    def predict(self, data):
        if data[self.currentAttrib] <= self.a or data[self.currentAttrib] > self.b:
            return 1
        else:
            return 0


class DirectDecision:
    def __init__(self, D, nb, outlier):
        self.outlier = outlier
        self.nb = nb
        self.D = D

    def evaluer(self):
        tp = 0
        tn = 0
        fp = 0
        fn = 0

        for i in self.D:
            if i[self.D.shape[1]-1] == 1:
                if self.outlier == True:
                    tp = tp + 1
                else:
                    fp = fp + 1
            else:
                if self.outlier == False:
                    tn = tn + 1
                else:
                    fn = fn + 1

        exactitude = (tp + tn) / (tp+tn+fp+fn)
        exactitude_ponderee = ( (tp/(tp+fn)) + (tn/(tn+fp)) ) / 2
        precision = tp/(tp+fp)
        rappel = tp/(fn+tp)

        return tp, tn, fp, fn, exactitude, exactitude_ponderee, precision, rappel

    def predict(self, data):
        if self.outlier == True:
            return 1
        else:
            return 0

class Node:
    def __init__(self, currentAttrib = None, a = None, b = None, L = None, M = None, R = None):
        self.currentAttrib = currentAttrib
        self.a = a
        self.b = b
        self.R = R
        self.L = L
        self.M = M

    def evaluer(self):
        tp1, tn1, fp1, fn1, exactitude, exactitude_ponderee, precision, rappel = self.L.evaluer()
        tp2, tn2, fp2, fn2, exactitude, exactitude_ponderee, precision, rappel = self.M.evaluer()
        tp3, tn3, fp3, fn3, exactitude, exactitude_ponderee, precision, rappel = self.R.evaluer()
        tp = tp1+tp2+tp3
        tn = tn1+tn2+tn3
        fp = fp1+fp2+fp3
        fn = fn1+fn2+fn3
        exactitude = (tp + tn) / (tp+tn+fp+fn)
        exactitude_ponderee = ( (tp/(tp+fn)) + (tn/(tn+fp)) ) / 2
        precision = tp/(tp+fp)
        rappel = tp/(fn+tp)
        return tp, tn, fp, fn, exactitude, exactitude_ponderee, precision, rappel

    def predict(self, data):
        if data[self.currentAttrib] <= self.a:
            return self.L.predict(data)
        elif data[self.currentAttrib] > self.b:
            return self.M.predict(data)
        else:
            return self.R.predict(data)
