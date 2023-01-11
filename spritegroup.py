import pygame
import sys
from pygame.locals import *

counter = 0

dis_width = 500
dis_height = 500

dis = pygame.display.set_mode((dis_width, dis_height))

sprite1 = pygame.image.load("flappy_bird-sprites/img/bird1.png")
sprite2 = pygame.image.load("flappy_bird-sprites/img/bird3.png")
sprites = pygame.sprite.Group()
sprites.add(sprite1)
sprites.add(sprite2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if counter >= 2:
        print(sprites[1])
