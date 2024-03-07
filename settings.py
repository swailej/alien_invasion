import pygame

class Settings():
    '''This class stores all of the displaysettings for the game'''
    def __init__(self):
        '''Initialize the game's static settings.'''
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
         # We'll set a background color for the screen 
         # RBG 0-255. e.g. 255, 0, 0 is red. The entry is grey.
        self.bg_color = (230, 230, 230)
        # Ship settings
        #number of ships left
        self.ship_limit = 3
        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 6
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30
        #alien setting
        self.fleet_drop_speed = 10  #default 10
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change
        throughout the game."""
        self.ship_speed = 10
        self.bullet_speed = 2.0
        self.alien_speed = 5 #default 1
        #fleet direction of 1 = right and -1 left
        self.fleet_direction = 1

        #Scoring settings
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale



