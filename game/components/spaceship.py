import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE, MACHINE_GUN
from game.components.bullets.bullet import Bullet

# la clase Spaceship hereda de Sprite
class Spaceship(Sprite):

    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    SPACESHIP_POS_X = SCREEN_WIDTH / 2
    SPACESHIP_POS_Y = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom = (self.SPACESHIP_POS_X,self.SPACESHIP_POS_Y))
        self.type = 'player'
        self.has_power_up = False
        self.power_up_type = DEFAULT_TYPE
        self.power_up_time_up = 0
        self.long_shot = True

    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.rect.x -= 10
            if self.rect.right == 0:
                self.rect.left = SCREEN_WIDTH
        elif user_input[pygame.K_RIGHT]:
            self.rect.x += 10
            if self.rect.left == SCREEN_WIDTH:
                self.rect.right = 0
        elif user_input[pygame.K_UP] and self.rect.top > 300:
            self.rect.y -= 10
        elif user_input[pygame.K_DOWN] and (self.rect.bottom < SCREEN_HEIGHT-10):
            self.rect.y += 10

        if user_input[pygame.K_o] and self.long_shot:
            self.shoot(game.bullet_manager)
            if self.power_up_type != 'machine_gun':
                self.long_shot = False
        elif pygame.key.get_pressed()[pygame.K_o] == 0 :
            self.long_shot = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def shoot(self, bullet_manager):
    
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)

    def set_image(self, image = SPACESHIP, size = (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    def reset(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom = (self.SPACESHIP_POS_X,self.SPACESHIP_POS_Y))



    