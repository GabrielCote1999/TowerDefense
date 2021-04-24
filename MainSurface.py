import pygame

class mainSurface():

	

	def __init__(self):

		self.WIDTH = 700
		self.HEIGHT= 700
		self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		pygame.display.set_caption("Jeux")
		self.fps = 60
		

x = mainSurface()


