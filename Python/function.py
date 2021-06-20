
#functions and types


#function definition
def main():
    print('main function')

#function call 
main()

#function call 2 method

if __name__ == "__main__":
    main()


############################################


#function definition
def msg(data):
    if (data != 0):
        print('hello',data)
        return True
    else:
        return False
    
#function call    
status=msg('coder')
if(status==True):
   print('data printed')
else:
   print('data not printed')


############################################

#nested function variables scope

test_variable = 5

def outer_function():
    test_variable = 60
    def inner_function():
        test_variable = 100
        print(test_variable)
    inner_function()
    print(test_variable)
      
outer_function()
print("Global variable value",test_variable)


############################################

#function with initialized arg


def tech(data,t="systems"):
    print(data,t)
    
tech('embedded')


############################################

#Recursion functions

def fact(x):
    if(x==1):
        return 1
    else:
        return x*fact(x-1)
print(fact(5))






































