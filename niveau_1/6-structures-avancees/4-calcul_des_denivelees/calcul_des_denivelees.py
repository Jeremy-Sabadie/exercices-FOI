positiveTrajet=0
negativeTrajet=0
nbMontees=int(input())

for loop in range(nbMontees):
  trajet=int(input())
  if trajet>0:
    positiveTrajet=positiveTrajet+trajet
  else:
    negativeTrajet=negativeTrajet+trajet
print(positiveTrajet)
print (abs(negativeTrajet))