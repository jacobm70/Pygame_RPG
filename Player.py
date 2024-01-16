import pygame
from pygame.locals import *

vec = pygame.math.Vector2




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
        self.attack_range = pygame.Rect(0, 0, 0, 0)

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

        if self.pos.x > 540:
            self.pos.x = -20
        elif self.pos.x < -20:
            self.pos.x = 540

        self.rect.topleft = self.pos
        self.rect.x += 12

    def walking(self):
        if self.move_frame > 10:
            self.move_frame = 0
            return

        if self.jumping == False and self.running == True:
            if self.vel.x >= 0:
                self.image = self.animation_right[self.move_frame]
                self.direction = "RIGHT"
            elif self.vel.x < 0:
                self.image = self.animation_left[self.move_frame]
                self.direction = "LEFT"
            self.move_frame += 1

        if self.running == False and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = self.animation_right[self.move_frame]
            elif self.direction == "LEFT":
                self.image = self.animation_left[self.move_frame]

    def attack(self):
        if self.attacking == True:
            if self.direction == "RIGHT":
                self.attack_range = pygame.Rect(self.rect.x + self.rect.width, self.pos.y, 13, self.rect.height)
            elif self.direction == "LEFT":
                self.attack_range = pygame.Rect(self.pos.x, self.pos.y, 13, self.rect.height)

            if self.attack_frame > 7:
                self.attack_frame = 0
                self.attacking = False
                self.attack_range = pygame.Rect(0, 0, 0, 0)
                return

            if self.direction == "RIGHT":
                self.image = self.attack_right[self.attack_frame]
            elif self.direction == "LEFT":
                self.image = self.attack_left[self.attack_frame]

            self.attack_counter += 1
            if self.attack_counter >= 5:
                self.attack_frame += 1

    def update(self, group):
        self.walking()
        self.move()
        self.attack()
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

    def jump(self):
        if self.jumping == False:
            self.jumping = True
            self.vel.y = -7

    def render(self, display):
        # pygame.draw.rect(display, (255, 0, 0), self.rect)
        # pygame.draw.rect(display, (0, 255, 0), self.attack_range)
        display.blit(self.image, self.pos)

    def load_animations(self):
        self.animation_right = [pygame.image.load("Images/Player_Right.png").convert_alpha(),
                           pygame.image.load("Images/Player_RW2.png").convert_alpha(),
                           pygame.image.load("Images/Player_RW3.png").convert_alpha(),
                           pygame.image.load("Images/Player_RW4.png").convert_alpha(),
                           pygame.image.load("Images/Player_RW5.png").convert_alpha(),
                           pygame.image.load("Images/Player_RW6.png").convert_alpha(),
                           pygame.image.load("Images/Player_RW7.png").convert_alpha(),
                           pygame.image.load("Images/Player_RW8.png").convert_alpha(),
                           pygame.image.load("Images/Player_RW9.png").convert_alpha(),
                           pygame.image.load("Images/Player_RW10.png").convert_alpha(),
                           pygame.image.load("Images/Player_end.png").convert_alpha(),
                           ]

        self.animation_left = [pygame.image.load("Images/Player_Left.png").convert_alpha(),
                          pygame.image.load("Images/Player_LW2.png").convert_alpha(),
                          pygame.image.load("Images/Player_LW3.png").convert_alpha(),
                          pygame.image.load("Images/Player_LW4.png").convert_alpha(),
                          pygame.image.load("Images/Player_LW5.png").convert_alpha(),
                          pygame.image.load("Images/Player_LW6.png").convert_alpha(),
                          pygame.image.load("Images/Player_LW7.png").convert_alpha(),
                          pygame.image.load("Images/Player_LW8.png").convert_alpha(),
                          pygame.image.load("Images/Player_LW9.png").convert_alpha(),
                          pygame.image.load("Images/Player_LW10.png").convert_alpha(),
                          pygame.image.load("Images/Player_endL.png").convert_alpha(),
                          ]

        self.attack_right = [pygame.image.load("Images/Player_Right.png").convert_alpha(),
                        pygame.image.load("Images/Player_AR.png").convert_alpha(),
                        pygame.image.load("Images/Player_AR2.png").convert_alpha(),
                        pygame.image.load("Images/Player_AR3.png").convert_alpha(),
                        pygame.image.load("Images/Player_AR4.png").convert_alpha(),
                        pygame.image.load("Images/Player_AR4.png").convert_alpha(),
                        pygame.image.load("Images/Player_AR4.png").convert_alpha(),
                        pygame.image.load("Images/Player_Right.png").convert_alpha()
                        ]

        self.attack_left = [pygame.image.load("Images/Player_Left.png").convert_alpha(),
                       pygame.image.load("Images/Player_AL.png").convert_alpha(),
                       pygame.image.load("Images/Player_AL2.png").convert_alpha(),
                       pygame.image.load("Images/Player_AL3.png").convert_alpha(),
                       pygame.image.load("Images/Player_AL4.png").convert_alpha(),
                       pygame.image.load("Images/Player_AL4.png").convert_alpha(),
                       pygame.image.load("Images/Player_AL4.png").convert_alpha(),
                       pygame.image.load("Images/Player_Left.png").convert_alpha(),
                       ]

