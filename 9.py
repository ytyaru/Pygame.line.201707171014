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

# 指定した頂点リストに応じた等速直線アニメーションをする
class LinesAnimation:
    def __init__(self, pointlist, width=320, height=240):
        if len(pointlist) < 2: raise Exception('pointlistは少なくとも2つ以上の座標を入れて下さい。例: [[0,0], [0,50]]')
        self.__width = width
        self.__height = height
        self.__color =  (255,255,255)
        self.__width = 8
        self.__pointlist = pointlist
        self.__threshold = 50
        self.__direct = 270 # 左: 0 右: 180 上:90, 下:270 としておく
        self.__count = 0
        self.__step = 1
        
        self.__now_pointlist_index = 1
        self.__now_pointlist = [copy.deepcopy(self.__pointlist[0]), copy.deepcopy(self.__pointlist[0])]
        self.__step_x = 0
        self.__step_y = 0
        self.__set_next_animation_state()
    def draw(self, screen):
        pygame.draw.lines(screen, self.__color, False, self.__now_pointlist, self.__width)
        self.__animation()
    def __animation(self):
        self.__move()
    # 移動
    def __move(self):
        if self.__now_pointlist[-1][0] < self.__pointlist[self.__now_pointlist_index][0]:
            self.__now_pointlist[-1][0] += self.__step_x
        if self.__now_pointlist[-1][1] < self.__pointlist[self.__now_pointlist_index][1]:
            self.__now_pointlist[-1][1] += self.__step_y
        # 次の頂点を用意する
        self.__append_next_coordinate()
    # 次の頂点を用意する
    def __append_next_coordinate(self):
        if self.__pointlist[self.__now_pointlist_index][0] <= self.__now_pointlist[-1][0] and self.__pointlist[self.__now_pointlist_index][1] <= self.__now_pointlist[-1][1]:
            self.__now_pointlist_index += 1
            self.__now_pointlist.append(copy.deepcopy(self.__now_pointlist[-1]))
            self.__set_next_animation_state()
    # 次のアニメーションの移動方向(量)を決める
    def __set_next_animation_state(self):
        prev = self.__pointlist[self.__now_pointlist_index-1]
        now = self.__pointlist[self.__now_pointlist_index]
        if prev[0] < now[0]: self.__step_x = 1
        elif prev[0] > now[0]: self.__step_x = -1
        else: self.__step_x = 0
        if prev[1] < now[1]: self.__step_y = 1
        elif prev[1] > now[1]: self.__step_y = -1
        else: self.__step_y = 0

pygame.init()
pygame.display.set_caption("ジグザグ線のアニメーション")

screen = Screen()
line = Line()
lineanim = LinesAnimation([[0, 0], [0, 50], [50, 50], [50, 100], [100, 100], [100, 150], [150, 150], [150, 200], [200, 200], [200, 250], [250, 250], [250, 300], [300, 300], [300, 350], [350, 350], [350, 400], [400, 400], [400, 450], [400, 450]])
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit();
    screen.Fill()
    lineanim.draw(screen.Screen)
    pygame.display.flip()
    clock.tick(60) # 60 FPS

