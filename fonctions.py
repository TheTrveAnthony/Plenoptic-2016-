# coding: utf-8

import math
import numpy as np
from numpy import array
from numpy import uint8
from numpy import uint64
from PIL import Image
#from tabz import *


"""fonctions servant pour le programme principal."""

from tableaux import *


def taille(tableau):	#fonction renvoyant un entier valant le nombre de lignes et de colonnes de la liste -1
	
	return len(tableau)-1
	
	
	
def l_h(choix):  		#fonction mettant la fenetre à la bonne taille sous le format [largeur, hauteur]
	if choix == 1:
		return [840, 593]
	if choix == 2:
		return [650, 515]
	if choix == 3:
		return [512, 384]
		
		
	
def construire(choix):		#fonction constituant la liste finale  
	if choix == 1:
		return fish		
	elif choix == 2:	
		return hummer
	elif choix == 3:
		return dragon
	else:
		choix = input("erreur, recommencez svp\n")
		construire(choix)
		
		
def Image_Tableau(path):	# convertit une image en tableau
    img= Image.open(path)
    ta=np.array(img)
    taa=np.uint64(ta)
    return(ta)

def Tableau_Image(tab):		# convertit un tableau en image
    ta=np.uint8(tab)
    im=Image.fromarray(ta, mode = "RGB")
    img = im.save("trash/aux.png")	# image enregistrée
    return img
    #im.show()


"""	

def shift_bas(tab, nb): #prend un array et le nb de pixels à shifter en bas
    nbl=np.size(tab, 0)
    nbc = np.size(tab, 1)
    tbl = np.zeros(((nbl, nbc, 3)))
    i=nbl-1
	#print(type(tbl))
	#print(type(tbl[0]))
	#print(type(tbl[0][0]))
	#print(type(tbl[0][0][0]))
    while i>-1:

        if i >= nb:
            tbl[i] = tab[i-nb]
        i=i-1
	tab = tbl
    return (tab)


def shift_haut(tab, nb):
    nbl = np.size(tab, 0)
    nbc = np.size(tab, 1)
    tbl = np.zeros(((nbl, nbc, 3)))
    i = 0

    while i < nbl:

        if i <= nbl-1-nb:
            tab[i]=tab[i+nb]
        i=i+1
    tab = tbl
    return(tab)

def shift_gauche(tab, nb):
    nbl=np.size(tab,0)
    nbc=np.size(tab, 1)
    tbl = np.zeros(((nbl, nbc, 3)))
    i=0
    while i<nbc:
        if i<=nbc-1-nb:
            t=0
            while t<nbl:
                tbl[t][i]=tab[t][i+nb]
                t=t+1
        i=i+1
    tab = tbl
    return(tab)

def shift_droite(tab, nb):
    nbl=len(tab)
    nbc=len(tab[1]) 
    tbl = np.zeros(((nbl, nbc, 3)))
    i=nbc-1
    while i>-1:

        if i>=nb:
            t=0
            while t<nbl:
                tbl[t][i]=tab[t][i-nb]
                t=t+1
        i=i-1
    tab = tbl
    return(tab)

# Fonction qui sert à décaler la matrice selon les fonctions de deplacement avec le coeff de deplacement
def Decalage(tab, u, v, coeff):
	
	
	if u < 0:
		uposi=-u
		tab.sg(tab, uposi*coeff)
		if v < 0:
			vposi = -v
			tab.sh(tabLG, vposi*coeff)
           
		elif v > 0:
			tab.sb(tabLG, v*coeff)
            
        

	elif u>0:
		tab.sd(tab, u*coeff)
		if v < 0:
			vposi = -v
			tab.sh(tabLD, vposi*coeff)
            
		elif v > 0:
			tab.sb(tabLD, v*coeff)
           

#fonction qui décale les images du tableau d'images Tab selon leurs positions et retourne le tableau d'images décalées (à finir)
def Posi_Decalage(Tab, coeff, x, y):
    nbl= Tab.l
    nbc= Tab.c
 
    i=0
    while i<nbl:
        j=0
        while j<nbc:
            print j
            Decalage(Tab, x-i, y-j, coeff)

            j=j+1
        i=i+1
    return 1	
"""

	
