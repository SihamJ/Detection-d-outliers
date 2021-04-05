import matplotlib.pyplot as plt
import csv
import numpy as np

import Functions as Functions
from Node import *


##################################################################################
## 1- Preparation des données
##################################################################################

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
print('\nRépartitions des données:\n')
plt.show()
x = np.array(x)
y = np.array(y)
data = (x, y, c)
data = np.array(data)
data = data.T
attribIdx = [c for c in range( data.shape[1] - 1 )]


###################################################################################
## 4-1: Feuille de décision
###################################################################################

print('\n\n4-1 Feuille de décision:\n')

attr, listAttr = Functions.Functions.meilleur_attribut( data.T, attribIdx )
classes, seuils = Functions.Functions.k_means( data.T[attr] )
dl = DecisionLeaf(data, attr)
tp, tn, fp, fn, exactitude, exactitude_ponderee, precision, rappel = dl.evaluer()
classes = dl.classes()

# Plot
color = [0 for c in range(len(listAttr))]
for j in range(len(listAttr)):
    if classes[j] == 0:
        color[j] = '#10bbcf'
    else:
        color[j] = '#eecc10'

plt.scatter(listAttr, y, c=color, s=20, cmap='viridis')
plt.axvline(x=seuils[0],linewidth = 1,color="r")
plt.axvline(x=seuils[1],linewidth = 1,color="r")
plt.xlabel('x')
plt.ylabel('y')


plt.show()
print('\nEvaluation du modèle:')

print('\nExactitude: '+ str(exactitude) + '\nExactitude ponderee: ' + str(exactitude_ponderee) + '\nPrécision: '+ str(precision) + '\nRappel: '+ str(rappel) + '\n')


###################################################################################
## 4-2: Arbre de décision
###################################################################################

print('\n\n4-2 Arbre de décision:\n')

arbre = Functions.Functions.buildDecisionTree(data, True, attribIdx)

tp, tn, fp, fn, exactitude, exactitude_ponderee, precision, rappel = arbre.evaluer()

for i in range(data.shape[0]):
    classes[i] = arbre.predict(data[i])

# Plot
color = [0 for c in range(len(listAttr))]
for j in range(len(listAttr)):
    if classes[j] == 0:
        color[j] = '#10bbcf'
    else:
        color[j] = '#eecc10'

plt.scatter(listAttr, y, c=color, s=20, cmap='viridis')
plt.axvline(x=seuils[0],linewidth = 1,color="r")
plt.axvline(x=seuils[1],linewidth = 1,color="r")
plt.xlabel('x')
plt.ylabel('y')

plt.show()

print('\nExactitude: '+ str(exactitude) + '\nExactitude ponderee: ' + str(exactitude_ponderee) + '\nPrécision: '+ str(precision) + '\nRappel: '+ str(rappel) + '\n')
