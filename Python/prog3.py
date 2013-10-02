# -*- coding: utf-8 -*-
# ce programme calcule les coordonées du milieuu d'un segment
print("Salut ! ")
sxA = input("tape l'abscisse du point A ! ")
syA = input("tape l'ordonnée du point A ! ")
sxB = input("tape l'abscisse du point B ! ")
syB = input("tape l'ordonnée du point B ! ")
xA = int(sxA)
yA = int(syA)
xB = int(sxB)
yB = int(syB)
xM = (xA + xB)/2
yM = (yA + yB)/2
sxM = str(xM)
print("l'abscice du milieu est " + sxM)
print("l'ordonnée du milieu est " , yM)
