import numpy as np
source = [0,1,31265,310,5]
attribIdx = {item: idx for idx, item in enumerate(source)}

items_to_find = [31265,5]

#print( [attribIdx.get(item) for item in items_to_find] )

N = [i for i in range(len(source)) if source[i] in items_to_find]
print(N)