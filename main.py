import random
import pygame

from pygame.locals import *

from player import Player

pygame.init()

screen_info = pygame.display.Info()
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

background_image = pygame.image.load("astroidBackground.png")
background_rect = background_image.get_rect()
background_image = pygame.transform.scale(background_image, (int(0.5 * background_rect.width), int(0.5 * background_rect.height)))
background_rect = background_image.get_rect()
background_rect.center = (width // 2, height // 2)

player = Player(image_name = "space_ship.png", scale = 0.28, pos = (400, 530))

def main():
	while True:
		clock.tick(60)

		for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_DOWN:
						player.speed[1] = 10
					if event.key == K_UP:
						player.speed[1] = -10
					if event.key == K_LEFT:
						player.speed[0] = -10
					if event.key == K_RIGHT:
						player.speed[0] = 10
				if event.type == KEYUP:
					if event.key == K_DOWN or event.key == K_UP:
						player.speed[1] = 0
					if event.key == K_LEFT or event.key == K_RIGHT:
						player.speed[0] = 0
		player.move_player()
		screen.blit(background_image, background_rect)
		screen.blit(player.image, player.rect)
		pygame.display.flip()

main()