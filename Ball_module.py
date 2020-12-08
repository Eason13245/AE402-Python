import pygame
import math
import random
screen = pygame.display.set_mode((600, 400))
class Ball(pygame.sprite.Sprite):
    dx = 0  #x位移量
    dy = 0  #y位移量
    x = 0  #球x坐標
    y = 0  #球y坐標
    speed = 0  #球移動速度
    direction = 0  #球移動方向

    def __init__(self, speed, srx, sry, radium, color,edge=10):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.x = srx
        self.y = sry
        self.image = pygame.Surface([radium*2, radium*2])  #繪製球體
        self.image.fill((255,255,255))
        pygame.draw.circle(self.image, color, (radium,radium), radium, edge)
        self.rect = self.image.get_rect()  #取得球體區域
        self.rect.center = (srx,sry)  #初始位置
        direction = random.randint(20,70)  #移動角度
        radian = math.radians(direction)  #角度轉為弳度
        self.dx = speed * math.cos(radian)  #球水平運動速度
        self.dy = -speed * math.sin(radian)  #球垂直運動速度

    def update(self):
        self.x += self.dx  #計算球新餘標
        self.y += self.dy
        self.rect.x = self.x  #移動球圖形
        self.rect.y = self.y
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()):  #到達左右邊界
            self.bouncelr()
        elif self.rect.top <= 5:  #到達上邊界
            self.bounceup()
        if self.rect.bottom >= screen.get_height()-5:
            return True
        else:
            return False
    def collidebounce(self):
        self.dx *= -1
    def bounceup(self):  #上邊界反彈
        self.dy *= -1  #垂直速度變號

    def bouncelr(self):  #左右邊界反彈
        self.dx *= -1  #水平速度變號

    def bounceLR(self):
        self.dx *= -1
    def bonceUP(self):
        self.dy *= -1

#self.rect.bottom >= screen.get_height()-5
