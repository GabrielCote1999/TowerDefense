import pygame

class Characters():


	def __init__(self,posX,posY):

		self.posY = 100
		self.posX = 100
		self.life = 50
		self.ray = 30

	def move(self):

		surface = pygame.Surface((1000,700), pygame.SRCALPHA, 32)

		circle = pygame.draw.circle(surface, (255,255,0), (self.posX, self.posY), 12 )

		self.posX = self.posX +1

		return surface

		
	

  

		


	

		


