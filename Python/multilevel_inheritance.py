
#multilevel inheritance

class grandpa:
    def __init__(self):
        self.name1='raja'

class father(grandpa):
    def __init__(self):
        #invoking class
        grandpa.__init__(self)
        self.name2='ravi'
        
class son(father):
    def __init__(self):
        #invoking class
        father.__init__(self)
        self.name3='ram'
    def msg(self):
        print(self.name1,self.name2,self.name3)

#obj for class
obj=son()

#class method call
obj.msg()
