import pygame

import time

class Ship():
    """A class to manage the ship."""
    def __init__(self, ai_game): #to ref the AlienInvader instance.
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()#background rect
        self.settings = ai_game.settings # ship settings from main 
        # settings.

        #Load the ship and get it's rectangle (rect)
        self.image = pygame.image.load('images\spiked_ship.bmp') #image file
        self.rect = self.image.get_rect() # image surface rectangle.

        #game over notice
        self.end_game = pygame.image.load('images\game_over.bmp')
        self.sign = self.end_game.get_rect()
        self.sign.center = self.screen_rect.center


        #Start each new ship at the bottom centre of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; set to False so stationary by default
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on the  flag"""
        #The below is based on the x float value not the rect.x
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Move the ship to the right 
            self.x += self.settings.ship_speed 

            # Move the ship to the right
        if  self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed   

        # Update rect object from self.x
        self.rect.x = self.x    

    def center_ship(self):
        """Center the ship on the screen. This create a new rect but
        not a new ship intance (e.g. Ship(self) as this would reset 
        the stats."""
        #Start each new ship at the bottom centre of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)


    def blitme(self): 
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect) 

    
       
        

