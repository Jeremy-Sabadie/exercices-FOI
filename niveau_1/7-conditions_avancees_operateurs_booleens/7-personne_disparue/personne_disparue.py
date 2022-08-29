search=int(input())
tailleListe= int(input())
for loop in range(tailleListe):
  num=int(input())
  if num==search:
    search=True
if search==True:
  print("Sorti de la ville")
else: print("Encore dans la ville")
"""
search=int(input(""))
tailleList= int(input(""))
list=[]
for loop in range(tailleList):
  numberOfList=int(input(""))
  list.append(numberOfList)
if numberOfList in list:
  print("Encore dans la ville")
else: print("Sorti de la ville")