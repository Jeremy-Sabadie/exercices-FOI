nbPersonne=int(input())
count=0
for loop in range(nbPersonne):
  count=0
  sizeCm=int(input())
  if sizeCm>=178 and sizeCm<=182:
    count=count+1
  
  age=int(input())
  if age>=34:
    count=count+1
  
  weight=int(input())
  if weight<70:
    count=count+1
  
  horse=int(input())
  if horse==0:
    count=count+1
  
  brownHair=int(input())
  if brownHair==1:
    count=count+1
  
  if count==5:
    print("Très probable")
  elif count==3 or count==4:
    print("Probable")
  elif count==0:
    print("Impossible")
  else:
    print("Peu probable")