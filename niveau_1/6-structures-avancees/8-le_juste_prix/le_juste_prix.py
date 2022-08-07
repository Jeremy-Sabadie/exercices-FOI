nbMarchands=int(input())
bestPrice=1000000
positonMarchand=1
for a in range(1,nbMarchands+1):
  prix=int(input())
  if prix<bestPrice:
    bestPrice=prix
    positonMarchand =a
  if prix==bestPrice:
    positonMarchand =a
print(positonMarchand)