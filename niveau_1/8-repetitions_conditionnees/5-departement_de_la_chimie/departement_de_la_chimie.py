"""pas encore bon:
totalExp=int(input())
tempMin=int(input())
tempMax=int(input())
relevé=0
alert=False
count=1
while alert==False and count<=totalExp :
  relevé=int(input())
  if relevé<=tempMax and relevé>=tempMin:
    print("Rien à signaler")
    count=count+1
  elif relevé>tempMax or relevé<tempMin:
    alert==True
    print("Alerte !!")