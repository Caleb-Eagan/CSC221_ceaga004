import sys
import pygame

from settings import Settings
from rocket_ship import Ship

# Satisfies TIY 12-4

class AlienInvasion:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initialize the game, and create game resources.'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Create the screen
        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        # Create self.ship
        self.ship = Ship(self)
        
    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

            # Always move the ship by dx,dy
            self.ship.rect.x += self.ship.dx
            self.ship.rect.y += self.ship.dy

            # Keep the ship on the screen
            if self.ship.rect.x < 0:
                self.ship.rect.x = 0
                self.ship.dx = 0
            if self.ship.rect.right > self.screen.get_width():
                self.ship.rect.right = self.screen.get_width()
                self.ship.dx = 0
            if self.ship.rect.y < 0:
                self.ship.rect.y = 0
                self.ship.dy = 0
            if self.ship.rect.bottom > self.screen.get_height():
                self.ship.rect.bottom = self.screen.get_height()
                self.ship.dy = 0

            # Now let's speed it up (unless dx == 0)
            #if self.dx < 25:
            #self.dx *= 1.05
            #if self.dx < 30:
            #self.dy *= 1.05

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
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        '''Respond to key releases.'''
        if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            
    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen.'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


