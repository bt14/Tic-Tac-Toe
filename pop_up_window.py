import pygame

class PopUpWindow():

	def __init__(self, x, y, width, height, text, font, text_color, color, buttons):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.rect = pygame.Rect(x, y, width, height)
		self.text = text
		self.font = font
		self.text_color = text_color
		self.color = color
		self.buttons = buttons # array of buttons
		self.visible = False	# indicates if it should be drawn or not (used in the calling function)
		self.updateMessage()

	def updateMessage(self):
		self.message = self.font.render(self.text, True, self.text_color)			# puts message slightly above pop up's center
		self.message_rect = self.message.get_rect(center=(self.rect.center[0], int(self.rect.center[1]) - 50))

	def draw(self, win):
		self.updateMessage()
		pygame.draw.rect(win, self.color, self.rect)
		win.blit(self.message, self.message_rect)

		for button in self.buttons:
			button.visible = True

		pygame.display.update()

	def close(self):
		self.visible = False
		for button in self.buttons:
			button.visible = False
