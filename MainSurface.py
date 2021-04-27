import pygame, sys
import os

from Tower import Tower
from Map import Map

from Characters import Characters


y = Map(0,0)

WIDTH = 1000
HEIGHT = 700
WIN = pygame.display.set_mode( (WIDTH, HEIGHT) )
FPS = 60

pygame.display.set_caption( "Jeux" )


class Game():

    def __init__(self):
        self.lives = 100
        self.towers = []


    def draw_window(self, x, y,character):


        #draw the map
        WIN.blit( Map.surfaceMap(self), (0, 0) )

        #draw the tower
        WIN.blit(x.surfaceTower(), ( x.getXPos(), x.getYPos() ) )

        #draw the tower range
        WIN.blit(x.shooterRange(x.getNormalPosX(), x.getNormalPosY()),  (int(x.getNormalPosX()-x.getNormalPosX()), (int(x.getNormalPosY()-x.getNormalPosY())) ) ) 


        
        WIN.blit(character.move(),  (int(30), (int(39)) ) ) 
        
  
        pygame.display.update()


def main():
    game = Game()
    clock = pygame.time.Clock()
    run = True
    x = Tower(100,200)

    character = Characters(30,30)
    while run:

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
                x.changePos(x)


        game.draw_window(x,y, character)



    pygame.quit()


if __name__ == "__main__":
    main()
