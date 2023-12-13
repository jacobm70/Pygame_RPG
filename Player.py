import pygame
from pygame.locals import *

vec = pygame.math.Vector2

animation_right = [pygame.image.load("Images/Player_Right.png"),
                   pygame.image.load("Images/Player_RW2.png"),
                   pygame.image.load("Images/Player_RW3.png"),
                   pygame.image.load("Images/Player_RW4.png"),
                   pygame.image.load("Images/Player_RW5.png"),
                   pygame.image.load("Images/Player_RW6.png"),
                   pygame.image.load("Images/Player_RW7.png"),
                   pygame.image.load("Images/Player_RW8.png"),
                   pygame.image.load("Images/Player_end.png"),
                   ]

animation_left = [pygame.image.load("Images/Player_Left.png"),
                  pygame.image.load("Images/Player_LW2.png"),
                  pygame.image.load("Images/Player_LW3.png"),
                  pygame.image.load("Images/Player_LW4.png"),
                  pygame.image.load("Images/Player_LW5.png"),
                  pygame.image.load("Images/Player_LW6.png"),
                  pygame.image.load("Images/Player_LW7.png"),
                  pygame.image.load("Images/Player_LW8.png"),
                  pygame.image.load("Images/Player_endL.png"),
                  ]


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Images/Player_Right.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Player Info
        self.pos = vec(x, y)
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)

        # Player Constants
        self.ACC = 0.2
        self.FRIC = -0.1

        # Player Movements
        self.jumping = False
        self.running = False
        self.direction = "RIGHT"
        self.move_frame = 0

    def move(self):
        self.acc = vec(0, 0.5)

        if abs(self.vel.x) > 0.3:
            self.running = True
        else:
            self.running = False

        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            self.acc.x = -self.ACC
        if keys[K_RIGHT]:
            self.acc.x = self.ACC

        self.acc.x += self.vel.x * self.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.topleft = self.pos

    def walking(self):
        if self.move_frame > 8:
            self.move_frame = 0
            return

        if self.jumping == False and self.running == True:
            if self.vel.x >= 0:
                self.image = animation_right[self.move_frame]
                self.direction = "RIGHT"
            elif self.vel.x < 0:
                self.image = animation_left[self.move_frame]
                self.direction = "LEFT"
            self.move_frame += 1

        if self.running == False and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = animation_right[self.move_frame]
            elif self.direction == "LEFT":
                self.image = animation_left[self.move_frame]

    def update(self, group):
        self.walking()
        self.move()
        self.collision(group)

    def collision(self, group):
        hits = pygame.sprite.spritecollide(self, group, False)

        if self.vel.y > 0:
            if hits:
                lowest = hits[0]

                if self.rect.bottom >= lowest.rect.top:
                    self.pos.y = lowest.rect.top - self.rect.height
                    self.rect.y = lowest.rect.top - self.rect.height
                    self.vel.y = 0
                    self.jumping = False

    def jump(self):
        if self.jumping == False:
            self.jumping = True
            self.vel.y = -7

    def render(self, display):
        display.blit(self.image, self.pos)
