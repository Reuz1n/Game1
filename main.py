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

    player_icon = pygame.image.load("images\player.png")

    def __init__(self):
        super().__init__(352, 515, 3)


    def move_player(self):
        self.pos_x += self.speed
        window.blit(self.player_icon, (self.pos_x ,self.pos_y))

    
    def set_speed(self, value):
        self.speed = value





pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("NAVECITAS LOCURA")
icon = pygame.image.load("images\icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("images\wallpaper.jpg")


main_player = Player()
 

while True:

    main_player.move_player()

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


    pygame.display.update()