class Settings:
    '''A class to store all settings for Alien Invasion.'''

    def __init__(self):
        '''Initialize the game's settings.'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 750
        self.fullscreen = False
        self.bg_color = (100, 200, 249) # Blue sky for TIY 12-1

        # Bullet settings
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 50

        # Alien settings
        self.alien_speed = 10
        self.fleet_drop_speed = 10
        # fleet direcction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Ship settings
        self.ship_limit = 1