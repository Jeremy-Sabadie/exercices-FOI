date_1=int(input())
date_2=int(input())
count=0
nbEntrées=int(input())
for a in range(nbEntrées):
  enter=int(input())
  if enter>=date_1 and enter<=date_2:
    count= count+1
print(count)