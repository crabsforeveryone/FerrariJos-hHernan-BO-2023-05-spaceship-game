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
        self.mousex, self.mousey = (0,0)
        self.menu_call = False
        self.helper = counter()

    def update(self, game):
        pygame.display.update()
        #game.events()
        self.handle_events(game)

    def draw(self, screen, data = [], deaths=0):
        #cosito = 3
        #print("desde el menu")
        if deaths < 1 or self.menu_call:
            self.helper.show({"Bienvenido al juego":'Welcome'}, self.screen, 100, 100, position='left')
            self.helper.show({
                "Jugar":'Jugar'
            }, self.screen, 100, SCREEN_HEIGHT / 2, position='left', mouse_x=self.mousex, mouse_y=self.mousey)
            self.helper.show({"Salir":"Salir"}, self.screen, 100, SCREEN_HEIGHT-100, position='left', mouse_x=self.mousex, mouse_y=self.mousey)
   
        elif deaths != 0 and not self.menu_call:
            self.helper.end(self.screen)
            self.helper.show(data, self.screen, self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT+50, position='center')
            self.helper.show({'menu': "Menu"}, screen = self.screen, posx=SCREEN_WIDTH - 100, posy=SCREEN_HEIGHT-100, mouse_x=self.mousex, mouse_y=self.mousey)
            

        #self.reset_screen(screen)

    def handle_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            if event.type == pygame.KEYDOWN:
                game.run()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousex, self.mousey = pygame.mouse.get_pos()
            if self.helper.option == 0:
                game.run()
                self.helper.option = None
            if self.helper.option == 'Salir':
                game.playing = False
                game.running = False
            elif self.helper.option == 'Jugar':
                game.run()
                self.menu_call = False
                self.helper.option = None
            elif self.helper.option == 'Puntuaciones':
                print(game.bigscore)
                self.helper.option = None
                self.menu_call = False
            elif self.helper.option == 'Tienda':
                print("Tienda")
                self.menu_call = False
                self.helper.option = None
            elif self.helper.option == 'Menu':
                self.menu_call = True
                self.reset_screen(self.screen)
                print("vayase al menu")
                self.draw(self.screen)
                pygame.display.update()
                self.helper.option = None
                
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