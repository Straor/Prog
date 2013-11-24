# -*- coding: utf-8 -*-
#programme qui affiche les cent premiers nombres pairs
print("on affiche les cents premiers nombres pairs")
nombres=1
compteur=1
while((compteur<=100)):
	if(nombres%2==0):
		print(nombres)
		compteur=compteur+1
	nombres=nombres+1
print("voilà")
