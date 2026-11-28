rnos = [1,2,3,4,5]
print(rnos,type(rnos),id(rnos))
# shallowcopy()
import copy
srnos = copy.copy(rnos)
print(srnos,type(srnos),id(srnos))

class1_rnos = [[2,3],[4,5]]
# whole list memory address
print(class1_rnos,id(class1_rnos))
# element memory address
for i in class1_rnos : 
    print(i,id(i))