from statistics import*
totalExp=int(input())
tempMin=int(input())
tempMax=int(input())
tab=[tempMax,tempMin]
moy =mean(tab)
relevé=moy
count=0


countExp=0
while moy<=tempMax and moy>=tempMin and countExp<totalExp:
  relevé=int(input())
  countExp=countExp+1
  if relevé<=tempMax and relevé>=tempMin:
    print("Rien à signaler")
    count=count+1
  elif (relevé>tempMax) or (relevé<tempMin):
    print("Alerte !!")
    break