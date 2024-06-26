import sys
import pygame
from time import sleep

from sideways_settings import Settings
from game_stats import GameStats
from sideways_ship import Ship
from sideways_bullet import Bullet
from alien import Alien

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

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        # Create self.ship and self.bullet
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Alien Invasion in an active state.
        self.game_active = True
    
        print("i made it to here")
        
    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
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
        
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        '''Respond to bullet-alien collisions.'''
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create a new fleet.
            self.bullets.empty()
            self._create_fleet()
    
    def _check_aliens_bottom(self):
        '''Check if any aliens have reached the bottom of the screen.'''
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _create_fleet(self):
        '''Create the fleet of aliens.'''
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = self.settings.screen_width, self.settings.screen_height
        while current_x > (4 * alien_width):
            while current_y < (self.settings.screen_height - alien_height):
                self._create_alien(current_x, current_y)
                current_y += 2 * alien_width
            
            # Finished a row; reseet x value, and increment y value.
            current_y = alien_height
            current_x -= 2 * alien_width
    
    def _create_alien(self, x_position, y_position):
        '''Create an alien and place it in the fleet.'''
        new_alien = Alien(self)
        new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
    def _check_fleet_edges(self):
        '''Respond appropriately if any aliens have reached an edge.'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        '''Drop the entire fleet and change the fleet's direction'''
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        '''Update the positions of all aliens in the fleet.'''
        self.aliens.update()
        self._check_fleet_edges()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the left of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        '''Respond to the ship being hit by an alien.'''
        # Decrement ships_left.
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        
        else:
            self.game_active = False

    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen.'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


