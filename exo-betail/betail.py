NbOfFarmer=3


for loop in range(NbOfFarmer):
  FarmerNb=int(input("entrez votre nombre de karvas:"))
  FarmerNb+=FarmerNb
  FarmerNb=str(FarmerNb)
print("le nombre total de karvas est de "+FarmerNb)
#deuxième essaie aprés réflexion ///////////////////////////////////////////////////=>
total_number_of_karvas : int = 0

for i in range(2):
  total_number_of_karvas += int(input(f"Fermier {i + 1}, veuillez entrer votre nombre de karvas: "))
print(f"Le nombre total de Karvas est de : {total_number_of_karvas}")