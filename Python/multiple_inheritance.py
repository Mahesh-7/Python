
#multiple inheritance

class base_class1:
    def __init__(self):
        self.name1='base1'
        print('base class1')

class base_class2:
    def __init__(self):
        self.name2='base2'
        print('base class2')

class derive_class(base_class1,base_class2):
    def __init__(self):
        #invoking base class
        base_class1.__init__(self)
        base_class2.__init__(self)
    def msg(self):
        print('derived class')
        print(self.name1,self.name2)

#obj for derived class
obj=derive_class()

#derived class method call
obj.msg()
