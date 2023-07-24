import pygame
from pygame.sprite import Sprite
import random

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP

class PowerUp(Sprite):
    
    def __init__(self, image, type, result_image = SPACESHIP):
        self.POS_ON_X = random.randint(120, SCREEN_WIDTH -120)
        self.result_image = result_image
        self.image = image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(midtop = (self.POS_ON_X, 0))
        self.type = type
        self.start_time = 0


    def update(self, game_speed, power_ups):
        self.rect.y += game_speed
        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
            power_ups.remove(self) 

    def draw(self,screen):
        screen.blit(self.image, self.rect)
    
    def impact(self, game):
        # power_up.start_time = pygame.time.get_ticks()
        self.start_time = pygame.time.get_ticks()
        game.player.has_power_up = True
        game.player.power_up_type = self.type
        # game.player.power_up_time_up = power_up.start_time + self.duration
        game.player.set_image(self.result_image, (40,60))
