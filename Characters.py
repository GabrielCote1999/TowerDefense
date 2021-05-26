import pygame
import os





class Characters():


	def __init__(self):

		self.posY = 520
		self.posX = 0
		self.life = 50
		self.ray = 30
		self.width = 100
		self.length = 100
		self.folderName = "towerDefense"
		self.assetName = "greenPlane.png"
		self.dmg = 2
		self.dmgCount = 1
		self.angle = 0


	def getDmgCount(self):

		return self.dmgCount

	def decDmgCount(self):

		self.dmgCount = self.dmgCount -1 

	def getDmg(self):

		return self.dmg


	def drawHealthBar(self, WIN):


		pygame.draw.rect(WIN, (255,0,0), pygame.Rect(self.getXPos()+ 20  , self.getYPos(), 50, 10))

		pygame.draw.rect(WIN, (0,255,0), pygame.Rect(self.getXPos()+ 20  , self.getYPos(), self.getLife() , 10))


	def getXPos(self):

		return self.posX- self.width/2

	def getYPos(self):

		return self.posY - self.width/2


	def calculateHealthBarLength(self):

		return self.getLife() % 50

	def getAngle(self):

		return self.angle

	def setAngle(self, x):

		self.angle = self.angle + x

		return self.angle



	"""
		TODO: mettre les changements de mouvements dans une fonction unique
	"""

	def move(self, plane):

		current_path = os.path.dirname( self.folderName )

		transform = os.path.join( current_path, self.assetName )

		plane = pygame.image.load( transform )

		plane = pygame.transform.scale( plane, (100, 100) )

		#plane = pygame.transform.rotate(plane, 100)

		

		if self.posX < 133:

			self.posX = self.posX +5

			

		elif self.posX > 133 and self.posX < 220  :

			self.posY = self.posY -5
			self.posX = self.posX +2

			plane = pygame.transform.rotate(plane, 70)

			



		elif self.posX >= 170 and self.posX < 324:

			self.posX = self.posX +5
			plane = pygame.transform.rotate(plane, -5)


		elif self.posX >= 324 and self.posX < 370:

			self.posX = self.posX +1
			self.posY = self.posY - 5
			plane = pygame.transform.rotate(plane, 75)

		elif self.posX >= 370 and self.posX< 869 and self.posY<100:

			self.posX = self.posX +5
			plane = pygame.transform.rotate(plane, -5)
			

		elif self.posX >=869 and self.posX <= 950 and self.posY<=210 :

			self.posX = self.posX +2
			self.posY = self.posY +5
			plane = pygame.transform.rotate(plane, -75)
			
			

		elif self.posX >=740  and self.posY >= 150 and self.posY< 360:

			self.posX = self.posX -6
			self.posY = self.posY +5
			
			plane = pygame.transform.rotate(plane, -135)


	

		elif self.posX >= 740 and self.posY >=360 and self.posY < 525:

			self.posX = self.posX +1
			self.posY = self.posY +6

			plane = pygame.transform.rotate(plane, -75)
			

			

		elif self.posX >= 775 and self.posY >= 525 and self.posX <= 905:

			self.posX = self.posX +5			

		elif self.posX >=900 and self.posY >= 525 and self.posY < 700:

			self.posY = self.posY +5
			plane = pygame.transform.rotate(plane, -90)

			

		elif self.posX >=905 and self.posY >= 525 and self.posY < 750 or self.getLife() <= 0:

			plane = pygame.transform.rotate(plane, -90)

			self.setInvisible()


		return plane

	def checkDelete(self):

		if self.posY <=300:

			print("est plus grand que 600")

			self.pop()
			return True
		else:
			return False

	def getLife(self):

		return self.life

	def getAttacked(self):

		self.life = self.life -1
		return self.life

	def isVisible(self):

		if self.life > 0:

			return True

		return False

	def setInvisible(self):

		self.life = 0

		
	

  

		


	

		


