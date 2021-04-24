import pygame

class Tower(metaclass=abc.ABCMeta):
	 @abc.abstractmethod
	
	def setLife(self):
		pass

	def getLife(self):
		pass

	def setRange(self):
		pass

	def getRange(self):
		pass

	def getType(self):
		pass

	def setDef(self):
		pass

	def getDef(self):
		pass

	def getPos(self):
		pass

	def setPos(self):
		pass

	def setDmg(self):
		pass

	def getDmg(self):
		pass

class RedTower(Tower):

	def __init__(self,posX,posY, ray):

		self.posY = posY
		self.posX = posX
		self.life = 50
		self.ray = ray
		self.type = redTower
		self.def = 10
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

	def setDef(self, def):

		self.def = def

	def getDef(self):
		return self.def

	def getPos(self):
		pass

	def setPos(self):
		pass

	def setDmg(self, dmg):
		self.dmg = dmg

	def getDmg(self):
		return self.dmg
