import pygame
import os
#from MainSurface import MainSurface

class Tower():



    def __init__(self, xPos, yPos):

        self.xPos = xPos
        self.yPos = yPos
        self.isSelected = False
        self.pos = [self.xPos, self.yPos]
        self.width = 100
        self. length = 100
        self.shootingRange = 120
        self.enemyInRange = []
        self.angle = 0
        self.click = False
        self.clickMove = False
        self.startPos = []



    #set the startPos to a position
    def setStartPos(self, pos):

        self.startPos = pos
    



    #get the position of the turrent when it was clicked
    def getStartPos(self):

        return self.startPos


    #define clickMove to True
    def isClickMove(self):

        self.clickMove = True

    #define clickMove to fasle
    def unClickMove(self):

        self.clickMove = False


    #define if a tower is clicked or not
    def moveTower(self):

        if self.getClickMove() == True :

            self.setPos(pygame.mouse.get_pos()) 


    def getClickMove(self):

        return self.clickMove

    def getClick(self):

        return self.click


    def isClick(self):


        self.click = True

    def unClick(self):

        self.click = False


    #temporaire
    def plusAngle(self):

        self.angle = self.angle + 2

    #temporaire
    def getAngle(self):

        return self.angle

    def rotateTowardEnemies(self):

        #if self.getEnemyInRange() != [] :

          #  angle = self.getYPos() - self.getEnemyInRange()[len(self.getEnemyInRange())-1].getYPos()

        #else:
         #   return 0 



        return angle






    #return the list of the enemies in range
    def getEnemyInRange(self):

        return self.enemyInRange

    #add the enemies in range in a list
    def addEnemyInRange(self, character):

        self.enemyInRange.append(character)


    #delete the enemy not in range anymore of the list
    def removeEnemy(self, character):

        self.enemyInRange.pop(character)


    """
        Define the turrent range on the x axes
    """
    def getShootingZoneX(self, pos):

        x1 = self.getXPos() - self.shootingRange//2 -10

        x2 = self.getXPos()+ self.length + self.shootingRange//2 + 10

        if pos == 0:

            return x1

        return x2


    """
        Define the turrent range on the y axes
    """
    def getShootingZoneY(self, pos):

        y1 = self.getNormalPosY() - self.shootingRange 

        y2 = self.getNormalPosY()+ self.length +20

        if pos == 0:
            
            return y1

        return y2 
        

    """
        draw the turrent range 
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

        

        Tower = pygame.image.load(transform).convert_alpha()

        

        Tower = pygame.transform.rotate(Tower,self.getAngle())

        Tower = pygame.transform.scale(Tower, (100, 100) )

        #Tower_copy = pygame.transform.scale(Tower, (100, 100) )

        #self.plusAngle()
        self.moveTower()

       # Tower = pygame.transform.rotate(Tower,self.getAngle())


        
        

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

    def setPos(self,pos):

       self.setXPos(pos[0]-self.getWidth()/2)
       self.setYPos(pos[1]-self.getLength()/2)

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










