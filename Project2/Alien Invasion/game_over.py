import pygame

class GameOver:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.stats = ai_game.stats
    
    def game_over(self):
        '''Gets triggered when the game ends, which is after the player runs out of lives.'''
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('GeeksForGeeks', True, (0, 255, 0), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (self.settings.screen_width // 2, self.settings.screen_height // 3)
        self.screen.blit(text, textRect)
