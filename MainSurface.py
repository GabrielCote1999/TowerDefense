import pygame, sys
import os
from Tower import Tower
from Map import Map
import time 
from Characters import Characters
from GrayEnemy import GrayEnemy
import random
from GrayTurret import GrayTurret
from BrownEnemy import BrownEnemy
from BuyGreenTower import BuyGreenTower
from BuyRocketTower import BuyRocketTower
from BuySubMachineGun import BuySubMachineGun
from MainMenu import MainMenu

pygame.init()
y = Map(0,0)

WIDTH = 1000
HEIGHT = 700
WIN = pygame.display.set_mode( (WIDTH, HEIGHT) )
FPS = 60
RED = (255,0,0)

pygame.display.set_caption( "Jeux" )
font = pygame.font.Font(None, 50)

class Game():

    def __init__(self):
        self.lives = 50
        self.towers = [Tower(100,200), Tower(800,150), Tower(800,600)]
        self.characters = []
        self.buyTower =[BuyGreenTower(0,580), BuyRocketTower(200, 580), BuySubMachineGun(400,580)]
        self.menus = [MainMenu()]

        self.characterNum = len(self.characters)
        self.towerNum = len(self.towers)
        self.buyTowerNum = len(self.buyTower)
        self.compteur = 0
        self.objectCount = 0

        self.gameLife = 100
        self.click = False

        self.test = 0

        self.musicCount = 0



    def clicks(self):

        if self.click == True:

            self.click = False
        else:

            self.click = True

    def drawScore(self):

        text = font.render("Life: " +str(self.getGameLife()), 0, (50,255,110))
        WIN.blit(text, (10,10))
        
    def drawMenu(self):

        soundObj = pygame.mixer.Sound('lofi.wav')

        if self.musicCount != 1:
            soundObj.play()

        self.menus[0].drawMenu(WIN, WIDTH, HEIGHT)

        myFont = pygame.font.SysFont('Geometric Sans-serif', 90)

        towerDefense = myFont.render("Tower Defense", 100, (250,255,110))

        settings = myFont.render("Settings", 100, (250,255,110))

        quit = myFont.render("Quit", 100, (250,255,110))

        play = myFont.render("Play", 100, (255, 255, 110))

        WIN.blit(play, (255, 200))

        WIN.blit(towerDefense, (245,50))

        WIN.blit(settings, (255,300))

        WIN.blit(quit,(255,400))

        self.musicCount = 1
        

       
    def draw_Menus(self, game):

        self.drawMenu()

        pygame.display.update()



    def showTowerRange(self):

        for i in range(self.towerNum):

            #look if the user have clicked on a tower NOT DONE
            if pygame.mouse.get_pos()[0] >= self.towers[i].getXPos() and pygame.mouse.get_pos()[0] <=  self.towers[i].getXPos()+self.towers[i].getWidth() and pygame.mouse.get_pos()[1] <= self.towers[i].getYPos()+self.towers[i].getLength() and pygame.mouse.get_pos()[1] >= self.towers[i].getYPos() and self.getClick() == False:

                self.towers[i].isClick()
                print("yoo")

            else:

                self.towers[i].unClick()

    def moveTower(self, key_pressed):

        for i in range(self.towerNum):

        #look if the m key is pressed 

            if pygame.mouse.get_pos()[0] >= self.towers[i].getXPos() and pygame.mouse.get_pos()[0] <=  self.towers[i].getXPos()+self.towers[i].getWidth() and pygame.mouse.get_pos()[1] <= self.towers[i].getYPos()+self.towers[i].getLength() and pygame.mouse.get_pos()[1] >= self.towers[i].getYPos() and self.towers[i].getClickMove() == False and key_pressed[pygame.K_m]:

                self.towers[i].setStartPos(pygame.mouse.get_pos())
                self.towers[i].isClickMove()

            elif pygame.mouse.get_pos() != self.towers[i].getStartPos() :

                self.towers[i].unClickMove()

    def getClick(self):

        return self.click



    def gameDmg(self):

        for i in range (self.characterNum):
           # print("pos de 0 ",self.characters[0].isVisible())

            if self.characters[i].getYPos() >= 650 and self.characters[i].isVisible() == True and self.characters[i].getDmgCount() !=0:

                self.gameLife = self.gameLife - self.characters[i].getDmg()

                self.characters[i].decDmgCount()
                #print("dans if")


    def getGameLife(self):

        return self.gameLife

    def drawBuyTower(self):

        for i in range(self.buyTowerNum):

            WIN.blit(self.buyTower[i].drawBuyTower(), (self.buyTower[i].getPosX(),self.buyTower[i].getPosY()))
        

    #draw the map
    def draw_map(self):

        WIN.blit( Map.surfaceMap(self), (0, 0) )
        

 
    def draw_window(self,game):



       
        #draw the map
       # self.draw_map()

        
        #draw characters
        #self.drawCharacters()

        #self.drawScore()

        #self.drawBuyTower()

       

       # self.drawTower()



        self.drawMenu()
        pygame.display.update()
        

    def drawTower(self):

        #draw the towers and their range 
        for tower in range (self.towerNum):

            if self.towers[tower].getClick() == True:

                WIN.blit(self.towers[tower].shooterRange(self.towers[tower].getNormalPosX(), self.towers[tower].getNormalPosY()),  (int(self.towers[tower].getNormalPosX()-self.towers[tower].getNormalPosX()), (int(self.towers[tower].getNormalPosY()-self.towers[tower].getNormalPosY())) ) ) 
                
            WIN.blit(self.towers[tower].surfaceTower(), ( self.towers[tower].getXPos(), self.towers[tower].getYPos()  ) )

        



    #Draw the characters on the map
    
    def drawCharacters(self):

        #character
        for i in range (self.characterNum):
            if self.characters[i].isVisible():

                self.characters[i].drawHealthBar(WIN)

                WIN.blit(self.characters[i].move(self.characters[i]), ( (self.characters[i].getXPos()), (self.characters[i].getYPos()))  ) 

                
                

    #attack the first enemy that entered the shooting zone of the turret

    def towerAttack(self):

        self.towerList()

        for tower in range (self.towerNum-1):

            if self.towers[tower].getEnemyInRange() != []:

                self.towers[tower].getEnemyInRange()[len(self.towers[tower].getEnemyInRange())-1].getAttacked()

    """
        Add the enemy to a list if they are in range, delete them if they are not
    """

    def towerList(self):

        for tower in range (self.towerNum-1):

            for i in range (self.characterNum-1):

                    #look if the enemies are in the turrent range, if they are, add them in the list
                    if self.characters[i].getXPos() > self.towers[tower].getShootingZoneX(0) and self.characters[i].getXPos() < self.towers[tower].getShootingZoneX(1) and self.characters[i].getYPos() > self.towers[tower].getShootingZoneY(0)and self.characters[i].getYPos() < self.towers[tower].getShootingZoneY(1):

                        if self.characters[i] not in self.towers[tower].getEnemyInRange():

                            self.towers[tower].addEnemyInRange(self.characters[i])



                    #look if the enemies are not in the turrent range, in they are not, remove them from the list
                    elif self.characters[i] in self.towers[tower].getEnemyInRange() and (self.characters[i].getXPos() < self.towers[tower].getShootingZoneX(0) or self.characters[i].getXPos() > self.towers[tower].getShootingZoneX(1)) and (self.characters[i].getYPos() < self.towers[tower].getShootingZoneY(0)or self.characters[i].getYPos() > self.towers[tower].getShootingZoneY(1) ):

                        print("dans if")
                        self.towers[tower].removeEnemy(self.towers[tower].getEnemyInRange().index(self.characters[i]))
                        


    #add the different characters to the game every x seconds
    def addCharacters(self):

        if self.compteur %30 == 0:


                randomEnemy = [Characters(),GrayEnemy(), BrownEnemy()]

                randomNumber = random.randint(0,2)

                self.characters.append(randomEnemy[randomNumber])

                self.characterNum = self.characterNum +1

                self.objectCount = self.objectCount + 1


def main():
    game = Game()
    clock = pygame.time.Clock()
    run = True

    character = game.characters


    while run:

        game.addCharacters()

        game.towerAttack()

        game.gameDmg()

        

       


        #print("this is game life", game.getGameLife())

        game.compteur = game.compteur+1

        #print(game.compteur)
        #print(game.characters[game.objectCount].checkDelete())

        # clock
        clock = pygame.time.Clock()
        run = True
        # make sure that we dont go over 60 fps
        clock.tick( FPS )

        # liste des différents évènements
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                game.showTowerRange()
                #Change the position of a tower at the clicked position
                #x.changePos(x)

                #print("ceci est x ",x.getXPos())
                #print("Ceci est Y ",x.getYPos())
                print(pygame.mouse.get_pos())


            if event.type == pygame.KEYDOWN :

                key_pressed = pygame.key.get_pressed()

               

                game.moveTower(key_pressed)
                

        print('fps', clock.tick(FPS))

        game.draw_Menus(game)
        #game.draw_window(game)




    pygame.quit()


if __name__ == "__main__":
    main()
