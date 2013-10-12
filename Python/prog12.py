# -*- coding: utf-8 -*-
# programme qui convertis en dollar une somme en euro choisie en demandant le taux de change
chaine = input("donne un euro pour que je te le convertisse en dollar : ")
euro = int(chaine)
chaine2 = input("donne moi le taux de change : ")
tauxdechange=float(chaine2)
dollar=tauxdechange*euro
print(euro,"euro(s) = ",dollar," dollar(s)")


