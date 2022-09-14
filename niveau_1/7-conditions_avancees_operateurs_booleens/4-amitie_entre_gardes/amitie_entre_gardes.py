garde_1Start=int(input())
garde_1_stop=int(input())
garde_2Start=int(input())
garde_2_stop=int(input())
if (garde_1Start>=garde_2Start) and (garde_1Start<=garde_2_stop):
  print("Amis")
elif  (garde_2Start>=garde_1Start) and (garde_2Start<=garde_1_stop):
  print("Amis")
else:
  print("Pas amis")
  ///////
  garde_1Start=int(input())
garde_1_stop=int(input())
garde_2Start=int(input())
garde_2_stop=int(input())
if (garde_1Start>=garde_2Start) and (garde_1Start<=garde_2_stop)or(garde_1_stop>=garde_2Start and garde_1_stop<=garde_2_stop):
  print("Amis")
elif  (garde_2Start>=garde_1Start) and (garde_2Start<=garde_1_stop)or(garde_2_stop>=garde_1Start and garde_2_stop<=garde_1_stop):
  print("Amis")
else:
  print("Pas amis")


  """presse papier:
    condition=(absMin1>=absMin2) and (absMin1<=absMax2)or(absMax1>=asbsMin2 and absMax1<=absMax2):
  print("OUI")
elif  (ordoMin2>=ordoMin1) and (ordoMin2<=ordoMax1)or(ordoMax2>=ordoMin1 and ordoMax2<=ordoMax1):
  print("NON")