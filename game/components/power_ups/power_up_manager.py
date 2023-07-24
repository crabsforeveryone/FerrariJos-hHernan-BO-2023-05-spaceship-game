import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.machine_gun import MachineGun

from game.utils.constants import SPACESHIP_SHIELD

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.available_power_ups = [Shield(), MachineGun()]
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(3000, 5000)
        self.now = 0
        self.has = False
        self.flag_done= False


    def update(self, game):
        current_time = pygame.time.get_ticks()
        self.has = game.player.has_power_up 

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):

                power_up.impact(game)
                game.player.power_up_time_up = power_up.start_time + self.duration
                self.power_ups.remove(power_up)
                self.flag_done = False

    def draw(self, screen):
        if not self.has:
            for power_up in self.power_ups:
               power_up.draw(screen)

    def generate_power_up(self):
        if self.has:
            print("nono")
        elif self.has == False:
            choice = random.choice(self.available_power_ups)
            power_up = choice
            if power_up.rect.y >= 0 and self.flag_done == False:
                power_up.rect.y = 0
                self.flag_done = True
            else:
           
                self.when_appears += random.randint(5000 + self.now , 10000 +  self.now) 
                self.power_ups.append(power_up)
                self.has = True
                print(power_up.rect.x, power_up.rect.y)
                self.flag_done = True

    def reset(self):
        self.now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(self.now + 8000, self.now + 10000)
        self.has = Falseo