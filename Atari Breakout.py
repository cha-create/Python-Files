import pygame
from pygame.locals import *
import sys
import random
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
dis_height = 800
dis_width = 800
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.font.init()


def run():
    paddleX = dis_width / 2
    paddleY = dis_height - 50
    ballX = dis_width / 2
    ballY = dis_height / 2
    ballVX = random.randint(-7, 7)
    ballVY = 7
    if ballVX == 0:
        ballVX = -2
    wall1_stat = True
    wall2_stat = True
    wall3_stat = True
    wall4_stat = True
    font = pygame.font.Font(None, 100)
    text = font.render("You won. yay.", False, white)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(60)
        paddleX = pygame.mouse.get_pos()[0] - 50
        paddle = Rect(paddleX, paddleY, 100, 10)
        if ballY >= dis_height:
            run()
        if ballY <= 0:
            ballVY = -ballVY
        if ballX >= dis_width - 5 or ballX <= 0:
            ballVX = -ballVX
        if paddle.collidepoint(ballX, ballY):
            ballVY = -ballVY
        # Render Wall
        wall1 = Rect(20, 100, (dis_width / 4) - 20, 50)
        wall2 = Rect(210, 100, (dis_width / 4) - 20, 50)
        wall3 = Rect(400, 100, (dis_width / 4) - 20, 50)
        wall4 = Rect(590, 100, (dis_width / 4) - 20, 50)
        if wall1_stat == True and wall1.collidepoint(ballX, ballY):
            ballVX = -ballVX
            ballVY = -ballVY
            wall1_stat = False
        if wall2_stat == True and wall2.collidepoint(ballX, ballY):
            ballVX = -ballVX
            ballVY = -ballVY
            wall2_stat = False
        if wall3_stat == True and wall3.collidepoint(ballX, ballY):
            ballVX = -ballVX
            ballVY = -ballVY
            wall3_stat = False
        if wall4_stat == True and wall4.collidepoint(ballX, ballY):
            ballVX = -ballVX
            ballVY = -ballVY
            wall4_stat = False
        ballX += ballVX
        ballY += ballVY
        dis.fill(black)
        if wall1_stat == False and wall2_stat == False and wall3_stat == False and wall4_stat == False:

            for i in range(2000):
                dis.blit(text, ((dis_width / 5), (dis_height / 2)))
                pygame.display.update()
                pygame.time.wait(1)
                print(i)
            run()
        pygame.draw.rect(dis, white, paddle)
        if wall1_stat == False:
            pygame.draw.rect(dis, black, wall1)
        else:
            pygame.draw.rect(dis, red, wall1)
        if wall2_stat == False:
            pygame.draw.rect(dis, black, wall2)
        else:
            pygame.draw.rect(dis, red, wall2)
        if wall3_stat == False:
            pygame.draw.rect(dis, black, wall3)
        else:
            pygame.draw.rect(dis, red, wall3)
        if wall4_stat == False:
            pygame.draw.rect(dis, black, wall4)
        else:
            pygame.draw.rect(dis, red, wall4)
        pygame.draw.circle(dis, green, (ballX, ballY), 10)
        pygame.display.update()


run()
