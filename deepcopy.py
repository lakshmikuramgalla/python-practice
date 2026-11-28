rnos = [3,5,7,9,12]
print(rnos,id(rnos))
import copy
drnos = copy.deepcopy(rnos)
print(drnos,id(drnos))

cls2_rnos = [[2,3],[4,5]]
# whole list memory address
print(cls2_rnos,id(cls2_rnos))
# element memory address
for i in cls2_rnos : 
    print(i,id(i))