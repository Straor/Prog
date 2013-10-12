# -*- coding: utf-8 -*-
# ce programme affiche la table de multiplication choisie avec une boucle.
chaine = input("quelle table veux-tu ? ")
nombre = int(chaine)
fois=0
while(fois<=10):
	print(fois,"x",nombre,"=",fois*nombre)
	fois=fois+1

