import sys
import pygame
import random

from settings import Settings
from raindrop import Rain

class RainGame:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initialize the game, and create game resources.'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Rain")

        self.rain = pygame.sprite.Group()
        self._create_rain()

    def run_game(self):
        while True:
            self._check_events()
            self._rain_update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        '''Respond to keyboard and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT recieved")
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        '''Respond to key presses.'''
        if event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        pass

    def _create_rain(self):
        '''Creates the grid of rain.'''
        raindrop = Rain(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        
        current_x, current_y = raindrop_width, raindrop_height
        while current_y < (self.settings.screen_height - raindrop_height):
            while current_x < (self.settings.screen_width - raindrop_width):
                self._create_raindrop(current_x, current_y)
                current_x += 2 * raindrop_width
            
            # Finished a row; reseet x value, and increment y value.
            current_x = raindrop_width
            current_y += 2 * raindrop_height
        
        self._rain_update()
    
    def _create_raindrop(self, x_position, y_position):
        '''Creates the raindrops.'''
        new_raindrop = Rain(self)
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        self.rain.add(new_raindrop)
    
    def _rain_update(self):
        for rain in self.rain:
            rain.rect.y += self.settings.rain_speed

            if rain.rect.top >= self.settings.screen_height:
                self.rain.remove(rain)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rain.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    rain_game = RainGame()
    rain_game.run_game()