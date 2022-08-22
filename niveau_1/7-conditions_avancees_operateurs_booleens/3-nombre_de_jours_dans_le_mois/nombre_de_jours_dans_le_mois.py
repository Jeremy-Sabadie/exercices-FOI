month=int(input())
if month<4 or month>=7 and month<=9:
  print("30")
elif month==11:
  print("29")
else: 
  print("31")