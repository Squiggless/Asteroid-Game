import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, image_name, scale):
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()

		self.image = pygame.transform.scale(self.image,(int(scale*self.rect.width), int(scale*self.rect.height)))

		self.rect = self.image.get_rect()