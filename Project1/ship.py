import pygame

from settings import Settings

# Credit to Killy Overdrive for the ship images: https://opengameart.org/content/spaceship-360
# The code in here should satisfy TIY 12-2

class Ship:
    '''A class to manage the ship'''

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the settings
        self.settings = Settings()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/shipUP_64.bmp')
        self.image_fix()
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement Flag: Start with a ship that isn't moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.dx = 0
        self.dy = 0
    
    def update(self):
        '''Update the ship's position and orientation based on the movement flag.'''
        if self.moving_right:
            self.image_fix()
            if self.dx < 20:
                self.dx += 1
        if self.moving_left:
            self.image_fix()
            if self.dx > -20:
                self.dx += -1
        if self.moving_up:
            self.image_fix()
            if self.dy > -20:
                self.dy += -1
        if self.moving_down:
            self.image_fix()
            if self.dy < 20:
                self.dy += 1

        self.movement_decay()

    def movement_decay(self):
        '''Causes the movement of the ship in the right, left, up, or down direction if those keys aren't being pressed.'''
        if self.moving_right == False:
            if self.dx > 0:
                self.dx += -.2
        if self.moving_left == False:
            if self.dx < 0:
                self.dx += .2
        if self.moving_up == False:
            if self.dy < 0:
                self.dy += .2
        if self.moving_down == False:
            if self.dy > 0:
                self.dy += -.2

    def image_fix(self):
        '''Fixes the background of the ship image. Done to satisfy TIY 12-2'''
        image_pixel_array = pygame.PixelArray(self.image)
        image_pixel_array.replace((255,255,255),self.settings.bg_color)

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)