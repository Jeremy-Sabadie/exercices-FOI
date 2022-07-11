de1=int(input())
de2=int(input())
prix= (de1+de2)
if prix>=10:
  print("Taxe spéciale !")
  print(36)
else:
  print("Taxe régulière ")
  print(prix*2)