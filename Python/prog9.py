# -*- coding: utf-8 -*-

print("Salut ! ")
trouve=0
while(trouve==0):
	motdepasse = input("tape le mot de passe ! ")
	if motdepasse == "secret" :
		print("gagné !!!!!")
		trouve=1
	else : 
		print("perdu !!!!!")
	
