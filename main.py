import random
import pygame

from pygame.locals import *


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
def main():
	while True:
		clock.tick(60)
		screen.blit(background_image, background_rect)
		pygame.display.flip()

main()