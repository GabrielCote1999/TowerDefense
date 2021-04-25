import pygame, sys

from Tower import Tower

# x = Tower( 2, 3 )

WIDTH = 1500
HEIGHT = 1000
WIN = pygame.display.set_mode( (WIDTH, HEIGHT) )
FPS = 60

pygame.display.set_caption( "Jeux" )

map = pygame.image.load( r'C:\Users\Gabriel\Desktop\Apprentissage\Td\TowerDefense\game_background_3.png' )

map = pygame.transform.scale( map, (WIDTH, HEIGHT) )


class Game():

    def __init__(self):
        self.lives = 100
        self.towers = []


    def draw_window(self, x):

        WIN.blit( map, (0, 0) )
        WIN.blit(x,(200,110))
        pygame.display.update()


def main():
    game = Game()
    clock = pygame.time.Clock()
    run = True
    x = Tower(2,3)
    while run:

        # clock
        clock = pygame.time.Clock()
        run = True
        # make sure that we dont go over 60 fps
        clock.tick( FPS )

        # liste des différents évènements
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        game.draw_window(x.surfaceTower())



    pygame.quit()


if __name__ == "__main__":
    main()
