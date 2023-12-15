import pygame
from pygame.locals import *
import sys

from Ground import Ground
from Player import Player


# begin pygame
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

GroundGroup = pygame.sprite.Group()
GroundGroup.add(ground)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            pass

        if event.type == KEYDOWN:
            if event.key == K_UP:
                player.jump()
            if event.key == K_z:
                player.attacking = True
                player.attack()

    player.update(GroundGroup)

    player.move()
    player.collision(GroundGroup)

    display.blit(background, (0, 0))
    ground.render(display)
    player.render(display)

    pygame.display.update()
    CLOCK.tick(FPS)
