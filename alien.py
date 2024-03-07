import pygame

from pygame.sprite import Sprite



class Alien(Sprite):
    """A class to represent a single alien in fleet."""
    def __init__(self, ai_game):
        """initialize an alien and set it's starting position"""
        super().__init__()
        #pull in settings from the ai_game instance
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the alien image and set it's rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()#set rectangle for image.

        #start each alien on the top left of the screen separated by 
        #a space = to the rect width and height.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's position as a float for exact speed.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """return true id alien is at edge of screen."""
        screen_rect = self.screen.get_rect() #get screen rectangle
        return (self.rect.right >= screen_rect.right or \
                self.rect.left <= screen_rect.left)

        
    def update(self):
            """move the alien to the left or right"""
            self.x += self.settings.alien_speed * \
            self.settings.fleet_direction
            self.rect.x = self.x

    
        

    
