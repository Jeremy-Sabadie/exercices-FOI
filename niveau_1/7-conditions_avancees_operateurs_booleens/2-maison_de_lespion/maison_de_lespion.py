absMini=int(input())
absMax=int(input())
ordoMini=int(input())
ordoMax=int(input())
nbHousses=int(input())
count=0
for loop in range(nbHousses):
  abs=int(input())
  ordo=int(input())
  condition= (abs>=absMini and abs<=absMax)     and(ordo>=ordoMini and ordo<=ordoMax)
  if condition:
    count=count+1
print(count)