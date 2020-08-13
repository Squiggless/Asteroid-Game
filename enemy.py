import pygame
import random

class Enemy(pygame.sprite.Sprite):
	def __init__(self, image_name, scale):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()

		self.image = pygame.transform.scale(self.image,(int(scale*self.rect.width), int(scale*self.rect.height)))
		self.rect = self.image.get_rect()
		x = random.randint(70, 800)
		y = random.randint(0, 600)
		self.rect.center = (x, y)
		# making sure enemy stays on screen
		if self.rect.right > 800:
			self.rect.right = 800
		if self.rect.left < 70: 
			self.rect.left = 70
		if self.rect.top < 0: 
			self.rect.top = 0
		if self.rect.bottom > 600:
			self.rect.bottom = 600
		self.speed = pygame.math.Vector2(0,5)
		rotation = random.randint(0, 360)
		self.speed.rotate_ip(rotation)
	def update(self):
		self.rect.move_ip(self.speed)
		if self.rect.right > 800 or self.rect.left < 80:
			self.speed[0] *= -1
		if self.rect.top < 0 or self.rect.bottom > 600:
			self.speed[1] *= -1
