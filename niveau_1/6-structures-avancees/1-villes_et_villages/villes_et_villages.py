count=1
NbLieux=int(input())
for loop in range(NbLieux):
  people=int(input())
  if people>10000:
    count= count+1
print(count-1)