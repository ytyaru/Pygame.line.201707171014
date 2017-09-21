#!python3
# coding: utf-8
import sys, pygame
from pygame.locals import *

pygame.init()
screen_size = (320, 240)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("線の描画")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,255,255), (0,0), (100, 100), 8)
    pygame.display.flip()
#    pygame.display.update()
