import pygame

from game.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.data_counter import counter


class Menu:
    SCREEN_HALF_HEIGHT = SCREEN_HEIGHT / 2
    SCREEN_HALF_WIDTH =  SCREEN_WIDTH / 2

    def __init__(self, screen, message):
        self.reset_screen(screen)
        self.screen = screen
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, False, 'Black')
        self.rect = self.text.get_rect(center = (self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT))
        # self.score = self.font.render('0', False, 'Blue')
        # self.score_height = self.SCREEN_HALF_HEIGHT + 50
        # self.rect2 = self.score.get_rect(center = (self.SCREEN_HALF_WIDTH, self.score_height))
        # self.bigscore = self.font.render('0', False, 'Blue')
        # self.bigscore_height = self.SCREEN_HALF_HEIGHT + 80
        # self.rect3 = self.bigscore.get_rect(center = (self.SCREEN_HALF_WIDTH, self.bigscore_height))
        # self.deaths = self.font.render('0', False, 'Blue')
        # self.deaths_height = self.SCREEN_HALF_HEIGHT + 110
        # self.rect4 = self.bigscore.get_rect(center = (self.SCREEN_HALF_WIDTH, self.deaths_height))
        #self.deaths = 0
        self.helper = counter()

    def update(self, game):
        pygame.display.update()
        self.handle_events(game)

    def draw(self, data, deaths):
        #cosito = 3
        #print("desde el menu")
        if deaths < 1:
            screen.blit(self.text, dest=(self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT))
        else:
            self.helper.show(data, self.screen)

        #self.reset_screen(screen)

    def handle_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            if event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen(self, screen):
        screen.fill('White')

    # def update_message(self, message = 0, score = '0',  bigscore = 0, deaths = 0):
    #     #self.text = self.font.render(message, False, 'Red')
    #     #self.rect = self.text.get_rect(center = (self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT))

    #     #self.score = self.font.render(score, False, 'Blue')
    #     #self.rect2 = self.score.get_rect(center = (self.SCREEN_HALF_WIDTH, (self.SCREEN_HALF_HEIGHT+10)))
        
    #     #self.bigscore = self.font.render(bigscore, False, 'Green')
    #     #self.rect3 = self.bigscore.get_rect(center = (self.SCREEN_HALF_WIDTH, (self.SCREEN_HALF_HEIGHT+20)))

    #     #self.deaths = self.font.render(deaths, False, 'Pink')
    #     #self.deaths = int(deaths)

    #     self.rect4 = self.bigscore.get_rect(center = (self.SCREEN_HALF_WIDTH, (self.SCREEN_HALF_HEIGHT+30)))