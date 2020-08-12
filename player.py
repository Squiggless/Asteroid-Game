import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, image_name, scale, pos):
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()

		self.image = pygame.transform.scale(self.image,(int(scale*self.rect.width), int(scale*self.rect.height)))

		self.rect = self.image.get_rect()
		self.reset(pos)
		self.speed = pygame.math.Vector2(0, 0)
	
	def reset(self, pos):
		self.rect.center = pos

	def move_player(self):
		self.rect.move_ip(self.speed)