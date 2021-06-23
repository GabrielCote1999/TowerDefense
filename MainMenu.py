import pygame
import pygame_menu

class MainMenu():

	def __init__(self):

		self.bouton = False
		self.backGroundColor = (255,100,100)


	def drawMenu(self,WIN, screenWidth, screenHeight):

		pygame.draw.rect(WIN, self.backGroundColor, pygame.Rect(0, 0, screenWidth, screenHeight))

		



