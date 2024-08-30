import pygame
import random
import sys

class Entity:

  def __init__(self, pos_x, pos_y, health=None):
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.health = health


class Player(Entity):
  
  # Variables de clase
  speed = 0
  player_icon = pygame.image.load("images\player.png")

  def __init__(self):
    super().__init__(352, 515)

  def move_player(self):
    self.pos_x += self.speed
    window.blit(self.player_icon, (self.pos_x ,self.pos_y))
  
  def set_speed(self, value):
    self.speed = value


class Enemy(Entity): 

  # Variables de clase
  icon = pygame.image.load("images\enemy.png")
  enemies = []  

  def __init__(self, pos_x, pos_y, direction):
    super().__init__(pos_x, pos_y)
    self.direction = direction
    
  def move_enemy(self):
    if self.direction == "right":
        self.pos_x += 5 #borde derechp
        if self.pos_x >= 736:  
            self.direction = "left"
            self.pos_y += 10  # baja 10px abajo
    elif self.direction == "left":
        self.pos_x -= 5      #borde izquierdo
        if self.pos_x <= 0:
            self.direction = "right"
            self.pos_y += 10
        window.blit(self.icon, (self.pos_x, self.pos_y))


# Inicio de juego

pygame.init()

# Variables del juego
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("NAVECITAS LOCURA")
icon = pygame.image.load("images\icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("images\wallpaper.jpg")

# Variables globales 
enemies = [] 
enemies_max = 10
cantity = 5
main_player = Player()
FPS = 60 # Constante FPS

#Loop main
while True:

  # Actualiza el Background
  window.blit(background, (0, 0))
  
  # Reescribe el personaje
  main_player.move_player()

  # Mueve y genera todos los enemigos
  for enemy in enemies:
    enemy.move_enemy()  
    window.blit(enemy.icon, (enemy.pos_x, enemy.pos_y))  

  # Crea y guarda enemigos en la lista si es que no llego al maximo 
  if len(enemies) < enemies_max:
        enemy = Enemy(random.randint(0, 736), random.randint(50, 200), random.choice(["left", "right"]))
        enemies.append(enemy) 


  for event in pygame.event.get():

    if event.type == pygame.QUIT: sys.exit() # Cierra el juego

    # Logica de movimiento
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        main_player.set_speed(-5)
      if event.key == pygame.K_RIGHT:
        main_player.set_speed(5)
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT and main_player.speed == -5:
        main_player.set_speed(0)
      if event.key == pygame.K_RIGHT and main_player.speed == 5:
        main_player.set_speed(0)
  
  # Evitar que salga de pantalla
  if main_player.pos_x <= 0:
    main_player.pos_x = 0
  elif main_player.pos_x >= 736:
    main_player.pos_x = 736
  
  # Actualiza el juego
  pygame.display.flip()

  pygame.time.Clock().tick(FPS)