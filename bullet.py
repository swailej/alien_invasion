import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''create a class bullet at the ships position'''
    def __init__(self, ai_game):
        super().__init__()
        #pull in settings from the ai instance.
        self.screen = ai_game.screen 
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #initially create a bullet rect in  top left position (0, 0)
        #Could this be swapped for an image?
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        #put the bullet at the current ship location.
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the position as a float
        self.y = float(self.rect.y)
    
    def update(self):
        """move the bullets up the screen"""
        #update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # update the rect position to match the self.y value.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)    

        





