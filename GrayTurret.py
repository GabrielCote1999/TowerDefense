import pygame
from Tower import Tower
import os


class GrayTurret(Tower):

	def __init__(self, xPos, yPos):
	
		super(GrayTurret,self).__init__(xPos,yPos)

		




	"""
		Define the image of the tower and scale it 
	"""

	def surfaceTower(self):

		current_path = os.path.dirname("towerDefense")

		transform = os.path.join(current_path, "greyTurret.png")

		grayTower = pygame.image.load(transform)

		grayTower = pygame.transform.scale(grayTower, (100, 100))

		return grayTower







