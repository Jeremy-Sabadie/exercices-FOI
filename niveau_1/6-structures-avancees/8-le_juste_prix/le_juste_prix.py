nbMarchands=int(input("nb de marchand:"))
prixMax=1000000
prixMin=1
positonMarchand=1

for a in range(1,nbMarchands+1):
  prix=int(input("votre prix"))
  if prix<prixMin:
    prixMin=prix
    position=a
print(a)
//////////////////////////////////////////////////
nbMarchands=int(input("nb de marchand:"))
pmaxPrice=1000000
minPrice=1
bestPrice=0
positonMarchand=1
///////////////////////////////////////////////////
nbMarchands=int(input("nb de marchand:"))
prixMax=1000000
bestPrice=1
positonMarchand=1

for a in range(1,nbMarchands+1):
  prix=int(input("votre prix"))
  if prix>bestPrice:
    prixMin=prix
    position=a
  elif prix<bestPrice and position>a:
    bestPrice=prix
    position=a
print(a)

for a in range(1,nbMarchands+1):
  price=int(input("votre prix"))
  if price<bestPrice:
    bestPrice=price
    positonMarchand =a
  elif price==bestPrice:
    positonMarchand=a
print(positonMarchand)