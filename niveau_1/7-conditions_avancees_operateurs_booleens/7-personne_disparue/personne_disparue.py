search=int(input())
tailleListe= int(input())
for loop in range(tailleListe):
  num=int(input())
  if num==search:
    search=True
if search==True:
  print("Sorti de la ville")
else: print("Encore dans la ville")