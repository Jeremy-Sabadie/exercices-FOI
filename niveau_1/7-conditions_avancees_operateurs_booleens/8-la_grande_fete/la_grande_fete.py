suspect=0
start=int(input())
end= int(input())
nbInvites=int(input())
for loop in range(nbInvites):
  
  arrive=int(input())
  depart=int(input())
  condition=(arrive>=start and arrive<=end) or (depart<=end and depart>=start)or (arrive<=start and depart>=end) 
  if condition:
    suspect=suspect+1
print(suspect)