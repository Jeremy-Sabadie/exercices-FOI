Les enfants du village sont très intrigués par votre langue si différente de la leur, à tel point qu'ils insistent pour que vous leur donniez des cours. Vous commencez par leur apprendre à réciter l'alphabet, puis comme ils s'intéressent aussi à l'écriture, vous décidez de leur apprendre à écrire les trois premières lettres : a, b et c.

Pour les y aider, vous souhaitez imprimer des pages d'écriture. Les élèves devront y recopier chaque lettre qui s'y trouve dans un emplacement prévu juste à côté de cette lettre.

Ce que doit faire votre programme :
Votre programme doit écrire 3 lignes, chacune contenant plusieurs fois de suite une lettre suivie du caractère « _ » (underscore en anglais) : la lettre « a » sur la première ligne, la lettre « b » sur la deuxième et la lettre « c » sur la troisième.

Vous disposez déjà d'un modèle où chaque ligne contient 4 lettres :

↳
a_a_a_a_ 
b_b_b_b_
c_c_c_c_
Cependant, vous vous dites qu'il serait mieux de mettre 30 lettres par ligne. Écrivez un programme qui étend votre modèle. Bien sûr, vous utiliserez une boucle pour ne pas vous fatiguer à écrire vous-même 30 fois chaque lettre.



Afficher du texte sans retour à la ligne
L'instruction ci-dessous :

print("Bonjour")
effectue en fait deux choses distinctes :

premièrement, afficher le mot « Bonjour » ;
deuxièmement, passer à la ligne suivante ou, autrement dit, effectuer un retour à la ligne.
Nous pourrions l'écrire comme ceci en pseudo-code :

Afficher "Bonjour" (sans retour à la ligne)
Aller à la ligne
Bien qu'il soit généralement pratique d'afficher du texte et de terminer la ligne en une seule commande, on peut vouloir effectuer l'une des deux actions indépendamment de l'autre. Pour afficher le mot « Bonjour » sans revenir à la ligne, on utilise la commande suivante :

print("Bonjour", end = "")
Le texte qui suit le « Bonjour » est une option qui permet de dire que l'on ne veut rien ajouter après « Bonjour ».

Voyons ce qui se passe si on écrit un programme contenant deux fois cette instruction :

print("Bonjour", end = "")
print("Bonjour", end = "")
↳
BonjourBonjour
On a donc deux « Bonjour » collés.

À l'inverse, comment aller à la ligne sans rien afficher du tout ? Pour cela, il suffit simplement d'utiliser l'instruction print en lui disant d'afficher un texte vide :

print("")
En fait, on peut même ne pas fournir le texte vide. Voici un programme d'exemple le démontrant :

print("Un ", end = "")
print("deux ", end = "")
print("trois", end = "")
print()
print("Soleil !")
↳
Un deux trois
Soleil !