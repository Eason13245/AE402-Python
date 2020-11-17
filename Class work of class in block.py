import pygame
import random

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

pygame.init()

a = 10
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self. image = pygame.Surface([width,height])
        self. image.fill(color)
        self.rect = self.image.get_rect()

hit_group = pygame.sprite.Group()
all_group = pygame.sprite.Group()


for i in range(10):
    block = Block(BLACK,20,20)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    all_group.add(block)
    hit_group.add(block)

player = Block(RED,20,20)
all_group.add(player)


font = pygame.font.Font(None,50)
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
                done = True

        keys = pygame.key.get_pressed()
        
    screen.fill(WHITE)
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]
    score_group = pygame.sprite.spritecollide(player, hit_group, True)

    for block in score_group:
        score += 1
        a = a -1
        hit_group.empty()
        all_group.empty()
        player = Block(RED,20,20)
        all_group.add(player)
        for i in range(a):
            block = Block(BLACK,20,20)
            block.rect.x = random.randrange(screen_width)
            block.rect.y = random.randrange(screen_height)
            hit_group.add(block)
            all_group.add(block)

    score = len(score_group)
    message = str(score)+"points"
    text = font.render(message, True, BLACK)
    screen.blit(text, (10,10))
    all_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
