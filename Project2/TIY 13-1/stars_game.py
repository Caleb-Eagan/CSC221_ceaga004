import sys
import pygame

from settings import Settings
from stars import Star

class StarsGame:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initialize the game, and create game resources.'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        while True:
            self._check_events()
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

    def _create_stars(self):
        '''Creates the field of stars.'''
        star = Star(self)
        star_width, star_height = star.rect.size
        
        current_x, current_y = star_width, star_height
        while current_y < (self.settings.screen_height - 2 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width
            
            # Finished a row; reseet x value, and increment y value.
            current_x = star_width
            current_y += 2 * star_height
    
    def _create_star(self, x_position, y_position):
        '''Creates a star.'''
        new_star = Star(self)
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    stars_game = StarsGame()
    stars_game.run_game()