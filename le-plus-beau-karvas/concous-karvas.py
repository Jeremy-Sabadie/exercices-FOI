NbKarvas=int(input("entrez le nombre de karvas du concours:"))
for loop in range(NbKarvas):
  Weight=int(input("entrez le poids de votre karva:"))
  Age=int(input("entrez l'age de votre karva:"))
  HornsLength=int(input("entrez la longueur de cornes de votre karva:"))
  Heigth=int(input("donnez la hauteur au garrot de votre karvas:"))
  Note=(HornsLength*Heigth)+Weight
  print(Note)