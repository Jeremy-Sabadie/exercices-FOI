actualPosition=int(input())
NbVillages=int(input())
count=-1
for loop in range(NbVillages):
  positionVillage=int(input())
  if actualPosition-positionVillage<=50:
    count=count+1
print(count)