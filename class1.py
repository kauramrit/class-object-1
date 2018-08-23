# DICTIONARIES

#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop.

a=[1,2,3]
b=['a','b','c']
c={}
for i in range(len(a)):
    c[a[i]]=b[i]
print(c)

#Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.
#Print the marks of a given student from that dictionary for every subject. 
#Hint: Use nested dictionary to store subjects marks.

student={'qwe':{34,65,78},'abc':{45,87,98}}
A=input("enter name of elements")
for key,value in student.items():
    if A==key:
        print(value)
