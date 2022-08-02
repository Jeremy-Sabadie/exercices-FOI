nbMarchands=int(input())
prixMax=1000000
bestPrice=1
positonMarchand=1

for a in range(1,nbMarchands+1):
  prix=int(input())
  if prix<bestPrice:
    bestPrice=prix
    positonMarchand =a
  elif prix>bestPrice and a>positonMarchand :
    positonMarchand =a
print(positonMarchand)