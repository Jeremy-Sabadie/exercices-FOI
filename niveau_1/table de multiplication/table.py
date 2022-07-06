multiplié=int(1)#doit aller de 1 jusqu'à 10
multiplicateur=int(1)#doit aller de 1 jusqu'à 20
result= multiplié*multiplicateur
for multiplié in range(1,21):
  for multiplicateur in range(1,21):
    print(multiplié*multiplicateur,end=" ")
  multiplié=multiplié+1
  print("\n")