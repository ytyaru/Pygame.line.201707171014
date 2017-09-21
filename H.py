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

# 指定した頂点リストに応じた等速直線アニメーションをする
class LinesAnimation:
    def __init__(self, pointlist, width=320, height=240):
        if len(pointlist) < 2: raise Exception('pointlistは少なくとも2つ以上の座標を入れて下さい。例: [[0,0], [0,50]]')
        self.__width = width
        self.__height = height
        self.__color =  (255,255,255)
        self.__width = 8
        self.__pointlist = pointlist
        
        self.__now_pointlist_index = 1
        self.__now_pointlist = [copy.deepcopy(self.__pointlist[0]), copy.deepcopy(self.__pointlist[0])]
        self.__frame = 0
        self.__frame_max = 0
        self.__frame_target = 0
        self.__anime_direct_x = 0
        self.__anime_direct_y = 0
        self.__get_frame_target()
        print(self.__pointlist)
    def draw(self, screen):
        pygame.draw.lines(screen, self.__color, False, self.__now_pointlist, self.__width)
        self.__animation()
    def __animation(self):
#        print(self.__now_pointlist_index, len(self.__pointlist))
        if self.__now_pointlist_index < len(self.__pointlist):
            self.__move()
            self.__set_frame()
    # 移動
    def __move(self):
        rate = self.__frame / self.__frame_max
        if 0 == self.__frame_target:
            self.__now_pointlist[-1][0] = int(self.__pointlist[self.__now_pointlist_index-1][0] + abs(self.__pointlist[self.__now_pointlist_index][0] - self.__pointlist[self.__now_pointlist_index-1][0]) * rate)
            self.__now_pointlist[-1][1] = int(self.__pointlist[self.__now_pointlist_index-1][1] + abs(self.__pointlist[self.__now_pointlist_index][1] - self.__pointlist[self.__now_pointlist_index-1][1]) * rate) 
        else:
            self.__now_pointlist[-1][0] = int(self.__pointlist[self.__now_pointlist_index-1][0] + abs(self.__pointlist[self.__now_pointlist_index][0] - self.__pointlist[self.__now_pointlist_index-1][0]) * rate)
            self.__now_pointlist[-1][1] = int(self.__pointlist[self.__now_pointlist_index-1][1] + abs(self.__pointlist[self.__now_pointlist_index][1] - self.__pointlist[self.__now_pointlist_index-1][1]) * rate)
    def __set_frame(self):
        target = not(self.__frame_target)
        if self.__frame < self.__frame_max: self.__frame += 1
        else: self.__frame = 0; self.__append_next_coordinate()
    # 次の頂点を用意する
    def __append_next_coordinate(self):
        self.__now_pointlist_index += 1
        print(self.__now_pointlist_index, self.__now_pointlist[-1], self.__now_pointlist)
        if self.__now_pointlist_index < len(self.__pointlist):
            self.__now_pointlist.append(copy.deepcopy(self.__pointlist[self.__now_pointlist_index-1]))
            self.__get_frame_target()
    # 差が小さいほうをframeにする(1pixcel/1tick以下にするため)
    def __get_frame_target(self):
        diff_x = (self.__pointlist[self.__now_pointlist_index][0] - self.__pointlist[self.__now_pointlist_index-1][0])
        diff_y = (self.__pointlist[self.__now_pointlist_index][1] - self.__pointlist[self.__now_pointlist_index-1][1])
        self.__anime_direct_x = 1 if 0 < diff_x else -1
        self.__anime_direct_y = 1 if 0 < diff_y else -1
        self.__frame_target = 1 if abs(diff_x) < abs(diff_y) else 0
        self.__frame_max = abs(diff_y) if diff_x < diff_y else abs(diff_x)
        print(self.__frame_max)
        
pygame.init()
pygame.display.set_caption("2頂点間の等速直線アニメーション")
screen = Screen()
#lineanim = LineAnimation()
#lineanim = LineAnimation(start=[50,50], end=[200,400])
#lineanim = LinesAnimation([[0, 0], [10, 50], [50, 50], [70, 100], [100, 100], [100, 150], [150, 150], [150, 200], [200, 200], [200, 250], [250, 250], [250, 300], [300, 300], [300, 350], [350, 350], [350, 400], [400, 400], [400, 450], [400, 450]])
lineanim = LinesAnimation([[0, 0], [10, 50], [50, 50], [70, 100], [100, 100], [100, 150], [150, 150], [150, 200], [200, 200], [200, 250]])
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit();
    screen.Fill()
    lineanim.draw(screen.Screen)
    pygame.display.flip()
    clock.tick(60) # 60 FPS
