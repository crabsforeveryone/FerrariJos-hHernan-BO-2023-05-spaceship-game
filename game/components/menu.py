import pygame

from game.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    SCREEN_HALF_HEIGHT = SCREEN_HEIGHT / 2
    SCREEN_HALF_WIDTH =  SCREEN_WIDTH / 2

    def __init__(self, screen, message):
        self.reset_screen(screen)
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, False, 'Black')
        self.rect = self.text.get_rect(center = (self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT))
        self.score = self.font.render('0', False, 'Blue')
        self.score_height = self.SCREEN_HALF_HEIGHT + 50
        self.rect2 = self.score.get_rect(center = (self.SCREEN_HALF_WIDTH, self.score_height))
        self.bigscore = self.font.render('0', False, 'Blue')
        self.bigscore_height = self.SCREEN_HALF_HEIGHT + 80
        self.rect3 = self.bigscore.get_rect(center = (self.SCREEN_HALF_WIDTH, self.bigscore_height))
        self.deaths = self.font.render('0', False, 'Blue')
        self.deaths_height = self.SCREEN_HALF_HEIGHT + 110
        self.rect4 = self.bigscore.get_rect(center = (self.SCREEN_HALF_WIDTH, self.deaths_height))


    def update(self, game):
        pygame.display.update()
        self.handle_events(game)

    def draw(self, screen, score = 0, bigscore = 0, deaths = 0):
        screen.blit(self.text, self.rect)
        screen.blit(self.score, self.rect2)
        screen.blit(self.bigscore, self.rect3)
        screen.blit(self.deaths, self.rect4)



    def handle_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            if event.type == pygame.KEYDOWN:
                game.run()

    def reset_screen(self, screen):
        screen.fill('White')

    def update_message(self, message, score = '0',  bigscore = 0, deaths = 0):
        self.text = self.font.render(message, False, 'Red')
        #self.rect = self.text.get_rect(center = (self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT))

        self.score = self.font.render(score, False, 'Blue')
        #self.rect2 = self.score.get_rect(center = (self.SCREEN_HALF_WIDTH, (self.SCREEN_HALF_HEIGHT+10)))
        
        self.bigscore = self.font.render(bigscore, False, 'Green')
        #self.rect3 = self.bigscore.get_rect(center = (self.SCREEN_HALF_WIDTH, (self.SCREEN_HALF_HEIGHT+20)))

        self.deaths = self.font.render(deaths, False, 'Pink')
        #self.rect4 = self.bigscore.get_rect(center = (self.SCREEN_HALF_WIDTH, (self.SCREEN_HALF_HEIGHT+30)))


        