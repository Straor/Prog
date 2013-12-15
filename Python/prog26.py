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
def etoile9(cote,epaisseur,couleur):
	compteur=1
	width(epaisseur)
	color(couleur)
	while(compteur <= 9):
		compteur=compteur+1
		forward(cote)
		left(120)
		forward(cote)
		right(80)
def etoile5(cote,epaisseur,couleur):
	compteur=1
	width(epaisseur)
	color(couleur)
	left(60)
	while(compteur <= 5):
		compteur=compteur+1
		forward(cote)
		right(80)
		forward(cote)
		left(151.5)
		
speed(1)
carre(50,2,'black')
etoile5(50,2,'black')
a = input()
