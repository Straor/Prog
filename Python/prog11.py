# -*- coding: utf-8 -*-
# programme qui affiche une table d convertion d'euro en dollar
euro=1
dollar=1.65
tauxdechange=1.65
while(euro<=16384):
	print(euro,"euro(s) = ",dollar," dollar(s)")
	euro=euro*2
	dollar=tauxdechange*euro
