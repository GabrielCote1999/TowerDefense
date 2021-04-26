import pygame
import os

class Tower():

    xPos = 0
    yPos = 0
 

    def __init__(self, xPos, yPos):

        self.xPos = xPos
        self.yPos = yPos
        self.isSelected = False


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


    def getSelected(self):

        return self.isSelected


x = Tower(2,3)










