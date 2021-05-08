import pygame, sys
import os
from Tower import Tower
from Map import Map
import time 
from Characters import Characters
from GrayEnemy import GrayEnemy
import random
from GrayTurret import GrayTurret


y = Map(0,0)

WIDTH = 1000
HEIGHT = 700
WIN = pygame.display.set_mode( (WIDTH, HEIGHT) )
FPS = 60

pygame.display.set_caption( "Jeux" )


class Game():

    def __init__(self):
        self.lives = 100
        self.towers = [GrayTurret(100,200), Tower(800,200), Tower(500,600)]
        self.characters = []

        self.characterNum = len(self.characters)
        self.towerNum = len(self.towers)
        self.compteur = 0
        self.objectCount = 0

        self.test = 0


    def draw_window(self, x, y,character,game):

       
        #draw the map
        WIN.blit( Map.surfaceMap(self), (0, 0) )

        #draw planes

        for i in range (self.characterNum):
            if game.characters[i].isVisible():
                WIN.blit(game.characters[i].move(game.characters[i]), ( (game.characters[i].getXPos()), (game.characters[i].getYPos()))  ) 
        
        



       
        #draw the towers and their range 
        for tower in range (self.towerNum):

            WIN.blit(self.towers[tower].shooterRange(self.towers[tower].getNormalPosX(), self.towers[tower].getNormalPosY()),  (int(self.towers[tower].getNormalPosX()-self.towers[tower].getNormalPosX()), (int(self.towers[tower].getNormalPosY()-self.towers[tower].getNormalPosY())) ) ) 
            WIN.blit(self.towers[tower].surfaceTower(), ( self.towers[tower].getXPos(), self.towers[tower].getYPos() ) )
            
   
        pygame.display.update()


    def drawCharacters(self,character):

        #character
        WIN.blit(character.move(),  (int(0), (int(0)) ) ) 

    """
        TODO: faire certain que les enemies perdes leurs vies
    """

    def towerAttack(self):

        for tower in range (self.towerNum-1):
        
            for i in range (self.characterNum-1):

                    if self.characters[i].getXPos() > self.towers[tower].getShootingZoneX(0) and self.characters[0].getXPos() < self.towers[tower].getShootingZoneX(1) and self.characters[i].getYPos() > self.towers[tower].getShootingZoneY(0)and self.characters[0].getYPos() < self.towers[tower].getShootingZoneY(1):

                        self.characters[i].getAttacked()
                

                        print(self.characters[0].getLife())
                      


    #add the different characters to the game every x seconds
    def addCharacters(self):

        if self.compteur %30 == 0:


                randomEnemy = [Characters(),GrayEnemy()]

                randomNumber = random.randint(0,1)

                self.characters.append(randomEnemy[randomNumber])

                self.characterNum = self.characterNum +1

                self.objectCount = self.objectCount + 1


                


def main():
    game = Game()
    clock = pygame.time.Clock()
    run = True
    x = GrayTurret(100,200)
    y = GrayTurret(100,200)
    character = game.characters


    while run:

        game.addCharacters()

        game.towerAttack()
        
       


        game.compteur = game.compteur+1

        #print(game.compteur)
        #print(game.characters[game.objectCount].checkDelete())

        

        isclicked = True
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
                #Change the position of a tower at the clicked position
                #x.changePos(x)

                #print("ceci est x ",x.getXPos())
                #print("Ceci est Y ",x.getYPos())
                print(pygame.mouse.get_pos())


        game.draw_window(x,y, character, game)



    pygame.quit()


if __name__ == "__main__":
    main()
