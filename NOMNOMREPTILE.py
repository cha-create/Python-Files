import pygame
from pygame.locals import *
import random
import sys

pygame.init()

green = (0, 255, 0)
blue = (0, 0, 255)

dis_height = 800
dis_width = 800

dis = pygame.display.set_mode((dis_width, dis_height))


def run():
    x1 = dis_width / 2
    y1 = dis_height / 2
    snake_list = []
    snake_length = 1
    direc = [0, 0]
    foodx = 120
    foody = 120
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direc = [0, -10]
                if event.key == pygame.K_RIGHT:
                    direc = [10, 0]
                if event.key == pygame.K_DOWN:
                    direc = [0, 10]
                if event.key == pygame.K_LEFT:
                    direc = [-10, 0]

        dis.fill(blue)
        x1 += direc[0]
        y1 += direc[1]
        clock.tick(10)
        snake_list.append([x1, y1])

        pygame.draw.rect(dis, green, [foodx, foody, 10, 10])
        if snake_list[0][0] == foodx and snake_list[0][1] == foody:
            foody = round(random.randrange(0, dis_height - 10) / 10) * 10
            foodx = round(random.randrange(0, dis_height - 10) / 10) * 10
            snake_length += 1

        if len(snake_list) > snake_length:
            del snake_list[0]

        if ([x1, y1] in snake_list[:-1]):
            run()

        for x in snake_list:
            pygame.draw.rect(dis, green, [x[0], x[1], 10, 10])

        if x1 <= 0 or x1 >= dis_width - 10:
            run()
        if y1 <= 0 or y1 >= dis_height - 10:
            run()

        pygame.display.update()


run()
