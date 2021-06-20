#string

#string imutable
"""
string="embedded"
string[0]='c'
print(string)
"""

#string access
string="embedded"
print(len(string))
print(string[0])
print(string[-8])
print(string+'\n')
print(string*2)

#string traverse
string="embedded"
index=0
for i in string:
    print('char',i, 'at index',index)
    index=index+1

#string slicing
#syntax --> string_name [start:end[:step]]
string="device"
print(string[1:]) #starting from
print(string[:3]) #ending to
print(string[1:4]) #start to end
print(string[0::2]) #two step skip

#string immutable,approach method using concat
string="device"
string='c'+string[1:]
print(string)

#string methods
"""
len(str)
max(str)
min(str)
upper()
lower()
"""
s
print(dir(str)) #to know more about methods

#string compare

print("january" == "jane")
print( "january" != "jane")
print("january" < "jane")
print( "january" > "jane")
print("january" <= "jane")
print( "january" >= "jane")
print ( "filled" > "")


#string with intergers
string="hello"
print(string*2)





