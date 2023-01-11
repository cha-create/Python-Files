import sys
import os
import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
dis_height = 936
dis_width = 864
dis = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()
spacebarPressed = False
xpos = (dis_width / 2)
ypos = (dis_width / 2)
scrollSpeed = 4
groundXPos = 0
bg = pygame.image.load(os.path.join("E:\\users\Boing\Documents\\Python\\random\\flappy_bird-sprites", "bg.png"))
bird = pygame.image.load(os.path.join("E:\\users\Boing\Documents\\Python\\random\\flappy_bird-sprites", "bird1.png"))
ground = pygame.image.load(os.path.join("E:\\Users\Boing\Documents\\Python\\random\\flappy_bird-sprites", "ground.png"))
birdFlap = pygame.image.load(os.path.join("E:\\Users\Boing\Documents\\Python\\random\\flappy_bird-sprites", "bird3.png"))
pipe = pygame.image.load(os.path.join("E:\\users\Boing\Documents\\Python\\random\\flappy_bird-sprites", "pipe.png"))
birdRect = bird.get_rect()
yDelta = 0.5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                spacebarPressed = True
        if event.type == pygame.KEYUP:
            if event.key == K_SPACE:
                spacebarPressed = False
    dis.blit(bg, (0, 0))
    dis.blit(ground, (groundXPos, bg.get_height()))
    if spacebarPressed == True:
        dis.blit(bird, (xpos, ypos))
    else:
        dis.blit(birdFlap, (xpos, ypos))
     
    if ypos >= (bg.get_height() - bird.get_height()):
        ypos = (bg.get_height() - bird.get_height())
        yDelta = 0
    if spacebarPressed == True:
        yDelta = -10
    if yDelta >= 8:
        yDelta = 8
    if abs(groundXPos) >= (ground.get_width() - bg.get_width()):
        groundXPos = 0
    yDelta += 0.5
    ypos += yDelta
    groundXPos -= scrollSpeed
    clock.tick(60)
    pygame.display.update()
    dis.fill(BLACK)
