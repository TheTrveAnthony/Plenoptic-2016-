# coding: utf-8

import pygame
from pygame.locals import *
import numpy
from numpy import array
from numpy import uint8
from numpy import uint64
from PIL import Image
from fonctions import *



class LF:		# classe définissant un Champ lumineux - LF = Light Field -
	
	def __init__(self, tab):
		
		self.tab = tab		#le tableau d'images du champ
		self.x = 0			# la colonne du tableu où on se trouve
		self.y = 0			# la ligne du tableau où on se trouve
		self.img = self.tab[0][0]   # image tab x,y
		self.apert = False	# booléen pour activer/desactiver l'appertue
		self.f = False		#focus
		self.z = 0 			# degré d'aperture
		self.tab_n = []		#tableau d'images converties en nombres
		
		
	def deplace(self):	#fonction déplacement dans le tableau d'images
		
		
		n = len(self.tab)-1
		m = len(self.tab[0])-1
		for event in pygame.event.get():  
			
			if event.type == QUIT:
				return 0
			
			if event.type == KEYDOWN:
				if event.key == K_DOWN:
			
					if self.x < n:
						self.x += 1
					
				if event.key == K_UP:
			
					if self.x > 0:
						self.x -= 1
											
				if event.key == K_RIGHT:
			
					if self.y < m:
						self.y += 1
								
				if event.key == K_LEFT:
			
					if self.y > 0:
						self.y -= 1
						
				if event.key == K_SPACE:		#pour (des)activer l'aperture
					if self.apert == False:
						self.apert = True
						print("aperture activé\n")
					elif self.apert == True:
						self.apert = False
						print("aperture desactivé\n")
						
				if event.key == K_f:		#pour (des)activer l'aperture
					if self.f == False:
						self.f = True
						print("focus activé\n")
					elif self.f == True:
						self.f = False
						print("focus desactivé\n")
									
				if event.key == K_a and self.z > 0:	#pour changer le degré de l'aperture
					self.z -= 1
				if event.key == K_z and self.z < len(self.tab):
					self.z += 1
												
		self.img = self.tab[self.x][self.y]
		return 1
		
		
	def aprt(self):		#fonction aperture
		
		if self.apert == True or self.f == True:	#si l'aperture ou les focus est activée
			

			
			y_min = self.y-self.z #première ligne
			y_max = self.y+self.z #dernière ligne
			x_min = self.x-self.z #première colonne
			x_max = self.x+self.z #dernière colonne
			
			i = x_min
			j = y_min

			s = numpy.uint64(self.tab_n[self.x][self.y])  # valeur de la somme
			t = 1 # itérateur pour moyenner
			
			while i <=  x_max:		# somme de tous les éléments
				while j <= y_max:
					if i < len(self.tab) and j < len(self.tab):
						if   i >= 0 and j >= 0:
							#print(self.tab[i][j])
							s += numpy.uint64(self.tab_n[i][j])
							t += 1
							
					j += 1
		
				i += 1
				j = y_min
					
			#print(t)
			so = s/t
			#print(so)
			self.img = Tableau_Image(so)
			#print(type(a))
		return 1
		
	
	def convert(self):	#sert à convertir le tableau d'images en int
		
		x = 0

		while x < len(self.tab):
			y = 0
			self.tab_n.append([])
			while y < len(self.tab[0]):
				self.tab_n[x].append(Image_Tableau(self.tab[x][y]))
					
				y += 1
			x += 1
		return 1
	
"""
			
class tabz:		# classe pour les décalages sur tableaux
	
	def __init__(self, tab):
		
		self.tab = tab
		self.l = len(tab)
		self.c = len(tab[0])
		
		
	def sb(self, nb): #prend un array et le nb de pixels à shifter en bas

		tbl = np.zeros(((self.l, self.c, 3)))
		i=self.l-1
	
		while i>-1:

			if i >= nb:
				tbl[i] = self.tab[i-nb]
			i=i-1
		self.tab = tbl
		


	def sh(self, nb):

		tbl = np.zeros(((self.l, self.c, 3)))
		i = 0

		while i < self.l:

			if i <= selfl-1-nb:
				tbl[i]=tab[i+nb]
			i=i+1
		self.tab = tbl
    

	def sg(self, nb):

		tbl = np.zeros(((self.l, self.c, 3)))
		i=0
		while i<self.c:
			if i<=self.c-1-nb:
				t=0
				while t<self.l:
					tbl[t][i]=self.tab[t][i+nb]
					t=t+1
			i=i+1
		self.tab = tbl
    

	def sd(self, nb):

		self.l = np.zeros(((self.l, self.c, 3)))
		i=self.c-1
		while i>-1:

			if i>=nb:
				t=0
				while t<self.l:
					tbl[t][i]=self.tab[t][i-nb]
					t=t+1
			i=i-1
		self.tab = tbl
    
"""
