import pygame
from pygame.locals import *
import sys


from Ground import Ground
from Player import Player
from Enemy import Enemy
from UserInterface import UserInterface


# Begin Pygame
pygame.init()


WIDTH = 580
HEIGHT = 380
FPS = 24
CLOCK = pygame.time.Clock()


display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame RPG")

background = pygame.image.load("Images/background.png")

ground = Ground(600, 300, 0, 250, "Images/Ground.png")
player = Player(200, 150)
player.load_animations()

E1 = Enemy()
UI = UserInterface()

EnemyGroup = pygame.sprite.Group()
EnemyGroup.add(E1)


GroundGroup = pygame.sprite.Group()
GroundGroup.add(ground)


while 1:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == player.hit_cooldown_event:
            player.hit_cooldown = True
            pygame.time.set_timer(player.hit_cooldown_event, 0)
            print("Cooldown off")

        if event.type == MOUSEBUTTONDOWN:
            pass

        if event.type == KEYDOWN:
            if event.key == K_UP:
                player.jump()
            if event.key == K_z:
                player.attacking = True
                player.attack()

    # Update Functions
    for enemy in EnemyGroup:
        enemy.update(GroundGroup, player)
    player.update(GroundGroup)
    UI.update()

    player.move()
    player.collision(GroundGroup)

    # Render Functions
    display.blit(background, (0, 0))
    ground.render(display)
    player.render(display)
    UI.render(display)

    for enemy in EnemyGroup:
        enemy.render(display)

    pygame.display.update()
    CLOCK.tick(FPS)
