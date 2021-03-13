## 3-Evaluation


**Questions 1**  
Le modèle semble bien détecter les in-liners ( 1000/1002 ), mais pas les out-liners ( 5/35 ). Comme le but est de detecter les outliners, le modèle ne semble pas si bon.

**Questions 2**  
exactitude = (1000+2) / (1000+2+30+5) = 0.97  
exactitude pondérée = ( (5/35) + (1000/1002) ) / 2 = 0.57

**Questions 3**  
Parce que le modèle détecte bien les négatifs mais pas les positifs. Et comme les données dont nous disposons comprennent surtout des négatifs (in-liners), l'exactitude semblera bonne.

**Questions 4**  
Elle n'est pas pertinente car elle ne renseigne pas sur la capacité du modèle à detecter les out-liners, ce qui est notre but.



