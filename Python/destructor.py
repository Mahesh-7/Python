#destructor
class Awesome:
    def greetings(self):
        print("Hello World!")
    def __del__(self):
        print("Hello from the __del__ method.")
    
obj = Awesome()
obj.greetings()

#destructor call
del obj
