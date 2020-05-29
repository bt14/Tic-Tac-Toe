import pygame

class Button:

	def __init__ (self, x, y, width, height, text, font, text_color, idle_color, hover_color, callback_funct, visible):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.rect = pygame.Rect(x, y, width, height)

		self.text = text
		self.label = font.render(text, True, text_color)
		self.label_rect = self.label.get_rect(center=self.rect.center)

		self.idle_color = idle_color
		self.hover_color = hover_color
		self.callback_funct = callback_funct
		self.hovered = False
		self.outlineRect = (x-1, y-1, width+2, height+2)
		self.outlineColor = (0,0,0)  # always black, change this to be a parameter later if needed
		self.visible = visible

	def updateHover(self, mouse_pos):
		self.hovered = False
		if self.rect.collidepoint(mouse_pos):
			self.hovered = True

	# if the mouse is clicked, and the mouse is over the button, 
	# call the corresponding method for the clicked button
	# also makes sure the button is actually visible 
	# (ie its not part of a pop up window thats not actually there yet)
	def get_event(self, event):
		if event.type == pygame.MOUSEBUTTONUP:
			if self.hovered and self.visible:
				self.callback_funct()
				return True
		return False

	def draw(self, win):
		if self.hovered:
			color = self.hover_color
		else:
			color = self.idle_color

		pygame.draw.rect(win, self.outlineColor, self.outlineRect)  
		pygame.draw.rect(win, color, self.rect)
		win.blit(self.label, self.label_rect)
