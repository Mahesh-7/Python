import sys

#author: guido van rossum
#python : highlevel lang ,1991 created
#using interpreter

#data types

"""
a=5
b=5.0
c="hello"
d='c'
e='hello'
f=[]
g=()
h={}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
"""

#variable declaration/initialization

"""
a,b,c=1,2,3  #valid
a=b=c=10     #valid
print(a,b,c)
"""

#sizeof of object


a=10
print(sys.getsizeof(a))


#len of string

"""
c='hello'
print(len(c))
"""

#operators

"""
a=5
b=10
print(a+b)
"""

#input and output with datatypes and typecast


a=int(input("enter your age\n"))

print(type(a))

print("\nage of person is",a)


#ascii to int conversion

"""
print(ord('a')) 
"""








    
