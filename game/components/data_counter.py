import pygame

from game.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT



class counter:
	def __init__(self):

		self.middle_x = SCREEN_WIDTH / 2
		self.middle_y = SCREEN_HEIGHT / 2

		self.font = pygame.font.Font(FONT_STYLE, 30)
		#self.data = data
		self.vertical = self.middle_y + 50

		self.game_over = self.font.render("Game Over: Press any key to restart", False, 'Black')
		self.go_rect = self.game_over.get_rect(center = (self.middle_x, self.middle_y))


	def update(self):
		pygame.display.update()



	def show(self, data, screen):
		screen.blit(self.game_over, self.go_rect)
		for i in range(len(data)):
			self.message_to_show = self.font.render(str(data[i]), False, 'Black')
			self.rect_to_show = self.message_to_show.get_rect(center = (self.middle_x, self.vertical))
			screen.blit(self.message_to_show, self.rect_to_show)
			self.vertical = self.vertical + 30
		self.vertical = self.middle_y + 50
