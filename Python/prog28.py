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
def affichage(A1, A2, A3, B1, B2, B3, C1, C2, C3):
	print("|", A1 ,"|", A2 ,"|", A3, "|")
	print("-------------")
	print("|", B1 ,"|", B2 ,"|", B3 ,"|")
	print("-------------")
	print("|", C1 ,"|" ,C2 ,"|", C3 ,"|")

nombredetourajouer=5

affichage(A1, A2, A3, B1, B2, B3, C1, C2, C3)
while(nombredetourajouer>0):
	if(A1==A2==A3 or B1==B2==B3 or C1==C2==C3 or A1==B2==C3 or A3==B2==C1
	or A1==B1==C1 or A2==B2==C2 or A3==B3==C3):
		print('bravo !!!')
		
	case=input('joueur 1 tu veux mettre ta croix dans quelle case ?')
	if(case=='A1'):
		A1='x'
	if(case=='A2'):
		A2='x'
	if(case=='A3'):
		A3='x'
	if(case=='B1'):
		B1='x'
	if(case=='B2'):
		B2='x'
	if(case=='B3'):
		B3='x'
	if(case=='C1'):
		C1='x'
	if(case=='C2'):
		C2='x'
	if(case=='C3'):
		C3='x'
	affichage(A1, A2, A3, B1, B2, B3, C1, C2, C3)

	case=input('joueur 2 tu veux mettre ton rond dans quelle case ?')
	if(case=='A1'):
		A1='o'
	if(case=='A2'):
		A2='o'
	if(case=='A3'):
		A3='o'
	if(case=='B1'):
		B1='o'
	if(case=='B2'):
		B2='o'
	if(case=='B3'):
		B3='o'
	if(case=='C1'):
		C1='o'
	if(case=='C2'):
		C2='o'
	if(case=='C3'):
		C3='o'
	affichage(A1, A2, A3, B1, B2, B3, C1, C2, C3)
	nombredetourajouer=nombredetourajouer-1
print('égalité !!!!')
