import  pygame

hero_rect = pygame.Rect(100,500,120,125)

print("hero的原点 %d %d" %(hero_rect.x ,hero_rect.y))
print("hero的尺寸  %d %d"% (hero_rect.width,hero_rect.height))
#sizes属性是元组属性 第一个值是width 第二个值是height
print("%d %d" % hero_rect.size)