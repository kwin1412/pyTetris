import pygame
import time

# 初始化pygame
pygame.init()

# Pygame窗口
screen = pygame.display.set_mode((800,600)) 

 # 标题
pygame.display.set_caption("Pygame绘制图形")

 # 循环变量标值
keep_going = True

  # 红色，使用RGB颜色
color = [0,0,0]
# 半径
radius = 20 

def ChangeTuple(t1,t2,t3):
      return (t1,t2,t3)

# 游戏循环
while keep_going:
      for event in pygame.event.get():  # 遍历事件
            if event.type == pygame.QUIT:  # 退出事件
                  keep_going = False
      
      color[0]=color[1]=color[2]=color[0]+1
      if(color[0]>=255):
            color[0]=color[1]=color[2]=color[0]-255

      print(tuple(color))
      pygame.draw.circle(screen,tuple(color),(200,300),radius)
      pygame.display.update()  # 刷新屏幕
      time.sleep(0.1)

# 退出程序
pygame.quit()