import pygame

RED = (255, 0, 0)
WHITE = ( 0, 0, 0)
pygame.init()
size = (640, 70)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moving Ball")


done = False
x = 320
y = 35

while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_LEFT]:
                x -= 10

            if keys[pygame.K_RIGHT]: 
                x += 10

        screen.fill(WHITE)

        if x >= 640:
            x = 630
            y = 35

        elif x <= 0:
            x = 10
            y = 35

        pygame.draw.circle( screen, RED, (x, y), 10)

        clock = pygame.time.Clock()

        pygame.display.flip()

        clock.tick(60)

pygame.quit()
