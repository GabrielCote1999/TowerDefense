import pygame

class Tower():

    xPos = 0
    yPos = 0
    Tower = pygame.image.load( r'C:\Users\Gabriel\Desktop\Apprentissage\Td\TowerDefense\towerDefense_tile249.png' )

    def __init__(self, xPos, yPos):

        self.xPos = xPos
        self.yPos = yPos
        self.isSelected = False


    """"
    Search for the image of a tower, resize it and return it surface object
    RETURN : surface object
    """
    def surfaceTower(self):

        surface = pygame.image.load( r'C:\Users\Gabriel\Desktop\Apprentissage\Td\TowerDefense\towerDefense_tile249.png' )

        surface = pygame.transform.scale( surface, (100, 100) )

        return surface


    def getSelected(self):

        return self.isSelected


x = Tower(2,3)

print(x.return2())








