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
  condition=(asbsMin1>asbsMin2) and (ordoMin1>ordoMin2) or (asbsMin2<asbsMin1)    and (ordoMin2<ordoMin1)
  if condition:
    print("OUI")
  else: print("NON")