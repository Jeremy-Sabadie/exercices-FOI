Cube=int(17)
totalEtage=Cube**3
totalPyramide=1

while Cube > 1 :
  totalEtage=Cube**3
  totalPyramide=totalEtage+totalPyramide
  Cube=Cube-2
  
print(totalPyramide)