# -*- coding: utf-8 -*-
# programme qui convertie un nombre entier de seconde en minutes
chaine = input("donne un nombre de secondes à convertir : ")
seconde = int(chaine)
minute = int(seconde/60)
resteseconde = seconde%60
heure = int(minute/60)
resteminute = minute%60
jour= int(heure/24)
resteheure = heure%24
annee= int(jour/365)
restejour= jour%365
print("voici le resultat",annee ,"an(s) et ", restejour , "jour(s) et " ,resteheure ,"heure(s) et" ,resteminute ,"minute(s) et " , resteseconde,"seconde(s)")


