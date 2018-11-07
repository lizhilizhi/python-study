import  pygame
#display方法
pygame.init()
#创建游戏的窗口 480* 852

screen = pygame.display.set_mode((480,850))

#绘制背景图像
# 1> 加载图像数据
# 2>绘制图像
# 2更新

backg = pygame.image.load("./image/background.png")
screen.blit(backg,(0,0))
pygame.display.update()



hero = pygame.image.load("./image/hero1.png")
screen.blit(hero,(150, 20))
#可以在所有绘制工作完成后，统一调用
pygame.display.update()


while True:
    pass

pygame.quit()