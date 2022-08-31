number=int(input())
proposition=0
answer=0

while answer!=number:
  answer=int(input())
  if answer<number:
    print("c'est plus")
    proposition=proposition+1
  elif answer>number:
    print("c'est moins")
    proposition=proposition+1
  else:
    proposition=proposition+1
    proposition=str(proposition)
print("Nombre d'essais nécessaires :   \n"  +proposition)