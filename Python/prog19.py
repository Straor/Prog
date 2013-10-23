# -*- coding: utf-8 -*-
# programme qui demande les trois longueurs d'un triangle et qui donne ses spécificités
chaine=input("quelle est la longueur du premier côté ? ")
a=int(chaine)
chaine=input("quelle est la longueur du deuxième côté ? ")
b=int(chaine)
chaine=input("quelle est la longueur du troisième côté ? ")
c=int(chaine)
equilateral=False
isocele=False
rectangle=False
quelconque=False
if(a==b and b==c):
	print("abc est un triangle équilatéral")
	equilateral=True
if(a==b or a==c or b==c and not equilateral):
	print("abc est un triangle isocèle")


