
#hybrid inheritance

class grandpa:
    def __init__(self):
        self.name1='grdpa.raja'

class father(grandpa):
    def __init__(self):
        #invoking class
        grandpa.__init__(self)
        self.name2='fath.ravi'

class grandma:
    def __init__(self):
        self.name3='grdma.rani'

class mother(grandma):
    def __init__(self):
        #invoking class
        grandma.__init__(self)
        self.name4='mom.raji'

class son(father,mother):
    def __init__(self):
        grandpa.__init__(self)
        father.__init__(self)
        grandma.__init__(self)
        mother.__init__(self)
        self.name5='son.rahul'
    def msg(self):
        print(self.name1,self.name2,self.name3,self.name4,self.name5)

#obj for class
obj=son()

#class method call
obj.msg()
