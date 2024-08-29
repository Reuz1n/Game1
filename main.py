import pygame
import random 
import sys

<<<<<<< Updated upstream
=======
class Entity:
    
    
    def __init__(self, pos_x, pos_y, health):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = health
    
    
class Player(Entity):
    
    speed = 0,3
    
    def __init__(self ):
        super().__init__(336, 236, 3)
        
        
    def play_now(self):
        window.blit((self.pos_x ,self.pos_y))
        
        
        
        

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("NAVECITAS LOCURA")
icon = pygame.image.load("Game1\Images\icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("Game1\Images\wallpaper.jpg")

    
player1 = Player()


 

while True:

    player1.play_now()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    pygame.display.update()