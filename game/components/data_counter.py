import pygame

from game.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT



class counter:
	middle_x = SCREEN_WIDTH / 2
	middle_y = SCREEN_HEIGHT / 2
	def __init__(self):

		

		self.font = pygame.font.Font(FONT_STYLE, 30)
		self.vertical = self.middle_y + 50
		self.option = None
		

	def end(self, screen):
		self.game_over = self.font.render("Game Over: Press any key to restart", False, 'Black')
		self.go_rect = self.game_over.get_rect(center = (self.middle_x, self.middle_y))
		screen.blit(self.game_over, self.go_rect)

	def update(self):
		pygame.display.update()



	def show(self, data, screen, posx = middle_x, posy = middle_y, color = 'Black', position='center', mouse_x=0, mouse_y=0):
		for i in data.values():
			if position == 'center':
				self.message_to_show = self.font.render(str(i), False, color)
				self.rect_to_show = self.message_to_show.get_rect(center = (posx, posy))
				screen.blit(self.message_to_show, self.rect_to_show)
				posy = posy + 30
				if self.rect_to_show.collidepoint(mouse_x, mouse_y):
					self.option = i
			elif position == 'left':
				self.message_to_show = self.font.render(str(i), False, color)
				self.rect_to_show = self.message_to_show.get_rect(midleft = (posx, posy))
				screen.blit(self.message_to_show, self.rect_to_show)
				posy = posy + 30

				if self.rect_to_show.collidepoint(mouse_x, mouse_y):
					self.option = i
	