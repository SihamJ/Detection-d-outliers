## 3-Evaluation


**Question 1**  
Le modèle semble bien détecter les inliers ( 1000/1002 ), mais pas les outliers ( 5/35 ). Comme le but est de detecter les outliers, le modèle ne semble pas si bon.

**Question 2**  
exactitude = (1000+2) / (1000+2+30+5) = 0.97  
exactitude pondérée = ( (5/35) + (1000/1002) ) / 2 = 0.57

**Question 3**  
Parce que le modèle détecte bien les négatifs mais pas les positifs. Et comme les données dont nous disposons comprennent surtout des négatifs (inliers), l'exactitude semblera bonne.

**Question 4**  
Elle n'est pas pertinente car elle ne renseigne pas sur la capacité du modèle à detecter les outliers, ce qui est notre but.


