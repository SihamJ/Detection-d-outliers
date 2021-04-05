## 3-Structures


Pour notre arbre superficiel, il nous faut creer 3 classes, qui sont implimentées dans le fichier 
 ``'Node.py' ``  


- **DecisionLeaf**:
une feuille de decision avec comme attributs
     - **a**  `higher_split`
     - **b** `lower_split`
     - **currentAttrib** `l'attribut d'intérêt`
     - **D** `notre dataset`
  

```python
class DecisionLeaf():
       def __init__(self, data=None, currentAttrib=None):
            self.currentAttrib = currentAttrib
            self.D = data
            clusters, cluster_centers = Functions.Functions.k_means(self.D.T[self.currentAttrib])
            self.a = cluster_centers[0] 
            self.b = cluster_centers[1]
```
-------

- **DecisionDirect**: Une classe de decision directe avec comme attributs 
    
     - **D** `notre dataset`
     - **nb** `le nombre des exmples reste à traiters`
     - **outier** `type Boolean`
    
```python
class DirectDecision:
    def __init__(self, D, nb, outlier):
        self.outlier = outlier
        self.nb = nb
        self.D = D
```

---

- **Node**: Une classe pour l'arbre artificiel, avec comme attributs 
  
     - **a**  `higher_split`
     - **b** `lower_split`
     - **R** `sous-arbre/branche droit`
     - **L** `sous-arbre/branche gauche`
     - **C**  `sous-arbre/branche du centre`


```python
class Node:
    def __init__(self, currentAttrib = None, a = None, b = None, L = None, M = None, R = None):
        self.currentAttrib = currentAttrib
        self.a = a
        self.b = b
        self.R = R
        self.L = L
        self.M = M
```
---
