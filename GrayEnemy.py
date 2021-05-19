import pygame
import os
from Characters import Characters

class GrayEnemy(Characters):

	def __init__(self):

		self.posY = 520
		self.posX = 0
		self.life = 150
		self.ray = 30
		self.width = 100
		self.heigth = 100
		self.folderName = "towerDefense"
		self.assetName = "grayEnemy.png"
		self.dmg= 2
		self.dmgCount = 1


	def drawHealthBar(self, WIN):


		pygame.draw.rect(WIN, (255,0,0), pygame.Rect(self.getXPos() - 20  , self.getYPos(), 150, 10))

		pygame.draw.rect(WIN, (0,255,0), pygame.Rect(self.getXPos() - 20  , self.getYPos(), self.getLife() , 10))





	