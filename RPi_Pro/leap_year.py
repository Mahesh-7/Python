num = int(input('enter year:'))
   
if(num%4 == 0 ):
  if(num%100 ==0):
      print('not a leap year')
  else:
      print('leap year')
elif(num%400==0):
    print('leap year')
else:
    print('not valid year')

