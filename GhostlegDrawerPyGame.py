import sys, pygame
import Ghostleg
# あみだくじを描画する（1Byte文字。横線はハイフン）
class GhostlegDrawerPyGame:
    class Screen:
        def __init__(self):
            self.__color = (0,0,0)
            self.__size = (320, 240)
            self.__screen = pygame.display.set_mode(self.__size)
        @property
        def Screen(self): return self.__screen
        @property
        def Size(self): return self.__size
        def Fill(self): self.__screen.fill(self.__color)

    def __init__(self, ghostleg):
#    def __init__(self, ghostleg=None):
        self.__leg = None
        self.__ghostleg = ghostleg
        pygame.init()
        pygame.display.set_caption("あみだくじ描画")
        self.__screen = GhostlegDrawerPyGame.Screen()
        self.__clock = pygame.time.Clock()
        self.__width = 8
        self.__color = (255,255,255)
        self.__to_goal_pointlist = None # ゴールまでの頂点リスト（self.__legから生成する）
        self.__select_line_color = (255,0,0)
        self.__select_line_width = 2
#        print(pygame.font.get_fonts()) # 使えるフォント名

    def Select(self, select_line_index):
        if len(self.__ghostleg.Ghostleg) < select_line_index: raise Exception('select_line_indexは {} 以下にして下さい。'.format(len(self.__ghostleg.Ghostleg)))
        self.__create_to_goal_pointlist(select_line_index)
    
    # あみだくじを描画する
    def Draw(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit();
            self.__screen.Fill()
            self.__draw_vartical_lines()
            self.__draw_horizon_lines()
            self.__draw_goals()
            self.__draw_select_lines()
            pygame.display.flip()
            self.__clock.tick(60) # 60 FPS

    def __draw_vartical_lines(self):
        for xi in range(len(self.__ghostleg.Ghostleg)+1):
            start = (20 + xi * 40, 20)
            end = (20 + xi * 40, self.__screen.Size[1] - 40)
            pygame.draw.line(self.__screen.Screen, self.__color, start, end, self.__width)

    def __draw_goals(self):
        font = pygame.font.Font("/usr/share/fonts/truetype/migmix/migmix-1m-regular.ttf", 12)
        for i in range(len(g.Goals)):
            self.__screen.Screen.blit(font.render(g.Goals[i], False, self.__color), (20 + i * 40, self.__screen.Size[1] - 40))
    def __draw_horizon_lines(self):
        for yi in range(len(self.__ghostleg.Ghostleg[0])):
            for xi in range(len(self.__ghostleg.Ghostleg)):
                if 1 == self.__ghostleg.Ghostleg[xi][yi]:
                    start = (20 + xi * 40, 20 + (yi+1) * 24)
                    end = (20 + (xi+1) * 40, 20 + (yi+1) * 24)
                    pygame.draw.line(self.__screen.Screen, self.__color, start, end, self.__width)

    # 選択肢からゴールまでの頂点リストを生成する
    def __create_to_goal_pointlist(self, select_line_index):
        self.__to_goal_pointlist = None
        self.__to_goal_pointlist = []
        now_line_index = select_line_index
        x = self.__get_leg_index_first_horizon_line(now_line_index, 0)
        self.__to_goal_pointlist.append([20 + now_line_index * 40, 20])
        for y in range(len(self.__ghostleg.Ghostleg[0])):
            if 0 == now_line_index:
                if 1 == self.__ghostleg.Ghostleg[now_line_index][y]: # └
                    self.__to_goal_pointlist.append([20 + now_line_index * 40, 20 + ((y+1) * 24)])
                    self.__to_goal_pointlist.append([20 + (now_line_index+1) * 40, 20 + ((y+1) * 24)])
                    now_line_index += 1
                else: # │
                    self.__to_goal_pointlist.append([20 + now_line_index * 40, 20 + (y+1) * 24])
                    self.__to_goal_pointlist.append([20 + now_line_index * 40, 20 + (y+2) * 24])
            elif len(self.__ghostleg.Ghostleg) == now_line_index:
                if 1 == self.__ghostleg.Ghostleg[now_line_index-1][y]: # ┘
                    self.__to_goal_pointlist.append([20 + now_line_index * 40, 20 + ((y+1) * 24)])
                    self.__to_goal_pointlist.append([20 + (now_line_index-1) * 40, 20 + ((y+1) * 24)])
                    now_line_index += -1
                else: # ｜
                    self.__to_goal_pointlist.append([20 + now_line_index * 40, 20 + (y+1) * 24])
                    self.__to_goal_pointlist.append([20 + now_line_index * 40, 20 + (y+2) * 24])
                print('aaaaaaaaaaaaaa')
            else:
                if 1 == self.__ghostleg.Ghostleg[now_line_index][y]: # └
                    self.__to_goal_pointlist.append([20 + now_line_index * 40, 20 + ((y+1) * 24)])
                    self.__to_goal_pointlist.append([20 + (now_line_index+1) * 40, 20 + ((y+1) * 24)])
                    self.__to_goal_pointlist.append([20 + (now_line_index+1) * 40, 20 + ((y+2) * 24)])
                    now_line_index += 1
                elif 1 == self.__ghostleg.Ghostleg[now_line_index-1][y]: # ┘                
                    self.__to_goal_pointlist.append([20 + now_line_index * 40, 20 + ((y+1) * 24)])
                    self.__to_goal_pointlist.append([20 + (now_line_index-1) * 40, 20 + ((y+1) * 24)])
                    self.__to_goal_pointlist.append([20 + (now_line_index-1) * 40, 20 + ((y+2) * 24)])
                    now_line_index += -1
                else: # ｜
                    self.__to_goal_pointlist.append([20 + now_line_index * 40, 20 + (y+1) * 24])
                    self.__to_goal_pointlist.append([20 + now_line_index * 40, 20 + (y+2) * 24])
        self.__to_goal_pointlist.append([self.__to_goal_pointlist[-1][0], self.__screen.Size[1] - 40])
        print(self.__to_goal_pointlist)
        return self.__to_goal_pointlist
    def __get_leg_index_first_horizon_line(self, now_line_index, horizon_start_index):
        if 0 == now_line_index: return now_line_index
        elif len(self.__ghostleg.Ghostleg) == now_line_index: return now_line_index-1
        else:
            for h in range(horizon_start_index, len(self.__ghostleg.Ghostleg[0])):
                if 1 == self.__ghostleg.Ghostleg[now_line_index][h]:return now_line_index
                elif 1 == self.__ghostleg.Ghostleg[now_line_index-1][h]: return now_line_index-1
            return now_line_index # 左右のlegとも横線が1本もない場合
    def __draw_select_lines(self):
        if self.__to_goal_pointlist:
            pygame.draw.lines(self.__screen.Screen, self.__select_line_color, False, self.__to_goal_pointlist, self.__select_line_width)
            
    """
    def __select_animation(self):
        
#        pygame.draw.lines(screen, self.__color, False, self.__pointlist, self.__width)
    """



g = Ghostleg.Ghostleg()
g.Create()
drawer = GhostlegDrawerPyGame(g)
for i in range(len(g.Goals)): print(i, g.GetGoal(i))
drawer.Select(0)
drawer.Draw()

