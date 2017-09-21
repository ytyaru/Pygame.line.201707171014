#!python3
# coding: utf-8
import sys, pygame
from pygame.locals import *

class Line:
    def __init__(self):
        self.__color =  (255,255,255)
        self.__start = (0,0)
        self.__end = (100, 100)
        self.__width = 8
    def draw(self, screen): pygame.draw.line(screen, self.__color, self.__start, self.__end, self.__width)

pygame.init()
screen_color = (0,0,0)
screen_size = (320, 240)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("線の描画")

line = Line()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(screen_color)
    line.draw(screen)
    pygame.display.flip()


