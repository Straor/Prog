# -*- coding: utf-8 -*-
#programme pendu

mot="bonjour"
compteur=0
taille=len(mot)
partiefinie=False
chance=10
motadeviner="_______"
while(not partiefinie):
	print("tape une lettre : ")
	proposition=input()
	while(compteur!=taille):
		if(proposition==mot[compteur]):
			motadeviner[compteur]=proposition
			print(motadeviner)
		compteur=compteur+1	
	chance=chance-1
	print(chance)
	if(chance==0):
		partiefinie=True
		print("tu as perdu")

