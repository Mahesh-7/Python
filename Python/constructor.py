#class is consist object/variable/attributes and methos/functions/behaviour in single unit

#class definition
class person:
    a='test variable'
    #constructor 
    def __init__(self,name):
        self.name=name
        print('this is constructor')
    def printAge(self):
        print(self.a)
    def display(self,msg):
        print(msg,self.name)
    #destructor call
    def __del__(self):
        print('destructor call')


#class call
person('ragul')
print(type(person))
print(person.a)



#class variables and methods access
obj=person('ragul')#class assign to obj variable
obj.printAge()
obj.display('hello')

#destructor
del person





