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


partiepasfinie=True
joueur1=True

partiepasfinie=True
affichage(dico)
while(partiepasfinie==True):
	if(joueur1==True):
		joueur="Joueur 1 "
		signe='x'
	else :
		joueur='Joueur 2 '
		signe='o'
		
	case=input(joueur + 'tu veux mettre ' + signe +' dans quelle case ? ')	
	while(case!='A1' and case!='A2' and case!='A3' and case!='B1' and case!='B2' and case!='B3' and case!='C1' and case!='C2' and case!='C3'):
		print('apprend à taper sur un clavier')
		case=input(joueur + 'tu veux mettre ' + signe +' dans quelle case ? ')
		if(case=='A1'or case=='A2'or case=='A3'or case=='B1'or case=='B2'or case=='B3'or case=='C1'or case=='C2'or case=='C3'):
			print('bravo tu es moins bète que ce que je pensais')
			
	if(dico[case]!=' '):
		print('tu vois pas que la case est déjà occupée ???? ')
	else: 		
		dico[case]=signe
	affichage(dico)
	joueur1= not joueur1
	if(dico['A1']==dico['A2']==dico['A3']==signe or dico['B1']==dico['B2']==dico['B3']==signe or dico['C1']==dico['C2']==dico['C3']==signe or dico['A1']==dico['B1']==dico['C1']==signe or dico['A2']==dico['B2']==dico['C2']==signe or dico['A3']==dico['B3']==dico['C3']==signe or dico['A1']==dico['B2']==dico['C3']==signe or dico['A3']==dico['B2']==dico['C1']==signe):
		partiepasfinie=False
		if(signe=='x'):
			print('joueur 1 tu as gagné')
		if(signe=='o'):
			print('joueur 2 tu as gagné')
	if(dico['A1'] and dico['A2'] and dico['A3'] and dico['B1'] and dico['B2'] and dico['B3'] and dico['C1'] and dico['C2'] and dico['C3'] != ' '):
		partiepasfinie=False
		print('match nul !')


		





