# -*- coding: utf-8 -*-
# programme qui demande les trois longueurs d'un triangle et qui donne ses spécificités
# avoir une phrase quand on tape un caractere à la plasse d'un chiffre
#traiter le cas où un triangle est impossile
chaine=input("quelle est la longueur du premier côté ? ")
a=int(chaine)
chaine=input("quelle est la longueur du deuxième côté ? ")
b=int(chaine)
chaine=input("quelle est la longueur du troisième côté ? ")
c=int(chaine)
equilateral=False
isocele=False
rectangle=False
quelconque=True
if(a==b and b==c):
	print("abc est un triangle équilatéral")
	equilateral=True
if(a==b or a==c or b==c and not equilateral):
	print("abc est un triangle isocèle")
hypotenuse=a
autrecote1=b
autrecote2=c
if(b>hypotenuse):
	hypotenuse=b
	autrecote1=a
	autrecote2=c
if(c>hypotenuse):
	hypotenuse=c
	autrecote1=a
	autrecote2=b
if(hypotenuse**2==autrecote1**2+autrecote2**2):
	rectangle=True
	print("abc est un triangle rectangle")
if(equilateral or isocele or rectangle):
	quelconque=False
if(quelconque):
	print("abc est un triangle quelconque")

