num = int(input('enter mark:'))
   
if(num>=35):
      print('pass')
elif(num<35):
    num=35-num
    if(num<=3):
     print('pass,',num,'marks provided as grace mark')
    else:
        print('fail,not eligible for grace mark')
