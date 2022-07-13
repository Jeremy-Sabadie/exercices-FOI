nbMembres=int(input())
equipe1=0
equipe2=0
player=1

for loop in range(nbMembres):
  poidsDuJoueur=int(input())
  player=player+1
  if (player%2)==0:
    equipe1=equipe1+poidsDuJoueur
  else:
   equipe2=equipe2+poidsDuJoueur
  poidsDuJoueur=int(input())
  player=player+1
  if (player%2)==0:
    equipe1=equipe1+poidsDuJoueur
  else:
   equipe2=equipe2+poidsDuJoueur
if equipe1>equipe2:
  print("L'équipe 1 a un avantage")
  print("Poids total pour l'équipe 1 : "+str(equipe1))
  print("Poids total pour l'équipe 2 :  "+str(equipe2))
elif equipe2>equipe1:
  print("L'équipe 2 a un avantage")
  print("Poids total pour l'équipe 1 : "+str(equipe1))
  print("Poids total pour l'équipe 2 : "+str(equipe2))
  """////////////////////////////////////
  vérifier si pair ou impair:
  pair=int(input())


if (pair%2)==1:
  print("impair")
else:
  print("pair")
  ////////////////////////////////////////////
