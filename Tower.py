import pygame
import os
#from MainSurface import MainSurface

class Tower():



    def __init__(self,xPos, yPos):

        self.xPos = xPos
        self.yPos = yPos
        self.isSelected = False
        self.pos = [self.xPos, self.yPos]
        self.width = 100
        self. length = 100
        self.shootingRange = 120
        

    """
        Define the turrent range and draw it
        *1000,700 = screen size

    """
    def shooterRange(self, normalisedPosX, normalisedPosY):
        

        surface = pygame.Surface((1000,700), pygame.SRCALPHA, 32)

        circle = pygame.draw.circle(surface, (30,224,200,100), (int(normalisedPosX), (int(normalisedPosY)) ) , int(self.shootingRange))

        return surface

    def getShootingRange(self):

        return self.shootingRange


    def setShootingRange(self, length):

        self.shootingRange = 3.14 * length*length

    def getNormalPosX(self):

        normalisedPosX = (self.xPos)+self.length//2

        return normalisedPosX


    def getNormalPosY(self):

        normalisedPosY = (self.yPos)+self.length//2

        return normalisedPosY




    """"
    Search for the image of a tower, resize it and return it surface object
    RETURN : surface object
    """
    def surfaceTower(self):

        current_path = os.path.dirname("towerDefense")

        transform = os.path.join(current_path, "towerDefense_tile249.png")

        Tower = pygame.image.load(transform)

        Tower = pygame.transform.scale(Tower, (100, 100) )

        return Tower

    def getXPos(self):

        return self.xPos

    def getYPos(self):

        return self.yPos

    def getPos(self):

        return self.pos

    def setXPos(self,x ):

        self.xPos = x

    def setYPos(self, yPos):

        self.yPos = yPos

    def setPos(self,x,y):

        self.pos[self.xPos,self.yPos] = [x,y]

    def getLength(self):

        return self.length

    def getWidth(self):

        return self.width

    """"
       Change the position of a tower to a clicked position
       RETURN : void
    """

    def changePos(self,tower):


        positionX = pygame.mouse.get_pos()[0]

        positionY = pygame.mouse.get_pos()[1]

        tower.setXPos( (positionX - tower.getWidth() / 2) )

        tower.setYPos( (positionY - tower.getLength() / 2) )






















x = Tower(2,3)










