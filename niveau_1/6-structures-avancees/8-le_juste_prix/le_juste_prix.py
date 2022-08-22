nbMarchands= int(input())
position=1
bestPrice=1000000
if nbMarchands<=1000000:
  for a in range(position,nbMarchands+1):
    prix=int(input())
    if prix<bestPrice and prix<1000000:
      bestPrice=prix
      position=a
    if prix<=bestPrice and a>position:
      bestPrice=prix
      position=a
      
  print(position)
  ///Version pimpée:
  nbMarchands= int(input())
position=1
bestPrice=1000000
if nbMarchands<=1000000:
  for a in range(position,nbMarchands+1):
    prix=int(input())
    if prix<bestPrice and prix<1000000:
      bestPrice=prix
      position=a
    if prix<=bestPrice and a>position:
      bestPrice=prix
      position=a
  print("le meilleur prix est: "+str(bestPrice))
  print("et c'est le vendeur en position n°: "+str(position))