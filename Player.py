import pygame
from pygame.locals import *

vec = pygame.math.Vector2

Walk_right = [pygame.image.load("Images/Player_Right.png"),
                   pygame.image.load("Images/Player_RW2.png"),
                   pygame.image.load("Images/Player_RW3.png"),
                   pygame.image.load("Images/Player_RW4.png"),
                   pygame.image.load("Images/Player_RW5.png"),
                   pygame.image.load("Images/Player_RW6.png"),
                   pygame.image.load("Images/Player_RW7.png"),
                   pygame.image.load("Images/Player_RW8.png"),
                   pygame.image.load("Images/Player_RW9.png"),
                   pygame.image.load("Images/Player_RW10.png"),
                   pygame.image.load("Images/Player_end.png"),
                   ]

Walk_left = [pygame.image.load("Images/Player_Left.png"),
                  pygame.image.load("Images/Player_LW2.png"),
                  pygame.image.load("Images/Player_LW3.png"),
                  pygame.image.load("Images/Player_LW4.png"),
                  pygame.image.load("Images/Player_LW5.png"),
                  pygame.image.load("Images/Player_LW6.png"),
                  pygame.image.load("Images/Player_LW7.png"),
                  pygame.image.load("Images/Player_LW8.png"),
                  pygame.image.load("Images/Player_LW9.png"),
                  pygame.image.load("Images/Player_LW10.png"),
                  pygame.image.load("Images/Player_endL.png"),
                  ]

Attack_right = [pygame.image.load("Images/Player_Right.png"),
                pygame.image.load("Images/Player_AR.png")
                ]

Attack_left = [pygame.image.load("Images/Player_Left.png"),
               pygame.image.load("Images/Player_AL.png")
               ]



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Images/Player_Right.png")
        self.rect = pygame.Rect(x, y, 35, 54)

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

        # Player Attacking
        self.attacking = False
        self.attack_frame = 0
        self.attack_counter = 0

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
        if self.move_frame > 10:
            self.move_frame = 0
            return

        if self.jumping == False and self.running == True:
            if self.vel.x >= 0:
                self.image = Walk_right[self.move_frame]
                self.direction = "RIGHT"
            elif self.vel.x < 0:
                self.image = Walk_left[self.move_frame]
                self.direction = "LEFT"
            self.move_frame += 1

        if self.running == False and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = Walk_right[self.move_frame]
            elif self.direction == "LEFT":
                self.image = Walk_left[self.move_frame]

    def attack(self):

        if self.attack_frame > 1:
            self.attack_frame = 0
            return

        if self.direction == "RIGHT":
            self.image = Attack_right[self.attack_frame]
        elif self.direction == "LEFT":
            self.image = Attack_left[self.attack_frame]

        self.attack_frame += 1

    def update(self, group):
        self.attack()
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
        pygame.draw.rect(display, (255, 0, 0), self.rect)
        display.blit(self.image, self.pos)

