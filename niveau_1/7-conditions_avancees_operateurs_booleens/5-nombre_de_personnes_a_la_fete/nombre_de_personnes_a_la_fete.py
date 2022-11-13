max=0
actualNumber=0
nbPerson=int(input())

for loop in range(nbPerson*2):
  personNumber=int(input())
  if personNumber>0:
    actualNumber=actualNumber+1
  else: 
    actualNumber=actualNumber-1
  if actualNumber>max:
     max=actualNumber  
print(max)