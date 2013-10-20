# -*- coding: utf-8 -*-
# programme qui convertit un nombre d'années d'heures et de minutes en secondes
chaineannee= input("donne un nombre d'années ")
annee=int(chaineannee)
chainejour= input("donne un nombre de jours ")
jour=int(chainejour)
chaineheure= input("donne un nombre d'heures ")
heure=int(chaineheure)
chaineminute= input("donne un nombre de minutes ")
minute=int(chaineminute)
seconde=(minute*60)+(heure*60*60)+(jour*24*60*60)+(annee*365*24*60*60)
print("voici le nombre de secondes",seconde ,"!")

