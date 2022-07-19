actualPosition=int(input())
NbVillages=int(input())

count=0
for loop in range(NbVillages):
  positionVillage=int(input())
  difference=positionVillage-actualPosition
  if difference<=50 and abs(difference)<=50:
    count=count+1
print(count)