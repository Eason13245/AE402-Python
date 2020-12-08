import pygame
screen= pygame.display.set_mode((600,400))
class Pad(pygame.sprite.Sprite):

    def __init__(self):
        pygame.prite.Sprite.__init__(self)
        self.image = ygame.Surface([50,10])
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width - self.rect_width)/2)
        self.rect.y = screen.get_height()- self.rect.height - 20

    def update(self):
        pos = pygame.mouse.get_pose()
        self.rect.x = pos[0]
        if self.rect.x > screen.get_width() - self.rect_width():
            self.rect.x = screen.get_width() - self.rect_width()
        
        
