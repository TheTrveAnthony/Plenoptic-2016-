# coding: utf-8
import pygame
from pygame.locals import *
import numpy
from numpy import array
from numpy import uint8
from numpy import uint64
from PIL import Image
from tableaux import *
from fonctions import *
from classes import *


print("choisissez un champ à visualiser:")
print("poissons:1")
print("hummer:2")
print("dragon:3")
choix = input()
im = LF(construire(choix))	# construction de la liste finale
im.convert()
w = l_h(choix)

pygame.init()
fenetre = pygame.display.set_mode((w[0], w[1]), RESIZABLE)
fenetre.blit(pygame.image.load(im.img).convert(), (0,0))


continuer = 1
pygame.key.set_repeat(1, 50)
while continuer:
	pygame.time.Clock().tick(30)
	
	continuer = im.deplace()
	im.aprt()
	if im.apert:
		fenetre.blit(pygame.image.load("trash/aux.png").convert(), (0,0))
	else:
		fenetre.blit(pygame.image.load(im.img).convert(), (0,0))
	pygame.display.flip()
	
	
	
					


 
