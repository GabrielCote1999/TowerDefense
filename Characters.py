import pygame

class RedTower():

	def __init__(self,posX,posY, ray):

		self.posY = posY
		self.posX = posX
		self.life = 50
		self.ray = ray
		self.type = 'redTower'
		self.defense = 10
		self.dmg = 20
		x =pygame.Rect(30,30,300,30)

	def setLife(self, life):

		self.life = life

	def getLife(self):

		return self.life

	def setRange(self, ray):

		self.ray = (ray*ray)*3.14


	def getRange(self):

		return self.ray

	def getType(self):

		return self.type

	def setDef(self, defense):

		self.defense = defense

	def getDef(self):

		return self.defense

	def getPos(self):
		pass

	def setPos(self):
		pass

	def setDmg(self, dmg):
		self.dmg = dmg

	def getDmg(self):

		return self.dmg