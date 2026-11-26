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