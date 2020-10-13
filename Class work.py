import pygame, random

BLACK = (0,0,0)
WHITE = (255, 255, 255)

pygame.init()

size = (700,500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mygame")

done = False
click = False
Rcount = 0
Rlimit = 50

def RandomColor():
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    return (R,G,B)

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
        if event.type== pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click = True
            Rcount = 0
            Color = RandomColor()
           
    screen.fill(BLACK)
    if click and Rcount < Rlimit:
        pygame.draw.circle(screen, Color, pos, Rcount)
        pygame.display.flip()
        Rcount +=1 
        if Rcount >= Rlimit:
            click = False
    clock.tick(60)

pygame.quit()
