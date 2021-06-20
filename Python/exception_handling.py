#exceptions handling-while running instructions,one event which disrupts normal execution flow
    #zerodivision error
    #value error
    #attribute error
    #keyboardinterrupt error
    #IOerror
    #indentation error
    #name error

#defualt exceptions

try:
    try:
        div=10/0
    finally:
        print('divide operation completed')
except:
    print('zero division error')
else:
    print('no exception')


#manual exceptions throw

class invalidRange(RuntimeError):
    def __init__(self,msg):
            print(msg)   
          
try:
     raise invalidRange('network error')
except invalidRange:
    print('invalid msg')
      
