suspect=0
start=int(input())
end= int(input())
nbInvites=int(input())
for loop in range(nbInvites):
  
  arrive=int(input())
  depart=int(input())
  condition=(arrive>=start and arrive<=end) or (depart<=end and depart>=start)or (arrive<=start and depart>=end) 
  if condition:
<<<<<<< HEAD
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
=======
    suspect=suspect+1
print(suspect)
>>>>>>> 4187761a6716a324bdb416b29bdd3a8494f32aec
