#!python3
# coding: utf-8
import sys, pygame
from pygame.locals import *

pygame.init()
screen_size = (320, 240)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("線の描画")

screen_color = (0,0,0)
line_color = (255,255,255)
line_start = (0,0)
line_end = (100, 100)
line_width = 8
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(screen_color)
    pygame.draw.line(screen, line_color, line_start, line_end, line_width)
    pygame.display.flip()
