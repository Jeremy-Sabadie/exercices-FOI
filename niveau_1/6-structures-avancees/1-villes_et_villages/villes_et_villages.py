count=1
NbLieux=int(input(combien de lieux?))
for loop in range(NbLieux):
  people=int(input("CbPersone?"))
  if people>10000:
    count= count+1
print(count-1)