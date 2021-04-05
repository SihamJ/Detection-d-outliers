import numpy as np
from Node import *

class Functions:

    # Determiner l'attribut dont l'écart type est le plus grand. attribIdx est une matrice contenant les listes des attributs.
    @classmethod
    def meilleur_attribut(cls, data, attribIdx):
        currentAttrib = 0
        listAttr = data[currentAttrib]
        for a in range(len(attribIdx)-1) :
            if np.nanstd(data[a]) < np.nanstd(data[a+1]):
                currentAttrib = a + 1
                listAttr = data[a+1]
        return currentAttrib, listAttr

    # Fonction K-means
    @classmethod
    def k_means(cls, data):
        j = 0
        res = [[0.0 for c in range(3)] for r in range(len(data))]
        clusters = [0 for c in range(len(data))]
        cluster_centers = np.array([np.amin(data),np.amax(data)])
 
        while(1):
            for j in range(len(data)):
                res[j][0] = abs(data[j] - cluster_centers[0])
                res[j][1] = abs(data[j] - cluster_centers[1])
                if res[j][0] < res[j][1]:
                    clusters[j] = 0
                else:
                    clusters[j] = 1
            j = 0
            while j<len(data):
                if(clusters[j] != res[j][2]):
                    break
                j = j+1
            if j == len(data):
                break
            else:
                cluster_centers[0] = 0.0
                cluster_centers[1] = 0.0
                nb_1 = 0.0
                nb_2 = 0.0
                for j in range(len(clusters)):
                    res[j][2] = clusters[j]
                    if clusters[j] == 0:
                        cluster_centers[0] = cluster_centers[0] + data[j]
                        nb_1 = nb_1 + 1.0
                    else:
                        cluster_centers[1] += data[j]
                        nb_2 = nb_2 + 1.0
                cluster_centers[0] = cluster_centers[0] / (nb_1)
                cluster_centers[1] = cluster_centers[1] / (nb_2)
        return clusters, cluster_centers

    @classmethod
    def getSplitParameters(cls, attribIdx, D):
        currentAttrib, listAttr = cls.meilleur_attribut(D.T, attribIdx)
        clusters, cluster_centers = cls.k_means(D.T[currentAttrib])
        return currentAttrib, listAttr, cluster_centers[0], cluster_centers[1]

    @classmethod
    def buildDecisionTree(cls, D, central, attribIdx):
        currentAttrib = 0
        if len(D) >= 4:
            if len(attribIdx) >= 2:
                currentAttrib, listAttr, a, b = cls.getSplitParameters( attribIdx, D)
                attribIdx = np.delete(attribIdx, currentAttrib, 0)
                Dl = np.array([x for x in D if x[currentAttrib] <= a]) #liste droite
                Dm = np.array([x for x in D if x[currentAttrib] > a and x[currentAttrib] <= b]) # liste du centre
                Dr = np.array([x for x in D if x[currentAttrib] > b]) # liste de gauche
                L = cls.buildDecisionTree(Dl, False, attribIdx)
                M = cls.buildDecisionTree(Dm, True, attribIdx)
                R = cls.buildDecisionTree(Dr, False, attribIdx)
                return Node(currentAttrib, a, b, L, M, R)

            else:
                currentAttrib = attribIdx[0]
                return DecisionLeaf(D,currentAttrib)

        elif len(D) < 4:
            nb = len(D)
            if central:
                return DirectDecision(D, nb, outlier = False)
            else:
                return DirectDecision(D, nb, outlier = True)

