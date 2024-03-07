import pygame.font #allow text to be placed on the screen)

class Button:
    """A class to build button for the game."""

    def __init__(self, ai_game, msg):# msg allows us to pass a message.
        """Initialize button attibutes."""
        self.screen = ai_game.screen #save main game rectangle.
        self.screen_rect = self.screen.get_rect()#get the rectangle.

        #set the dimensions and properties of the button.
        self.width, self.height = 220, 70#button size
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)

        #Build the button's rect object and center it.
        self.rect =pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #We only need the button to appear once. Call helper method. 
        self._prep_msg(msg)

    def _prep_msg(self, msg): 
        """Turn msg into a rendered image + center text on  button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)