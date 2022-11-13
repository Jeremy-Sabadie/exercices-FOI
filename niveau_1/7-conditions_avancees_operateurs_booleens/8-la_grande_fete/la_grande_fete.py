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
"""zzphyr
start=int(input())
end=int(input())
guest=int(input())
spy=0
for a in range(guest):
    arr=int(input())
    dep=int(input())
    susp = (arr>=start and arr<=end) or (dep<=end and dep>=start) or (arr <= start and dep >= end)
    if susp:
        spy=spy+1