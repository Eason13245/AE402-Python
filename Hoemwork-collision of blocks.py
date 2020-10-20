import pygame, random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width,screen_height])

player_x = 0
player_y = 0
player_W = 50
player_h = 50

block_W = 50
block_h = 50
block_x = random.randrange(screen_width-block_W)
block_y = random.randrange(screen_height-block_h)

collision = False
score = 0
done =False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True

    xin = block_x<=player_x<=block_x+block_W or block_x<=player_x+player_W<=block_x+block_W
    yin = block_y<=player_y<=block_y+block_h or block_y<=player_y+player_h<=block_y+block_h
    if xin and yin and not collision:
        collision = True

    screen.fill(WHITE)

    pos = pygame.mouse.get_pos()

    pygame.draw.rect(screen, RED, [player_x, player_y, player_W, player_h])
    pygame.draw.rect(screen, BLACK, [block_x, block_y, block_W, block_h])

    if not xin and yin:
        pygame.draw.rect(screen, RED, pos, [player_W, player_h])
        pygame.display.flip()

    clock.tick(60)

pygame.quit

