# coding: utf-8

import numpy as np



class tabz:		# classe pour les décalages sur tableaux
	
	def __init__(self, tab):
		
		self.tab = tab
		self.l = len(tab)
		self.c = len(tab[0])
		
		
	def sb(self, nb): #prend un array et le nb de pixels à shifter en bas

		self.tab = np.roll(self.tab, nb, axis = 0)
		for i in range(0, nb):
			for j in range(0, self.c):
				for k in range(0, 3):
					self.tab[i][j][k] = 0
		


	def sh(self, nb):

		self.tab = np.roll(self.tab, -nb, axis = 0)
		for i in range(self.l-1, self.l-nb-1, -1):
			for j in range(0, self.c):
				for k in range(0, 3):
					self.tab[i][j][k] = 0
    

	def sg(self, nb):

		self.tab = np.roll(self.tab, -nb, axis = 1)
		for i in range(0, self.l):
			for j in range(self.c-1, self.c-nb-1, -1):
				for k in range(0, 3):
					self.tab[i][j][k] = 0
    

	def sd(self, nb):

		self.tab = np.roll(self.tab, nb, axis = 1)
		for i in range(0, self.l):
			for j in range(0, nb):
				for k in range(0, 3):
					self.tab[i][j][k] = 0


	def Decalage(self, u, v, coeff):
	
	
		if u < 0:
			uposi=-u
			self.sg(uposi*coeff)
			if v < 0:
				vposi = -v
				self.sh(vposi*coeff)
           
			elif v > 0:
				self.sb(v*coeff)
            
        

		elif u>0:
			self.sd(u*coeff)
			if v < 0:
				vposi = -v
				self.sh(vposi*coeff)
            
			elif v > 0:
				self.sb(v*coeff)
           

#fonction qui décale les images du tableau d'images Tab selon leurs positions et retourne le tableau d'images décalées (à finir)
	def Posi_Decalage(self, coeff, x, y):

 
		i=0
		while i<self.l:
			j=0
			print i
			while j<self.c:
				#print j
				self.Decalage(x-i, y-j, coeff)

				j=j+1
			i=i+1
    	
