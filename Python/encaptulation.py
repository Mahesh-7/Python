#encaptulation-consist data variable and methods which hide to outside (data hiding)

#acess specifier 
class PrivateDemo:
    def __init__(self):
        self.nonprivateinstance = "I'm not a private instance"
        self.__privateinstance = "I'm private instance"
    def display_privateinstance(self):
        #print(f"{self.__privateinstance} used within the method of a class")
        print(self.__privateinstance,"used within the method of a class")
    def get_privatedata(self):
        return self.__privateinstance

#class methods call
demo = PrivateDemo()
print(demo.display_privateinstance())
print(demo.nonprivateinstance)
#print(demo.__privateinstance)

#getting private data using get method
print(demo.get_privatedata())





