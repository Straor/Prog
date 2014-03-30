# -*- coding: utf-8 -*-
# programme morpion
#premiere etape affichage de la grille
#etape deux remplissage de la grille
#etape trois l'ordinateur remplie la grille
#etape quatre detecter la fin de la partie



A1=' '
A2=' '
A3=' '
B1=' '
B2=' '
B3=' '
C1=' '
C2=' '
C3=' '


dico = {}
dico['A1'] =' '
dico['A2'] =' '
dico['A3'] =' '
dico['B1'] =' '
dico['B2'] =' '
dico['B3'] =' '
dico['C1'] =' '
dico['C2'] =' '
dico['C3'] =' '

def affichage(dico):
	print("|", dico['A1'] ,"|", dico['A2'] ,"|", dico['A3'] ,"|")
	print("-------------")
	print("|", dico['B1'] ,"|", dico['B2'] ,"|", dico['B3'] ,"|")
	print("-------------")
	print("|", dico['C1'] ,"|", dico['C2'] ,"|", dico['C3'] ,"|")


partiepasfinie=5
joueur1=True

partiepasfinie=True
affichage(dico)
while(partiepasfinie>0):
	if(joueur1==True):
		joueur="Joueur 1 "
		signe='x'
		
	else :
		joueur='Joueur 2 '
		signe='o'
		
	case=input(joueur + 'tu veux mettre ta ' + signe +' dans quelle case ?')	

	if(dico[case]!=' '):
		print('tu vois pas que la case est deja occupée ????')
	else: 		
		dico[case]=signe
	affichage(dico)
	joueur1= not joueur1
if(joueur==False):
		affichage(dico)
		

print('égalité !!!!')



