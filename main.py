import pygame
from pygame.locals import *
import sys


from Ground import Ground
from Enemy import Enemy
from Player import Player
from UserInterface import UserInterface
from LeverManager import LevelManager

# Begin Pygame
pygame.init()


WIDTH = 580
HEIGHT = 380
FPS = 24
CLOCK = pygame.time.Clock()


display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame RPG")

background = pygame.image.load("Images/background.png")


player = Player(200, 150)
player.load_animations()

E1 = Enemy()
UI = UserInterface()

Items = pygame.sprite.Group()

levelManager = LevelManager()



EnemyGroup.add(E1)





while 1:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == player.hit_cooldown_event:
            player.hit_cooldown = True
            pygame.time.set_timer(player.hit_cooldown_event, 0)

        if event.type == levelManager.enemy_generation:
            enemy = Enemy()
            levelManager.EnemyGroup.add(enemy)


        if event.type == MOUSEBUTTONDOWN:
            pass

        if event.type == KEYDOWN:
            if event.key == K_PLUS:
                player.jump()
            if event.key == K_z:
                player.attacking = True
                player.attack()
            if event.key == K_q:
                pygame.time.set_timer(levelManager.enemy_generation, 2000)
            if event.key == K_w:
                pygame.time.set_timer(levelManager.enemy_generation, 0)
            if event.key == K_1:
                level.Manager.changeLevel(0)
            if event.key == K_2:
                level.Manager.changeLevel(1)
    # Update Functions
    for enemy in levelManager.enemyGroup:
        enemy.update(levelManager.levels[levelManager.getLevel()].groundData, player, Items)
    player.update(levelManager.levels[levelManager.getLevel()].groundData)
    UI.update()

    player.move()
    player.collision(GroundGroup)

    # Render Functionsz
    display.blit(background, (0, 0))
    ground.render(display)
    for item in Items:
        item.render(display)
        item.update(player)

    player.render(display)
    UI.render(display)

    for enemy in levelManager.enemyGroup:
        enemy.render(display)



    pygame.display.update()
    CLOCK.tick(FPS)
