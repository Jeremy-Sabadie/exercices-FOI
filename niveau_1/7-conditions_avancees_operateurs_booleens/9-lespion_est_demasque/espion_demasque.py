count=0
for loop in range(nbPersonne):
  sizeCm=int(input("taille?"))
  if sizeCm>=178 and sizeCm<=182:
    count=count+1
  age=int(input("age?"))
  if age>=34:
    count=count+1
  weight=int(input("poids?"))
  if weight<70:
    count=count+1
  horse=int(input("cheval?"))
  if horse==0:
    count=count+1
  hair=int(input("cheveux?"))
  if hair==1:
    count=count+1
  if count>=5:
    print("Très probable")
  if count==3 or count==4:
    print("Probable")
  if count==0:
    print(" Impossible")
  elif count<3:
    print("Peu probable")