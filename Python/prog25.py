# -*- coding: utf-8 -*-
#programme pour apprendre les fonctions

from turtle import *
def triangle(cote,epaisseur,couleur):
	compteur=1
	width(epaisseur)
	color(couleur)
	while(compteur <= 3):
		compteur=compteur+1
		forward(cote)
		left(120)
def carre(cote,epaisseur,couleur):
	compteur=1
	width(epaisseur)
	color(couleur)
	while(compteur <= 4):
		compteur=compteur+1
		forward(cote)
		left(90)

compteur=1
toutfini=False
cote=50
epaisseur=5
ordonnee=0
couleur='black'
abscisse=-200
reset()	
up()
goto(abscisse,ordonnee)
while(compteur<=3):	
	down()
	triangle(cote,epaisseur,couleur)
	up()
	forward(cote+epaisseur+1)
	down()
	carre(cote,epaisseur,couleur)
	up()
	forward(cote+epaisseur+1)
	cote=cote+10
	epaisseur=epaisseur+1
	compteur=compteur+1	




a = input()
