import pygame

class Tetris():

      # 全局变量

      # 窗口宽度
      WINDOW_WIDTH=640

      # 窗口高度
      WINDOW_HIGHT=480

      # 方块尺寸
      BOX_SIZE=20

      #游戏窗口本身有10个方块的宽度
      BOARD_WIDTH = 10

      #游戏窗口本身有20个方块的高度
      BOARD_HEIGHT = 20
      

      def __init__(self):
            pygame.init()
            

