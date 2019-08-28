import  pygame

pygame.init()
#创建游戏的窗口 480* 852

screen = pygame.display.set_mode((480,850))

#绘制背景图像
# 1> 加载图像数据
backg = pygame.image.load("./image/background.png")
screen.blit(backg,(0,0))
pygame.display.update()

while True:
    pass

pygame.quit()