from BuyGreenTower import BuyGreenTower
import os
import pygame

class BuySubMachineGun(BuyGreenTower):

	def __init__(self, posX, posY):

		self.posX = posX
		self.posY = posY


	def drawBuyTower(self):


		current_path = os.path.dirname("towerDefense")

		transform = os.path.join(current_path, "SubMachineGun.png")

		Tower = pygame.image.load(transform).convert_alpha()

		Tower = pygame.transform.scale(Tower, (200, 120) )
		
		return Tower