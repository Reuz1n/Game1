import pygame
import random

<<<<<<< Updated upstream
=======
class Entity:
    
    
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    
class Player(Entity):
    
    speed = 0,3
    
    def __init__(self ):
        super().__init__(336, 236)
        
        
    def play_now(self):
        window.blit(self.pos_x ,self.pos_y)
        
        
        
        
>>>>>>> Stashed changes

pygame.init()


ventana = pygame.display.set_mode((800, 600))