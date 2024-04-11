import pygame
# This function is built in to alien_invasion.py
# It triggers once the player runs out of ships / lives

def game_over(self):
        '''Gets triggered when the game ends, which is after the player runs out of lives.'''
        font = pygame.font.Font('fonts/game_over.ttf', 250)
        text = font.render('Game Over', True, (255, 255, 255), (40, 40, 40))
        textRect = text.get_rect()
        textRect.center = (self.settings.screen_width // 2, self.settings.screen_height // 3)
        self.screen.blit(text, textRect)

        font = pygame.font.Font('fonts/game_over.ttf', 150)
        score_string = f"Score: {self.stats.score}"
        score = font.render(score_string, True, (255, 255, 255), (40, 40, 40))
        scoreRect = score.get_rect()
        scoreRect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2)
        self.screen.blit(score, scoreRect)

        quit_text = font.render("Press Q to quit", True, (255, 255, 255), (40, 40, 40))
        quitRect = quit_text.get_rect()
        quitRect.center = (self.settings.screen_width // 2, self.settings.screen_height - 200)
        self.screen.blit(quit_text, quitRect)