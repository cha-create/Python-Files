import pygame
import sys
pygame.init()


print("What Number would you like to count to?")
target = input()
count = 0
scrHeight = 500
scrWidth = 500 
running = True
pygame.font.init()

dis = pygame.display.set_mode((scrWidth, scrHeight))
font = pygame.font.SysFont("comicsansms", 72)
text = font.render(str(count), True, (0, 155, 0))

while running:
    dis.fill((255,155,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            count = count + 1
    text = font.render(str(count), True, (0, 155, 0))
    dis.blit(text, (100, 200))
    pygame.display.update()
pygame.quit()
sys.exit()
