import pygame, sys
import os

from Tower import Tower
from Map import Map


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


    def draw_window(self, x, y):


        #draw the map
        WIN.blit( Map.surfaceMap(self), (0, 0) )
        #draw the tower
        WIN.blit(x.surfaceTower(), ( x.getXPos(), x.getYPos() ) )

        pygame.display.update()


def main():
    game = Game()
    clock = pygame.time.Clock()
    run = True
    x = Tower(100,200)
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


                x.changePos(x)









                """""
                print(x.getXPos())
                x.setXPos(200)
                print("dans le mousseButtonDown")
                print(x.getXPos())
                print(x.getPos())
                x.pos[0] = x.getXPos()
                """""






        game.draw_window(x,y)



    pygame.quit()


if __name__ == "__main__":
    main()
