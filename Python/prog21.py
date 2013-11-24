# -*- coding: utf-8 -*-
#trouver les longueures d'un triangle rectangle et isocele
chaine=input("longueure entiere du plus grand coté ")
longueurduplusgrandcote=int(chaine)
autrescotes=longueurduplusgrandcote/2+1
while(longueurduplusgrandcote**2!=(autrescotes**2)*2):
	autrescotes=autrescotes+1
	if(autrescotes>=longueurduplusgrandcote):
		longueurduplusgrandcote=longueurduplusgrandcote+1
		autrescotes=longueurduplusgrandcote/2+1
print("le triangle ayant pour coté",longueurduplusgrandcote , autrescotes , autrescotes , "est un triangle rectangle")

