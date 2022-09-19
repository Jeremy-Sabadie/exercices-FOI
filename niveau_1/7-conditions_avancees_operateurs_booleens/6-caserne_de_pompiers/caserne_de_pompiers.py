nbpair=int(input())
for a in range(nbpair):
    absMin1=int(input())
    absMax1=int(input())
    ordoMin1=int(input())
    ordoMax1=int(input())
    absMin2=int(input())
    absMax2=int(input())
    ordoMin2=int(input())
    ordoMax2=int(input())
    condition=(absMax1 <= absMin2) or (absMax2 <= absMin1) or (ordoMax1 <= ordoMin2) or (ordoMax2 <= ordoMin1)
    if condition:
        print("NON")
    else:
        print("OUI")

    """Pour info:orrection présentée par FIOI apré la validation:

    nbPaires = int(input())
for loop in range(nbPaires):
   xMin1 = int(input())
   xMax1 = int(input())
   yMin1 = int(input())
   yMax1 = int(input())
   xMin2 = int(input())
   xMax2 = int(input())
   yMin2 = int(input())
   yMax2 = int(input())
   if ( (xMax2 <= xMin1) or (xMax1 <= xMin2) ) or ( (yMax2 <= yMin1) or (yMax1 <= yMin2) ):
      print("NON")
   else:
      print("OUI")