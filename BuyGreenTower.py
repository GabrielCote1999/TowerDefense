import pygame
import os

class BuyGreenTower():

	def __init__(self, posX, posY):

		self.posX = posX
		self.posY = posY
		self.width = 100
		self.height = 100

	def drawBuyTower(self):

		current_path = os.path.dirname("towerDefense")

		transform = os.path.join(current_path, "BuyGreenTower.png")

		Tower = pygame.image.load(transform)

		Tower = pygame.transform.scale(Tower, (200, 200) )
		return Tower

	def getPosX(self):

		return self.posX

	def getPosY(self):

		return self.posY
       



		


	

		

       
