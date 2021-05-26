import pygame
from Characters import Characters



class BrownEnemy(Characters):

	def __init__(self):

		self.posY = 520
		self.posX = 0
		self.life = 75
		self.ray = 30
		self.width = 100
		self.length = 100
		self.folderName = "towerDefense"
		self.assetName = "BrownEnemy.png"
		self.dmg = 2
		self.dmgCount = 1
		self.angle = 0


	def drawHealthBar(self, WIN):


		pygame.draw.rect(WIN, (255,0,0), pygame.Rect(self.getXPos() + self.width/4  , self.getYPos(), 75, 10))

		pygame.draw.rect(WIN, (0,255,0), pygame.Rect(self.getXPos() + self.width/4 , self.getYPos(), self.getLife() , 10))




	


