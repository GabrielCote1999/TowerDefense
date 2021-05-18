import pygame
from Characters import Characters



class BrownEnemy(Characters):

	def __init__(self):

		self.posY = 520
		self.posX = 0
		self.life = 50
		self.ray = 30
		self.width = 100
		self.length = 100
		self.folderName = "towerDefense"
		self.assetName = "BrownEnemy.png"
		self.dmg = 2
		self.dmgCount = 1


	


