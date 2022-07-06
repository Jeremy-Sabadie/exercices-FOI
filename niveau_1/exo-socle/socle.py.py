GroundLarge=int(input())
topSurfaceLarge=int(input())
NbBlocs=0
while GroundLarge>=topSurfaceLarge:
  NbBlocs=NbBlocs+(GroundLarge*GroundLarge)
  GroundLarge=GroundLarge-1
print(NbBlocs)