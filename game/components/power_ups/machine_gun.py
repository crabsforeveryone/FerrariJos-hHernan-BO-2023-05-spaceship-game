import pygame

from game.components.power_ups.power_up import PowerUp
from game.utils.constants import MACHINE_GUN_TYPE, MACHINE_GUN

class MachineGun(PowerUp):
    def __init__(self):
        super().__init__(MACHINE_GUN, MACHINE_GUN_TYPE)

    
