#data structure
    #list
    #tuples
    #set
    #dictionary


#########################################################################

#list

#empty list declaration
"""
lists=[]
print(type(lists))
"""
"""
#list input
lists=list(input('enter numbers for list'))
print(type(lists))
print(lists)
"""

#list is mutable

"""
list1=[1,2,3,4]
list3=[5,3,1,4,'a']
list3[0]=7
print(list3)
#delete list
del list3
"""

#list concatination


list3=[5,3,1,4] #no redeclaration error
list2=[1,2,7]
#print(list3+list2)

#nested list
"""
list1=[list3,list2]
print(list1)
print(list1[1][2])
"""

#list assignment

"""
list1=[1,2,3,4]
a,b,c,d=list1
print(a,b,c,d)
"""

#list methods

list3.sort()
print(list3)
list3.remove(4)
print(list3)
list3.append(2)
print(list3)
list3.pop()
print(list3)

print(dir(list))

#list for strings

list4=["google","microsoft","dell","hp"]
print(list4[2][3])
print(list4[2])
print(list4)


#########################################################################

#tuples

"""
tuples=()
print(type(tuples))
"""

#tuples are immutables

"""
tuples=(1,2,3)
tuples[0]=7
print(tuples)
"""

#tuples concat

"""
tuples=(1,2,3,4.4,'t',"hi")
tuples2=(9,8,7,"hlo")
print(tuples,tuples2)

#nested tupless
tuples3=(tuples,tuples2)
print(tuples3)
print(tuples3[1][3])
#delete tuples
del tuples3
"""

#tuple assignment
"""
tuples=(1,2,3,4)
a,b,c,d=tuples
print(a,b,c,d)
"""
#tuples methods
print(dir(tuple))

#########################################################################

#set

#set immutable,error throw

"""
sets_1 = {0, 2, 4, 6, 8}
sets_1[1]=7
print(sets_1)
"""


#set values
sets_1 = {0, 2, 4, 6, 8}
print(sets_1)



#set assignment
sets_1 = {0, 2, 4, 6}
a,b,c,d=sets_1
print(a,b,c,d)

#set concat

sets_1 = {0, 2, 4, 6, 8,'a',"hi",3.3}
sets_2 = {1, 2, 3, 4, 5}
sets_3=sets_1,sets_2
print (sets_3)
#print (sets_3[0])#valid
#print (sets_3[0][6])#invalid

#set methods
sets_1 = {0, 2, 4, 6, 8}
sets_2 = {1, 2, 3, 4, 5}
print (0 in sets_1)
print (sets_1| sets_2,"else", sets_1.union(sets_2))
print (sets_1& sets_2,"else", sets_1.intersection(sets_2))
print (sets_1- sets_2,"else", sets_1.difference(sets_2))
print (sets_2- sets_1,"else", sets_2.difference(sets_1))
print (sets_1^ sets_2,"else", sets_1.symmetric_difference(sets_2) )



#####################################################################


#dictionary

#dictionary immutable

#empty dictioary  
dic={}
print(type(dic))

#dictionary initializations
dic1={1:"apple",2:"ball",3:"cat"}
print(dic1)
#delete dictionary
del dic1


#dictionary methods
dic1={1:"apple",2:"ball",3:"cat"}
print(dic1.items())
print(dic1.keys())
print(dic1.values())

dic1={"tech":"apple","lang":"python","car":"BMW","lang":"C"}
print(dic1.items())
print(dic1.keys())
print(dic1.values())



list1=[]
list2=[]
for i in dic1.keys():
    print(i)
    list1.append(i)

for i in dic1.values():
    print(i)
    list2.append(i)
    
print(list1)
print(list2)















