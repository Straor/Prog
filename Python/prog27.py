# -*- coding: utf-8 -*-
#programme pendu

mot="bonjour"
compteur=0
taille=len(mot)
partiefinie=False
chance=10
motadeviner="_______"
nombredelettresmanquantes=taille

while(not partiefinie):
	print(motadeviner)
	print("tape une lettre : ")
	proposition=input()
	trouverlettre=False
	while(compteur!=taille):
		if(proposition==mot[compteur]):
			motadeviner=motadeviner[0:compteur]+proposition+motadeviner[compteur+1:]
			nombredelettresmanquantes=nombredelettresmanquantes-1
			trouverlettre=True
		compteur=compteur+1
	compteur=0
	if(not trouverlettre):
		chance=chance-1
	if(trouverlettre):
		print('bravo tu as trouvé, continu !')
	if(nombredelettresmanquantes==0):
		partiefinie=True
		print('tu as gagné')
	print('il te reste ',chance,'chance(s)')
	if(chance==0):
		partiefinie=True
		print("tu as perdu")
	
