#polymorphism -same function used in different forms with different arg

#using methods
#using inheritance

#types
    #compile-time polymorphism(func overloading)
    #run-time polymorphism(func over-riding)

#using methods,#methods overloading

"""
def sum(a,b,c=0):
    print(a+b+c)

sum(5,6)
sum(3,4,5)
"""

#using inheritance

class smartphone:
    def __init__(self,brand):
        self.brand=brands
        
    #methods overloading
    def msg(self,year,ver=0):
        print('smartphone available in diff brands in',year,'with version',ver)

    #methdos overriding 
    def model(self):
        print('demo brands')
    
class nokia(smartphone):
    #methods overriddings
    def model(self):
        print(self.brand)

class samsung(smartphone):
    def model(self):
        print(self.brand)

class apple(smartphone):
    def model(self):
        print(self.brand)

objx=smartphone('test brands')
#methods overloading-compile time
objx.msg(2020)
objx.msg(2021,10)

#methods overridding-run time
obj=apple('nokia x')
obj.model()

#methods overridding
obj1=nokia('samsung x')
obj1.model()

obj2=samsung('apple x')
obj2.model()
