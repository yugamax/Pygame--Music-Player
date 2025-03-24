import pygame
class Button():
	def __init__(self, x, y, im, p=0):
		if p==1:
			self.image = pygame.transform.scale(im, (150,150))
		else:
			self.image = pygame.transform.scale(im, (50, 50))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, display,s="heyy",p=0):
		font = pygame.font.Font('freesansbold.ttf', 16)
		text = font.render(s, True, (255, 255, 255))
		clk = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				clk = True
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		display.blit(self.image, (self.rect.x, self.rect.y))
		if p==1:
			display.blit(text, (450,220))
		else:
			display.blit(text, (self.rect.x +1 , self.rect.y + 52))
		return clk