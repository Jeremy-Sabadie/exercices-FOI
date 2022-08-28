partyStart=int(input())
partyEnd=int(input())
nbInvites=int(input())
count=0
for loop in range(nbInvites):
  arive=int(input())
  
    
  depart=int(input())
  condition=(arive>=partyStart and arive<=partyEnd) or(depart>=partyStart and depart<=partyEnd)
  if condition:
    count=count+1
print(count)