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