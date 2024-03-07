import sys #tools needed to exit the game.

from time import sleep #set a delay in seconds. 

import pygame # tools to make the game.

from settings import Settings

from game_stats import GameStats #game score and ships left

from scoreboard import Scoreboard

from button import Button #draw a button/text on the screen

from ship import Ship

from bullet import Bullet

from alien import Alien


class AlienInvasion:
    '''Overall class to manage game assets and behavior.'''
    def __init__(self):
        '''Initialize the game and create game resources'''
        pygame.init()
        # This allows pygame to set a consistant framerate for the
        #  game. set the loop time e.g. 0.1 second.
        self.clock = pygame.time.Clock() 
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200, 800)) 
        pygame.display.set_caption("Alien Invasion - Press q to exit")

        #create an instance of the game stats and scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self) # the self argument refers to current 
        #instance of Alien Invasion.
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        #start alien invasion is an inactive state.
        self.game_active = False

        #make a play button instance
        self.play_button = Button(self, "Play")


    def run_game(self):
        """Start the main loop for the game."""
    
        while True:
            # redraw the screen during each pass through the loop
            self._check_event()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets() 
                self._update_aliens()    
                
                
            self._update_screen()
            self.clock.tick(60) #the 60 represent a loop of 60 times 
            #per second.  
               
    def _check_event(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()     
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                     mouse_pos = pygame.mouse.get_pos()
                     self._check_play_button(mouse_pos)
                 
    def _start_game(self):
         """start game with key p if game not active"""
         if  not self.game_active:
                #reset game settings
                self.settings.initialize_dynamic_settings()
                #Reset the game statistics
                self.stats.reset_stats()
                self.game_active = True
                self.sb.prep_score()

                #Get rid of remaining aliens/bullets
                self.aliens.empty()
                self.bullets.empty()

                #Create a new fleet and center the ship
                self._create_fleet()
                self.ship.center_ship()

                #hide the mouse while game active
                pygame.mouse.set_visible(False)

    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
                #reset game settings
                self.settings.initialize_dynamic_settings()
                #Reset the game statistics
                self.stats.reset_stats()
                self.game_active = True
                self.sb.prep_score()

                #Get rid of remaining aliens/bullets
                self.aliens.empty()
                self.bullets.empty()

                #Create a new fleet and center the ship
                self._create_fleet()
                self.ship.center_ship()

                #hide the mouse while game active
                pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
            """respond to keypress down"""
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            #quit game by pressing q    
            elif event.key == pygame.K_q:
                sys.exit() 
            elif event.key == pygame.K_SPACE:
                 self._fire_bullet()
            elif event.key == pygame.K_p:
                 self._start_game()
                      
            

    def _check_keyup_events(self, event): 
            """reponse to key release."""
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False  
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
         """create a new bullet and add it to the bullet group"""
         if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """update bullets position and remove old ones in the group"""         
        self.bullets.update()

        #remove old bullets
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                
                self._check_bullet_alien_collisions()
                
    def _check_bullet_alien_collisions(self):
        """check for any bullets that have hit aliens if so, red rid
          of the bullet and alien. clear remaining bullets and 
          restart fleet if destroy plus speed up"""
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        
        if collisions:
             self.stats.score += self.settings.alien_points
             self.sb.prep_score()
             
        #1st bool keeps bullet destroys all rect in path.
        if not self.aliens:#check if any aliens left
                self.bullets.empty()#no aliens clear 
                self._create_fleet()#create a new fleet
                self.settings.increase_speed()

            

    def _update_aliens(self):
         """check for if alien is at an edge and then update 
         position of all aliens in the fleet"""
         self._check_fleet_edge() #check edges before updating 
         #positions
         self.aliens.update()
         

         #look for alien collision with ship
         if pygame.sprite.spritecollideany(self.ship, self.aliens):
              self._ship_hit()

        #check if any aliens have reached the bottom
         self._check_alien_bottom()

    def _ship_hit(self):
         """Respond to the ship being hit by an alien."""
         if self.stats.ship_left > 0:
            #decrement ships_left.
            self.stats.ship_left -= 1
            

            
            #clear remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            #create a new fleet of aliens and a ship
            self._create_fleet()
            self.ship.center_ship()  


            #pause
            sleep(0.5) 
         else:  
              self.game_active = False  
              pygame.mouse.set_visible(True)
              self.play_button = Button(self, "PLAY AGAIN?") 
              self.play_button.draw_button()
            

    def _create_fleet(self):
         """create the fleet of aliens."""
         #Create an alien an keep adding aliens until no room is left.
         #Spacing between aliens is one alien height and width.
         #spacing between aliens is = alien.width.
         #Make an alien and add it to the group.
         alien = Alien(self)  
         #tuple with rect width, height.
         alien_width, alien_height = alien.rect.size 
        #set the x position to the alien width 
         current_x, current_y = alien_width, alien_height
         while current_y < (self.settings.screen_height -2.8 * alien_height):
            #make new aliens until current_X is two alien widths x margin
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width #space by width x 2 

            current_x = alien_width # reset the row starting point
            current_y += 1.2 * alien_height # space by height x 2

    def _create_alien(self, x_position, y_position):
         """create an alien and place it in the fleet"""
         new_alien = Alien(self) #create the alien.
         new_alien.x = x_position #for movement speed/location
         new_alien.rect.x = x_position #place alien x co-ord.
         new_alien.rect.y = y_position #place alien y co-ord.
         self.aliens.add(new_alien) #add new alien to the group

    def _check_fleet_edge(self):
         """respond appropriately of any aliens have reached
           an edge."""     
         for alien in self.aliens.sprites():
              if alien.check_edges():
                   self._change_fleet_direction()
                   break
    
    def _change_fleet_direction(self): #used in _check_fleet_edge()
         """drop the entire fleet and change the fleet direction."""
         for alien in self.aliens.sprites():
              alien.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1   

    def _check_alien_bottom(self):
         """check if any aliens have reached the screen bottom."""
         for alien in self.aliens.sprites():
              if alien.rect.bottom >= self.settings.screen_height:
                   #same as if ship hit.
                   self._ship_hit()
                   break

    def _update_screen(self):
        """update images on the screen and flip to the new one."""
        self.screen.fill(self.settings.bg_color) #sets background
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme() #update rectangles on screen 
        self.aliens.draw(self.screen)#draw aliens group on the screen. 
        #The draw metod needs one argument, the rect to draw on.

        #Draw the score information.
        self.sb.show_score()

        #Draw a play button if the screen is inactive
        if not self.game_active:
             self.play_button.draw_button()#Draw last to appear over 
             #the screen.
        
        pygame.display.flip()
         

if __name__ == "__main__":
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()  