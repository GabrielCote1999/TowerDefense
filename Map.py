import pygame
import os

class Map():

	xPos = 0
	yPos = 0

	def __init__(self, xPos, yPos):

		self.xPos = xPos
		self.yPos = yPos

	""""
	Search for the image of the map, resize it and return it surface object
	RETURN : map object
	"""
	def surfaceMap(self):

		current_path = os.path.dirname( "towerDefense" )

		transform = os.path.join( current_path, "game_background_3.png" )

		map = pygame.image.load( transform )

		map = pygame.transform.scale( map, (1000, 700) )

		return map









