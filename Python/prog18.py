# -*- coding: utf-8 -*-
# programme qui vérifie si le mot est un palindrome
mot=input("quel mot avez vous choisi ? ")
inverse=""
nombrecaractere=len(mot)
compteur=-1
while(compteur>=nombrecaractere*(-1)):
	inverse=inverse+mot[compteur]
	compteur=compteur-1
print("l'inverse de", mot,"est",inverse)
if(inverse==mot):
	print("c'est un palindrome")
else:
	print("ce n'est pas un palindrome !")

