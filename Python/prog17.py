# -*- coding: utf-8 -*-
# programme qui inverse une chaine de caractères
mot=input("quel mot avez vous choisi ? ")
inverse=""
nombrecaractere=len(mot)
compteur=-1
while(compteur>=nombrecaractere*(-1)):
	inverse=inverse+mot[compteur]
	compteur=compteur-1
print("l'inverse de", mot,"est",inverse)
