import sys
import pygame

from settings import Settings
from sideways_ship import Ship
from sideways_bullet import Bullet

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

        # Create self.ship and self.bullet
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

            # Always move the ship by dx,dy
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
            self.ship.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_up = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        '''Respond to key releases.'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_up = False
            
    def _fire_bullet(self):
        '''Create a new bullet ad add it to the bullets group.'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''Update position of bullets and get rid of old bullets.'''
        # Update bullet position.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen.'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


