#inheritance-one class can access another class data variables and methods using derived it/invoking it.
#types
    #multiple inheritance
    #multilevel inheritance
    #hybrid inheritance

class base_class:
    def __init__(self,name):
        self.name=name
    def msg(self):
        print(self.name)
    

class derive_class(base_class):
        def display(self):
            self.msg()

#obj for base class
obj=base_class('base class')
obj.msg()

#obj for derived class
obj=derive_class('derive class')
obj.display()





