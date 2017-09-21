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

# ジグザグにアニメーションする
class ZigZag:
    def __init__(self):
        self.__color =  (255,255,255)
        self.__width = 8
        self.__pointlist = [[0,0], [0,0]]
        self.__threshold = 50
        self.__direct = 270 # 左: 0 右: 180 上:90, 下:270 としておく
        self.__count = 0
        self.__step = 1
    def draw(self, screen):
        pygame.draw.lines(screen, self.__color, False, self.__pointlist, self.__width)
        self.__animation()
    def __animation(self):
        if 2 == len(self.__pointlist): coordinate = self.__pointlist[-1]
        else: coordinate = self.__pointlist[-1]
#        else: coordinate = self.__pointlist[-2]
        if self.__direct == 270: # 下
            coordinate[1] += 1
            self.__count += self.__step
            if self.__threshold <= self.__count: self.__count = 0; self.__direct = 180; self.__create_next_line();
#            if self.__get_max_animation() <= coordinate[1]: self.__direct = 180; self.__create_next_line();
        elif self.__direct == 180: # 右
            coordinate[0] += 1
            self.__count += self.__step
            if self.__threshold <= self.__count: self.__count = 0; self.__direct = 270; self.__create_next_line();
#            if self.__get_max_animation() <= coordinate[0]: self.__direct = 270; self.__create_next_line();
    def __create_next_line(self):
        max = self.__get_max_animation()
#        self.__pointlist.append(copy.deepcopy(self.__pointlist[-1]))
#        self.__pointlist.append([max, max])
#    pygame.draw.lines(screen.Screen, (255,255,255), False, [[0, 0], [0, 50], [50, 50], [50, 100], [100, 100], [100, 150]], 5)
#        self.__pointlist.append([max, max])
        if 180 == self.__direct: self.__pointlist.append([max - self.__threshold, max]) # 次は右
        elif 270 == self.__direct: self.__pointlist.append([max, max]) # 次は下
#        elif 270 == self.__direct: self.__pointlist.append([max, max - self.__threshold]) # 次は下
#        self.__pointlist.append([max, max + self.__threshold])
        print(self.__pointlist)
    def __get_max_animation(self):
        return int((len(self.__pointlist) / 2)) * self.__threshold
    """
    def __calc_next(self):
        if self.__direct == 270:
            self.__direct = 180
        if self.__direct == 180:
            self.__direct = 270
    """

pygame.init()
pygame.display.set_caption("線の描画")

screen = Screen()
line = Line()
zig = ZigZag()
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit();
    screen.Fill()
#    line.draw(screen.Screen)
#    pygame.draw.lines(screen.Screen, (255,255,255), False, [[50, 50], [50, 100], [100, 150], [150, 200]], 5)
#    pygame.draw.lines(screen.Screen, (255,255,255), False, [[0, 0], [0, 50], [50, 50], [50, 100], [100, 100], [100, 150]], 5)
#    pygame.draw.aalines(screen.Screen, (255,255,255), False, [[0, 0], [0, 50], [50, 50], [50, 100], [100, 100], [100, 150]], 5)
    zig.draw(screen.Screen)
    pygame.display.flip()
    clock.tick(60) # 60 FPS

