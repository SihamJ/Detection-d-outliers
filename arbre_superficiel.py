import matplotlib.pyplot as plt
import csv
from collections import Counter  # Used for counting

# Importer la structure de données Feuille

import numpy as np

from siham_work.Feuille import *

x = []
y = []
c = []

with open('data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        c.append(float(row[2]))
plt.scatter(x, y, s=20, color='#10bbcf', label='Liers Data Frame')

plt.xlabel('x')
plt.ylabel('y')
# plt.show()
x = np.array(x)
y = np.array(y)
data = (x, y)
data = np.array(data)
data = data.T

# Determiner l'attribut dont l'écart type est le plus grand
if np.nanstd(x) > np.nanstd(y):
    attr = x
    attribut = 0
else:
    attr = y
    attribut = 1


# Fonction K-means
def k_means(data, nb_clusters):
    j = 0
    res = [[0.0 for c in range(3)] for r in range(len(data))]
    clusters = [0 for c in range(len(data))]
    cluster_centers = np.array([np.amin(data), np.amax(data)])

    while (1):
        for j in range(len(data)):
            res[j][0] = abs(data[j] - cluster_centers[0])
            res[j][1] = abs(data[j] - cluster_centers[1])
            if res[j][0] < res[j][1]:
                clusters[j] = 0
            else:
                clusters[j] = 1
        j = 0
        while j < len(data):
            if (clusters[j] != res[j][2]):
                break
            j = j + 1
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


# Clustering
classes, seuils = k_means(attr, 2)
feuille = Feuille(attribut=attribut, lower_split=seuils[0], higher_split=seuils[1])

##4.2  Arbre superficiel TO DO BEFORE 28-03

from Node import Node


def buildDecisionTree(D, central, attribIdx):
    """
    
    :param D:  un ensemble de donne de taille Card(D), chaque donnee a n attributs
                numérotés de 1 à n
    :param central: indique si le noeud en cours de création provient de la branche centrale de
            son parent ou non, par convention => True pour la racine
    :param attribIdx:   liste pour indexer les parametres    !!! (not sur) !!!!
    :return:     un arbre de décision
    """
    if (len(D)) >= 4:
        if (len(attribIdx)) >= 2:
            print("coucou 1")

            currentAttrib = attr
            a = feuille.lower_split
            b = feuille.higher_split
            Dl = [x for x in attr if x < feuille.lower_split] #liste
            Dm = [x for x in attr if (feuille.lower_split >= x > feuille.higher_split)]
            Dr = [x for x in attr if x > feuille.higher_split]
            attribIdx = [x for x in currentAttrib if x not in attribIdx]
            L = buildDecisionTree(Dl, False, attribIdx)
            M = buildDecisionTree(Dm, True, attribIdx)
            R = buildDecisionTree(Dr, False, attribIdx)
            return Node(currentAttrib, a, b, L, M, R)
        else:
            print("coucou 2")
            return DecisionLeaf(D, attribIdx)
    elif len(D) < 4:
        if central:
            print("coucou 3")
            return DirectDecision(outlier=False)
        else:
            print("coucou 4")
            return DirectDecision(outlier=True)


attribIdx = list(range(1, len(data)))

tree = buildDecisionTree(data, True, attribIdx)


# EVALUATION
