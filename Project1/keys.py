import pygame
import sys

from settings import Settings

# Made to satisfy TIY 12-5

class Keys:
    def __init__(self):
        '''Initialize the game, and create game resources.'''
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen.fill((self.settings.bg_color))

    def _check_events(self):
        '''Respond to keyboard and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT recieved")
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        '''Respond to key presses.'''
        print(event.key)
        if event.key == pygame.K_q:
            sys.exit()
    
    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen.'''
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()
    
    def run_game(self):
        '''Main loop'''
        while True:
            self._check_events()
            self._update_screen()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    keys = Keys()
    keys.run_game()