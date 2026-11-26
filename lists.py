# Lists data type

# creating a Empty List
marks = []  # method 1
print(marks,type(marks),id(marks))

# method 2 with function
marks = list()
print(marks,type(marks),id(marks))

# non Empty List creation
marks = [10,20,60,"fail",7.7,2+3j,15,35,65,77]
print(marks,type(marks),id(marks))
print(marks[3])
print(marks[0:3])
print(marks[-5:-1])
print(marks[0:8:2])
print(marks[8:4:-1])
print(marks[-1:-8:-2])
print(marks[-len(marks)])
print(marks[len(marks)-1])
print(len(marks))