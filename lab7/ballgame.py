import pygame

pygame.init()


width, height = 700, 700
screen = pygame.display.set_mode((width, height))

x, y = width // 2, height // 2
r = 25
step = 20
running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - r - step >= 0:
                y -= step
            elif event.key == pygame.K_DOWN and y + r + step <= height:
                y += step
            elif event.key == pygame.K_LEFT and x - r - step >= 0:
                x -= step
            elif event.key == pygame.K_RIGHT and x + r + step <= width:
                x += step

    pygame.draw.circle(screen, (255, 0, 0), (x, y), r)
    pygame.display.update()

pygame.quit()
