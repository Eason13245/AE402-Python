import pygame
from Ball_module import Ball
from Pad import Pad
from Bricks import Brick

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("打磚塊遊戲")
background = pygame.Surface(screen.get_size()).convert()
background.fill((255,255,255))
allsprite = pygame.sprite.Group()  #建立全部角色群組
bricks = pygame.sprite.Group()  #建立磚塊角色群組
ball = Ball(10, 300, 200, 30, (255,0,0),edge=3)  #建立紅色球物件
#ball1 = Ball(10, 300, 200, 30, (0,0,255),edge=3)
allsprite.add(ball)  #加入全部角色群組
#allsprite.add(ball1)  #加入全部角色群組
pad = Pad()  #建立滑板球物件
allsprite.add(pad)  #加入全部角色群組
clock = pygame.time.Clock()
for row in range(0, 4):  #3列方塊
    for column in range(0, 15):  #每列15磚塊
        if row == 0 or row == 1:  #1,2列為綠色磚塊
            brick = Brick((0,255,0), column * 40 + 1, row * 15 + 1)
        if row == 2 or row == 3:  #3,4列為藍色磚塊
            brick = Brick((0,0,255), column * 40 + 1, row * 15 + 1)
        bricks.add(brick)  #加入磚塊角色群組
        allsprite.add(brick)  #加入全部角色群組
playing = False  #開始時球不會移動
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    seconds=int((pygame.time.get_ticks()-start_ticks)/1000) #calculate how many seconds

    
    buttons = pygame.mouse.get_pressed()  #檢查滑鼠按鈕
    if buttons[0]:  #按滑鼠左鍵後球可移動
        playing = True
    if playing == True:  #遊戲進行中
        screen.blit(background, (0,0))  #清除繪圖視窗
        fail = ball.update()  #移動球體
        if fail:  #球出界
            running = False
        pad.update()  #更新滑板位置
        hitbrick = pygame.sprite.spritecollide(ball, bricks, True)  #檢查球和磚塊碰撞
        if len(hitbrick) > 0:  #球和磚塊發生碰撞
            ball.rect.y += 20  #球向下移
            ball.bounceup()  #球反彈
            score = 0+1
        hitpad = pygame.sprite.collide_rect(ball, pad)  #檢查球和滑板碰撞
        if hitpad:  #球和滑板發生碰撞
            ball.bounceup()  #球反彈


        allsprite.draw(screen)  #繪製所有角色
        message = str(score)+' point'
        text = font.render(message, 10, BLACK)
        screen.blit(text, (10,10))

        t = font.render(str(seconds), 10, RED)
        screen.blit(t, (10,40))

    pygame.display.flip()
pygame.quit() 
