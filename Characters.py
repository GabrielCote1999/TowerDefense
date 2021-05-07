import pygame

class Characters():


	def __init__(self):

		self.posY = 520
		self.posX = 0
		self.life = 50
		self.ray = 30



	def getXpos(self):

		return self.posX

	def getYpos(self):

		return self.posY

	def move(self):

		surface = pygame.Surface((1000,700), pygame.SRCALPHA, 32)

		circle = pygame.draw.circle(surface, (255,255,0), (self.posX, self.posY), 12 )

		if self.posX < 133:

			self.posX = self.posX +5

		elif self.posX > 133 and self.posX < 223  :

			self.posY = self.posY -5
			self.posX = self.posX +2

		elif self.posX >= 223 and self.posX < 324:

			self.posX = self.posX +5

		elif self.posX >= 324 and self.posX < 370:

			self.posX = self.posX +1
			self.posY = self.posY - 5

		elif self.posX >= 370 and self.posX< 869 and self.posY<100:

			self.posX = self.posX +5

		elif self.posX >=869 and self.posX < 920 and self.posY<=215 :

			self.posX = self.posX +2
			self.posY = self.posY +5
			
			

		elif self.posX <=920  and self.posY >= 215 and self.posY< 395:

			self.posX = self.posX -5
			self.posY = self.posY +5
			

		elif self.posX >= 740 and self.posY >=395 and self.posY < 525:

			self.posX = self.posX +2
			self.posY = self.posY +5
			

			

		elif self.posX >= 792 and self.posY >= 525 and self.posX <= 905:

			self.posX = self.posX +5			

		elif self.posX >=907 and self.posY >= 525 and self.posY < 700:

			self.posY = self.posY +5
		
		
			


		

		#elif self.

		return surface

		
	

  

		


	

		


