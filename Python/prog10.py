# -*- coding: utf-8 -*-
#programme qui fait deviner un nombre entre 1 et 100
#amélioration à faire : vérifier la saisie de chaine
import random
print("Salut ! ")
print("j'ai choisi un nombre trouves le !")
nombrechoisi=random.randint(1,100)
gagne=False
coups=0
while(gagne==False):
	essai=int(input("vas y tapes ton nombre ! \n"))
	if(essai>nombrechoisi):
		print("trop grand")
		coups=coups+1
	if(essai<nombrechoisi):
		print("trop petit")
		coups=coups+1
	if(essai==nombrechoisi):
		print("tu as trouvé en ", coups, "coups")
		gagne=True
if(coups>10):
	reponse="tu es vraiment nul tete de noeuds"
if(coups<5):
	reponse="tu es un genie"
if (coups>=5 and coups<=10):
	reponse="tu peux mieux faire"
print(reponse)

