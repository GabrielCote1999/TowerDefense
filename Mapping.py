import pygame

import MainSurface

class Mapping():
    def __init__(self, x):
        self.x = x

          
    def showMap(self, display_surface=None):

        x = (self.image,0,0)
        return x


    def drawMap(self):
        map = pygame.image.load( r'C:\Users\Gabriel\Desktop\Apprentissage\Td\TowerDefense\game_background_3.png' )

        map = map = pygame.transform.scale( map, (1500, 1000) )

        return map








