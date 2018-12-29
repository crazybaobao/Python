# @Time:2018/12/2413:29
# @Author: wangyun
# 下雪

import pygame
import random

from pygame.examples.prevent_display_stretching import clock

pygame.init()
SIZE = (600, 450)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("下雪了")
background = pygame.image.load('static/images/snow.jpg')

# 定义一个雪花列表
snow = []

# 初始化雪花
for i in range(300):
    x = random.randrange(0, SIZE[0])
    y = random.randrange(0, SIZE[1])
    speedx = random.randint(-1, 2)
    speedy = random.randint(3, 8)
    snow.append([x, y, speedx, speedy])

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0, 0))

    # 雪花列表循环
    for i in range(len(snow)):
        pygame.draw.circle(screen, (255, 255, 255), snow[i][:2], snow[i][3])
        snow[i][0] += snow[i][2]
        snow[i][1] += snow[i][3]

        if snow[i][1] > SIZE[1]:
            snow[i][1] = random.randrange(-50, -10)
            snow[i][0] = random.randrange(0, SIZE[0])

    pygame.display.flip()
    clock.tick(20)
pygame.quit()
