# P112
import sys

import pygame
# import pip
# print(pip.pep425tags.get_supported())

def run_game():
    # 初始化游戏
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alian Invasion')

    # 设置背景色
    
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sys.exit()
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
