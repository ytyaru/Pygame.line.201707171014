#!python3
# coding: utf-8
import sys, copy, pygame
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

# 始点と終点の線上にある座標点を算出して等速直線アニメーションをする
class LineAnimation:
    def __init__(self, start=[0,0], end=[320,240]):
        self.__color =  (255,255,255)
        self.__start = start
        self.__now = copy.deepcopy(start)
        self.__end = end
        self.__width = 16
        self.__frame_x = 1
    def draw(self, screen):
        pygame.draw.line(screen, self.__color, self.__start, self.__now, self.__width)
        self.__animation()
    def __animation(self):
        self.__calc_now()
        self.__set_frame()
    def __calc_now(self):
        rate = self.__frame_x / self.__end[0]
        self.__now[0] = self.__frame_x
        self.__now[1] = rate * self.__end[1]
    def __set_frame(self):
        if self.__frame_x < self.__end[0]: self.__frame_x += 1
        else: self.__frame_x = 1

pygame.init()
pygame.display.set_caption("2頂点間の等速直線アニメーション")
screen = Screen()
lineanim = LineAnimation()
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit();
    screen.Fill()
    lineanim.draw(screen.Screen)
    pygame.display.flip()
    clock.tick(60) # 60 FPS
