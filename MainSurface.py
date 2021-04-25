import pygame, sys




WIDTH = 1500
HEIGHT = 1000
WIN = pygame.display.set_mode( (WIDTH, HEIGHT) )
FPS = 60

pygame.display.set_caption( "Jeux" )




map = pygame.image.load(r'C:\Users\Gabriel\Desktop\Apprentissage\Td\TowerDefense\game_background_3.png')

map = pygame.transform.scale(map,(WIDTH,HEIGHT))


def draw_window():

    WIN.blit(map, (0, 0) )
    pygame.display.update()

def main():

    clock = pygame.time.Clock()
    run = True
    while run:

        # clock
        clock = pygame.time.Clock()
        run = True
        # make sure that we dont go over 60 fps
        clock.tick(FPS)

        # liste des différents évènements
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()










