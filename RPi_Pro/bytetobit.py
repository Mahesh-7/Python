


def char_to_bit(byte_1):
    byte = ord(byte_1)    #convert char to interger  
    bit_list = []         #empty list for holding bit pattern
    item = 0              #to hold a bit during seperation
    
    for i in range(0,8):        #to shift byte 8 times even if the value reached zero, to obtain complete bit pattern 
        item = 1 & byte
        bit_list.append(item)
        byte >>= 1

    return bit_list

def byte_to_bit(byte): 
    bit_list = []         #empty list for holding bit pattern
    item = 0              #to hold a bit during seperation
    
    for i in range(0,8):        #to shift byte 8 times even if the value reached zero, to obtain complete bit pattern 
        item = 1 & byte
        bit_list.append(item)
        byte >>= 1

    return bit_list



name = "ABCD"

h = 0x02

while True:

    output = byte_to_bit(h) 

    print(output)
    
    break










"""    
    for i in name:
        output = byte_to_bit(i) 

        print(output)

    break
"""    


"""
a = 15
bit_list = []
item = 1

for i in range(0,8):
    item = 1 & a
    bit_list.append(item)
    a >>= 1

print(bit_list)
    
"""


    




     




