"""suspect=0
start=int(input())
end= int(input())
nbInvites=int(input())
for loop in range(nbInvites):
  suspect=0
  arrive=int(input())
  depart=int(input())
  condition=(arrive>=start) and (arrive<=end) or (depart<=end) and (depart>=end) or (arrive<=start) and (depart>=end)
  if condition:
    suspect=suspect+1
print(suspect)"""