#!python3
# coding: utf-8
import sys, pygame
from pygame.locals import *

class Screen:
    def __init__(self):
        self.__color = (0,0,0)
        self.__size = (320, 240)
        self.__screen = pygame.display.set_mode(self.__size)
    @property
    def Screen(self): return self.__screen
    def Fill(self): self.__screen.fill(self.__color)
    
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
pygame.display.set_caption("線の描画")

screen = Screen()
line = Line()
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit();
    screen.Fill()
    line.draw(screen.Screen)
    pygame.display.flip()
    clock.tick(60) # 60 FPS

