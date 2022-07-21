age=int(input())
pound=int(input())
price=0

if age==60:
  print(price)
elif age<10:
  print(price+5)
else: 
  if pound<20:
    print(price+30)
  else:
    print(price+30+10)