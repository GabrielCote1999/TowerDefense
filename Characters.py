import pygame

class Characters():


	def __init__(self,posX,posY):

		self.posY = posY
		self.posX = posX
		self.life = 50
		self.ray = 30

	def move(self):

		surface = pygame.Surface((1000,700), pygame.SRCALPHA, 32)
		circle = pygame.draw.circle(surface, (30,224,200), (500, 40), 12 )

		return surface
	

  

		


	

		


