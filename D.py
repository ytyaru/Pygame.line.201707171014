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

# 始点と終点の線上にある座標点を算出して等速直線アニメーションをする
class LineAnimation:
    def __init__(self, start=[0,0], end=[320,240]):
        self.__color =  (255,255,255)
        self.__start = start
        self.__now = copy.deepcopy(start)
        self.__end = end
        self.__width = 16
        self.__frame_target = 0 # 0:x, 1:y
        self.__frame = 1
        print(self.__start, self.__end, self.__now)
        self.__get_frame_target()
    def draw(self, screen):
        pygame.draw.line(screen, self.__color, self.__start, self.__now, self.__width)
        self.__animation()
    def __animation(self):
        self.__calc_now()
        self.__set_frame()
    def __calc_now(self):
        rate = self.__frame / abs(self.__end[self.__frame_target] - self.__start[self.__frame_target])
        if 0 == self.__frame_target:
            self.__now[0] = self.__start[0] + self.__frame
            self.__now[1] = self.__start[1] + (rate * self.__end[1])
        else:
            self.__now[0] = self.__start[0] + (rate * self.__end[0])
            self.__now[1] = self.__start[1] + self.__frame
    def __set_frame(self):
        if self.__frame < self.__end[0]: self.__frame += 1
        else: self.__frame = 1
    # 差が小さいほうをframeにする(1pixcel/1tick以下にするため)
    def __get_frame_target(self):
        diff_x = (self.__start[0] - self.__end[0])
        diff_y = (self.__start[1] - self.__end[1])
        self.__frame_target = 0 if diff_x < diff_y else 1


pygame.init()
pygame.display.set_caption("2頂点間の等速直線アニメーション")
screen = Screen()
#lineanim = LineAnimation()
#lineanim = LineAnimation(start=[50,50], end=[200,400])
#lineanim = LineAnimation(start=[50,50], end=[400,200])
lineanim = LineAnimation(start=[0,0], end=[320,240])
#lineanim = LinesAnimation([[0, 0], [10, 50], [50, 50], [70, 100], [100, 100], [100, 150], [150, 150], [150, 200], [200, 200], [200, 250], [250, 250], [250, 300], [300, 300], [300, 350], [350, 350], [350, 400], [400, 400], [400, 450], [400, 450]])
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit();
    screen.Fill()
    lineanim.draw(screen.Screen)
    pygame.display.flip()
    clock.tick(60) # 60 FPS
