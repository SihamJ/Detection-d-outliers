import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

# Importer la structure de données Feuille
from Feuille import Feuille

from sklearn.cluster import KMeans
import numpy as np 

x = []
y = []
c = []

with open('data.csv','r') as csvfile:
     plots = csv.reader(csvfile, delimiter=',')
     for row in plots:
         x.append(float(row[0]))
         y.append(float(row[1]))
         c.append(float(row[2]))
plt.scatter(x,y,s=20, color='#10bbcf', label='Liers Data Frame')

plt.xlabel('x')
plt.ylabel('y')
plt.show()
x = np.array(x)
y = np.array(y)
data = (x,y)
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

# Clustering
classes, seuils = k_means(attr,2) 
feuille = Feuille(attribut = attribut, lower_split = seuils[0], higher_split = seuils[1])

# Prédictions
res = [0 for c in range(len(attr))]
for j in range(len(attr)):
    res[j] = feuille.predir(data[j,:])

# Plot
color = [0 for c in range(len(attr))]
for j in range(len(attr)):
    if res[j] == 0:
        color[j] = '#10bbcf'
    else:
        color[j] = '#eecc10'

plt.scatter(attr, y, c=color, s=20, cmap='viridis')
plt.axvline(x=seuils[0],linewidth = 1,color="r")
plt.axvline(x=seuils[1],linewidth = 1,color="r")
plt.xlabel('x')
plt.ylabel('y')

print('\nAprès Clustering:\n')
plt.show()

#3-Evaluation du Modèle
tp = 0
tn = 0
fp = 0
fn = 0

for i in range(len(c)):
    if(c[i] == res[i]):
        if(c[i] == 0):
            tn = tn + 1
        else:
            tp = tp + 1
    else:
        if(c[i] == 0):
            fp = fp + 1
        else:
            fn = fn + 1

print('\n_________________________________________________\n\nEvaluation du Modèle:\n_____________________')
print('\nTrue Negative:  '+str(tn)+' - True Positive:  '+str(tp)+'\nFalse Negative: '+str(fn)+' - False Positive: '+str(fp))
exactitude = (tp + tn) / (tp+tn+fp+fn)
exactitude_ponderee = ( (tp/(tp+fn)) + (tn/(tn+fp)) ) / 2
precision = tp/(tp+fp)
rappel = tp/(fn+tp)
print('\nExactitude: '+ str(exactitude) + '\nExactitude_ponderee: ' + str(exactitude_ponderee) + '\nPrécision: '+ str(precision) + '\nRappel: '+ str(rappel) + '\n')
print('_________________________________________________\n\n')
