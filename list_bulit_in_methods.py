# predefined methods in lists 
marks = [10,50,40,90,35,56,55,82,20,95,64]
print(marks,type(marks),id(marks))
# append()
print(marks.append(77))
print(marks,type(marks),id(marks))

topics = ["varaibles","data types","loops"]
print(topics,id(topics),type(topics))
new_topics = ["functions","statements"]
topics.append(new_topics)
print(topics,id(topics),type(topics))


mpc_subejcts = ["maths","chemistry","telugu","accounts"]
print(mpc_subejcts,type(mpc_subejcts),id(mpc_subejcts))
# clear()
mpc_subejcts.clear()
print(mpc_subejcts,type(mpc_subejcts),id(mpc_subejcts))

# copy()
fruits = ["apple","mango","orange"]
print(fruits,type(fruits),id(fruits))
items = fruits.copy()
print(items,type(items),id(items))

# count()
maths_marks = [35,50,72,40,35,25,30,10,5,60,70,50]
maths_marks.count(25)
maths_marks.count(5)
print(maths_marks,type(maths_marks))

# extend()
top_marks = [90,95,92,97]
maths_marks.extend(top_marks)
print(maths_marks)

# index()
game_score = [50,30,76,25,84,81,55,43,10,25,50]
print(game_score.index(30))

# insert()
game_score.insert(3,90)
print(game_score)
game_score.insert(-1,95)
print(game_score)

# pop()
print(game_score.pop())
print(game_score)

# pop(index)
print(game_score.pop(-4))
print(game_score)

# remove()
game_score.remove(25)
print(game_score)

# reverse()
game_score.reverse()
print(game_score)

# sort()
game_score.sort()
print(game_score)
game_score.sort(reverse=True)
print("descending sorting :" ,game_score)

# del operator in list
marks2 = [10,20,45,59,77,92,90,84]
del marks2[0]
print(marks2)
del marks2[1:4]
print(marks2)
del marks2 # list deleted in memory loaction
print(marks2)
