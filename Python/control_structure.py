#control strctures
    #condition statement
    #loopings
    #jumping statements


#condition statement
    #if
    #if.else
    #if elif ladder
    #nested if
#loopings
    #while
    #for
#jumping statements
    #break
    #continue
    #pass
    #return

#condition statement

"""
a=6
b=3
c=1

start=0
begin=1

if(start or begin):
    if(a>b and a>c):
        print('a is big')
    elif(b>a and b>c):
        print('b is big')
    else:
        print('c is big')
else:
    print('not started')
"""

#loopings

#for loop
"""
for i in [1,2,3]:
    print(i,end='')
for i in range(0,10):
    print(i,end=' ')

for i in "hello":
    print(i,end=' ')
"""

"""
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=' ')
    print('\n')
else:
    print('out of range')
"""


#while loop
"""
i=10
while(i):
    print(i,end=' ')
    i=i-1
else:
    print('out of range')
"""

#jumping statements

#break
"""
for i in range(0,10):
    if(i==5): break
    print(i,end=' ')
"""

#continue
"""
for i in range(0,10):
    if(i==5):
        continue
    print(i,end=' ')
"""

#pass

"""
for i in range(0,10):
        pass
"""     


#return ->outside function cant use it gives error

"""
for i in range(0,10):
    if(i==5):
        return
    print(i,end=' ')
"""
