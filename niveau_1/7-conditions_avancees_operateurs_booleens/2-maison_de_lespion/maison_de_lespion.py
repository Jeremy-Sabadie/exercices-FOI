absMini=int(input())
absMax=int(input())
ordoMini=int(input())
ordoMax=int(input())
nbHousses=int(input())
count=0
for loop in range(nbHousses):
  abs=int(input())
  if abs>= absMini or abs<=absMax:
    abs=True
  ordo=int(input())
  if ordo>=ordoMini or ordo<=ordoMax:
    ordo=True
  if abs==True and ordo==True:
    count=count+1
print(count)