## Feuille de décision:  

| exactitude pondérée   | Précision           | Rappel    |
| :-------------------: | :-----------------: | :-------: |
|        0.74975        | 0.5392156862745098  |    0.6875 |

## Arbre Superficiel:  
 
| exactitude pondérée   | Précision           | Rappel    |
| :-------------------: | :-----------------: | :-------: |
|       0.8005          | 0.651685393258427   |    0.725  |

## Arbre Généralisé:  

| Hauteur       | exactitude pondérée   | Précision           | Rappel    |
| :-----------: | :-------------------: | :-----------------: | :-------: |
| 1             |        0.74975        | 0.5392156862745098  |    0.6875 |
| 2             |        0.804          | 0.5714285714285714  |   0.8     |
| 3             |  0.5714999999999999   | 0.2987012987012987  |   0.575   |
| 4             |        0.5175         | 0.2541436464088398  |  0.575    |

## 3. Quelle hauteur vous semble donner les meilleurs résultats ?

Une hauteur de 2 donne les meilleurs résultats. Mais celle-ci n'est pas meilleure en précision que les résultats de l'arbre superficiel de la question 4-2, elle lui est égale en exactitude pondérée et est meilleure en rappel. Donc elle est moins précise dans la detection des outliers (plus de faux positifs), par contre elle detectera plus d'outliers que l'arbre superficiel qui en manquera certains. Et ceci est tout à fait normale, en améliorant le rappel on perdera un peu de précision.
