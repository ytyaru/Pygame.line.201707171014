#!python3
# coding: utf-8
import sys, pygame
from pygame.locals import *

class Line:
    def __init__(self):
        self.__color =  (255,255,255)
        self.__start = (0,0)
        self.__end = (0, 0)
        self.__width = 8
    def draw(self, screen):
        pygame.draw.line(screen, self.__color, self.__start, self.__end, self.__width)
        if self.__end[0] < 320 and self.__end[1] < 240: self.__end = (self.__end[0]+1, self.__end[1]+1)

pygame.init()
screen_color = (0,0,0)
screen_size = (320, 240)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("線の描画")

line = Line()
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit();
    screen.fill(screen_color)
    line.draw(screen)
    pygame.display.flip()
    clock.tick(60) # 60 FPS

