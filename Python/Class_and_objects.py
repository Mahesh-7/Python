#class is consist object/variable/attributes and methods/functions/behaviour in single unit

#class definition
class person:
    a='test variable'
    def printAge(self):
        print(self.a)
    def display(self,msg):
        print(msg,self.a)
    print(a)

#class call
person()
print(type(person))
print(person.a)

#class variables and methods access
obj=person()#class assign to obj variable
obj.printAge()
obj.display('hello')





