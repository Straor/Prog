# -*- coding: utf-8 -*-
# ce programme affiche la table de multiplication choisie avec une boucle et jusqu'à un nombre choisi.
chaine = input("quelle table veux-tu ? ")
nombre = int(chaine)
chaine = input("jusqu'à combien ? ")
maxi = int(chaine)
fois=0
while(fois<=maxi):
	print(fois,"x",nombre,"=",fois*nombre)
	fois=fois+1

