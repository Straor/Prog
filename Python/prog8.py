# -*- coding: utf-8 -*-
# ce programme affiche un nombre de ligne d'étoiles et le nombre d'étoile sur chaque lignes.
chaine = input("combien de lignes veux-tu ? ")
nombre = int(chaine)
etoile ='*'
compteur=0
while(compteur<=nombre/2):
	print(etoile)
	etoile=etoile+'*'
	compteur=compteur+1
compteur=0
while(compteur<=nombre/2):
	print(etoile[:-compteur-1])
	compteur=compteur+1
print("c'est fini !!!! ")

