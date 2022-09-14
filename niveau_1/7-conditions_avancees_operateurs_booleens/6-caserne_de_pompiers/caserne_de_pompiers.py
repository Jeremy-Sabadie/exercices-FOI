"""a modifier pour valider :
nbPaire=int(input())
for loop in range(nbPaire):
  asbsMin1=int(input())
  absMax1=int(input())
  ordoMin1=int(input())
  ordoMax1=int(input())
  asbsMin2=int(input())
  absMax2=int(input())
  ordoMin2=int(input())
  ordoMax2=int(input())
  condition=((absMax1>asbsMin2) and (ordoMax1>ordoMin2)) or((ordoMax2<ordoMin1 and absMax2<ordoMin1))    
  if condition:
    print("OUI")
  elif   condition!=True:
    print("NON")