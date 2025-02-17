import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.data_counter import counter

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.death_counter = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu(self.screen, "Presione cualquier boton para iniciar")
        self.bigscore = 0
        self.score = 0
        self.power_up_manager = PowerUpManager()
        self.counter = counter()
        

    def execute(self):
        self.running = True
        while self.running and not self.playing:
            self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.score = 0
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.player.reset()
        # Game loop: events - update - draw
        self.playing = True
        self.running = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        release = pygame.KEYUP
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.player.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()

        #esto se ve importante, no lo toques
        pygame.display.update()
        # pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
            
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        
        self.menu.update(self)

        self.menu.reset_screen(self.screen)

        if self.death_counter != 0:
            
            self.menu.draw(
                screen=self.screen, 
                data={
                'Score':f"Your score was: {self.score}",
                'Big Score':f"Your highest score was: {self.bigscore}",
                'Deaths':f"Deaths: {int(self.death_counter / 2)}"
            }, deaths=self.death_counter )
        else:
                self.menu.draw(self.screen)

        
   
        icon = pygame.transform.scale((ICON), (80, 120))
        self.screen.blit(icon, ((SCREEN_WIDTH / 2) - 40, (SCREEN_HEIGHT / 2) - 150))

        #self.menu.draw(self.screen)
        self.menu.update(self)

           
    def increase_death_counter(self):
        self.death_counter += 1

    def increase_score(self):
        self.score += 1
        if self.bigscore < self.score:
            self.bigscore = self.score
    
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', False, 'White')
        text_rect = text.get_rect(topright = (SCREEN_WIDTH - 30, 30))
        self.screen.blit(text, text_rect)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = int((self.player.power_up_time_up - pygame.time.get_ticks())/1000)
            if time_to_show >= 0:
                self.counter.show(data = {'message' : f"remaining time of the power-up: {time_to_show} seconds"}, screen=self.screen, posy=100, color='White' )
                
                # font = pygame.font.Font(FONT_STYLE, 30)
                # self.text = font.render(f'Power: {self.player.power_up_type.capitalize()} Time left: {time_to_show} seconds', False, 'White')
                # self.text_rect = self.text.get_rect(midtop = (SCREEN_WIDTH/2, 100))
                # self.screen.blit(self.text, self.text_rect)
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
            
                