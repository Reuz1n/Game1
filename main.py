import pygame
import random 
import sys

class Entity:


    def __init__(self, pos_x, pos_y, health):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = health


class Player(Entity):

    speed = 0

    player_icon = pygame.image.load("Game1\images\player.png")

    def __init__(self):
        super().__init__(352, 515, 3)


    def move_player(self):
        self.pos_x += self.speed
        window.blit(self.player_icon, (self.pos_x ,self.pos_y))

    
    def set_speed(self, value):
        self.speed = value


class Enemy(Entity): 
    enemy_icon = pygame.image.load("Game1\images\enemy.png")
    
    def __init__(self, pos_x, pos_y ):
        super().__init__(pos_x, pos_y)
    
    def move_enemy(self):
        self.pos_x = random.randint(0,800)
        self.pos_y = random.randint(500,600)
        window.blit(self.pos_x, self.pos_y)
    


pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("NAVECITAS LOCURA")
icon = pygame.image.load("Game1\images\icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("Game1\images\wallpaper.jpg")


main_player = Player()
#enemies = Enemy()

while True:
    window.blit(background, (0, 0))
    
    main_player.move_player()
    #enemies.move_enemy()
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                main_player.set_speed(-0.3)
            if event.key == pygame.K_RIGHT:
                main_player.set_speed(0.3)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and main_player.speed == -0.3:
                main_player.set_speed(0)
            if event.key == pygame.K_RIGHT and main_player.speed == 0.3:
                main_player.set_speed(0)
                
    # no sale de pantalla
    if main_player.pos_x <= 0:
        main_player.pos_x = 0
    elif main_player.pos_x >= 736:
        main_player.pos_x = 736
        
        
    pygame.display.update()