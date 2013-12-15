# -*- coding: utf-8 -*-
#programme pour apprendre les fonctions

def calcul_distance(vitesse,coefficient):
	resultat = vitesse/3.6 + vitesse**2/254*coefficient
	return resultat

chaine=input("donner la vitesse du véhicule")
vitesse=int(chaine)
dars=calcul_distance(vitesse,0.8)
darm=calcul_distance(vitesse,0.4)

print("votre distance d'arret est de ",dars,"m sur route sèche et de ",darm,"sur route mouillée")
