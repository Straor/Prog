# -*- coding: utf-8 -*-
# programme qui demande les trois longueurs d'un triangle et qui donne ses spécificités
# avoir une phrase quand on tape un caractere à la place d'un chiffre
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
impossible=False
#plus grand coté...
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
#impossible
if(hypotenuse>=autrecote1+autrecote2):
	impossible=True
#rectangle	
if(not impossible and hypotenuse**2==autrecote1**2+autrecote2**2):
	rectangle=True
#équilateral
if(not impossible and a==b and b==c):
	equilateral=True
#isocele
if(not impossible and (a==b or a==c or b==c) and not equilateral):
	isocele=True
#quelconque
if(not impossible and not equilateral and not isocele and not rectangle):
	quelconque=True
print("equilateral : ",equilateral)
print("isocele : ",isocele)
print("rectangle : ",rectangle)
print("quelconque : ",quelconque)
print("impossible : ",impossible)
