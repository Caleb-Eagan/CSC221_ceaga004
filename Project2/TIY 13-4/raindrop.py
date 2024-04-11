import pygame
from pygame.sprite import Sprite
import random

class Rain(Sprite):
    def __init__(self, rain_game):
        super().__init__()
        self.screen = rain_game.screen
        self.settings = rain_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.image_fix()

    def image_fix(self):
        '''Fixes the background of the ship image. Done to satisfy TIY 12-2'''
        image_pixel_array = pygame.PixelArray(self.image)
        image_pixel_array.replace((255,255,255),self.settings.bg_color)