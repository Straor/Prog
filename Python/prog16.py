# -*- coding: utf-8 -*-
# programme qui détermine si une chaine contient ou non un caractère choisi
caractere=input("quel caractere avez vous choisi ? ")
phrase=input("quelle est votre phrase à analyser ? ")
compteur=0
nombrecaracteretrouve=0
fini=0
while(fini==0):
	if(phrase[compteur]==caractere):
		nombrecaracteretrouve=nombrecaracteretrouve+1
	compteur =compteur+1
	if(len(phrase)==compteur):
		fini=1
print("votre phrase contient",nombrecaracteretrouve,caractere)

