import pygame
import os
from Characters import Characters

class GrayEnemy(Characters):

	def __init__(self):

		self.posY = 520
		self.posX = 0
		self.life = 100
		self.ray = 30
		self.width = 100
		self.heigth = 100




	def move(self, grayEnemy):

		current_path = os.path.dirname( "towerDefense" )

		transform = os.path.join( current_path, "grayEnemy.png" )

		grayEnemy = pygame.image.load( transform )

		grayEnemy = pygame.transform.scale( grayEnemy, (self.width, self.heigth) )

		

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

		return grayEnemy


