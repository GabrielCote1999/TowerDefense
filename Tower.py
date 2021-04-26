import pygame
import os

class Tower():

 

    def __init__(self,xPos, yPos):

        self.xPos = xPos
        self.yPos = yPos
        self.isSelected = False
        self.pos = [self.xPos, self.yPos]


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


















x = Tower(2,3)










