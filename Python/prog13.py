# -*- coding: utf-8 -*-
# programme qui demande un nombre et affiche les 10 triples successifs
chaine = input("donne un nombre : ")
nombre = int(chaine)
triple = nombre
compteur=1
while(compteur<=10):
	triple=triple*3
	print(triple)
	compteur=compteur+1

