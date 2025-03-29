import pygame
import random

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
done = False
score = 0
level = 1
speed = 150

#Head variable
coor_head = [100, 100]

#Body variable
coor_body = [
    [30, 100], [40, 100], [50, 100], [60, 100], [70, 100], [80, 100], [90, 100], [100, 100]
]


#Function to generate a random apple position avoiding snake body
def generate_apple():
    while True:
        apple_x = random.randrange(1, width // 10) * 10
        apple_y = random.randrange(1, height // 10) * 10
        if [apple_x, apple_y] not in coor_body:
            return [apple_x, apple_y]


coor_apple = generate_apple()
eaten = False

#Direction
next_dir = "r"
direc = "r"


def score_update(font, size, color):
    global score, level
    score_font = pygame.font.SysFont(font, size)
    score_render = score_font.render(f"Score: {score}  Level: {level}", True, color)
    screen.blit(score_render, (10, 10))
    pygame.display.update()


def game_over_message(font, size, color):
    global score, done
    game_over_font = pygame.font.SysFont(font, size)
    game_over_surface = game_over_font.render(f"Game Over, your final score: {score}", True, color)
    screen.blit(game_over_surface, (100, 250))
    pygame.display.update()
    pygame.time.delay(3000)
    done = True


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_dir = "r"
            if event.key == pygame.K_LEFT:
                next_dir = "l"
            if event.key == pygame.K_UP:
                next_dir = "u"
            if event.key == pygame.K_DOWN:
                next_dir = "d"

#Check for self-collision
    for seg in coor_body[:-1]:
        if coor_head == seg:
            game_over_message("times new roman", 50, (255, 0, 0))

#Check for wall collision
    if coor_head[0] < 0 or coor_head[0] >= width or coor_head[1] < 0 or coor_head[1] >= height:
        game_over_message("times new roman", 50, (255, 0, 0))

#Logic for movement
    if next_dir == "r" and direc != "l":
        direc = "r"
    if next_dir == "l" and direc != "r":
        direc = "l"
    if next_dir == "u" and direc != "d":
        direc = "u"
    if next_dir == "d" and direc != "u":
        direc = "d"

    if direc == "r":
        coor_head[0] += 10
    if direc == "l":
        coor_head[0] -= 10
    if direc == "u":
        coor_head[1] -= 10
    if direc == "d":
        coor_head[1] += 10

    new_coor = [coor_head[0], coor_head[1]]
    coor_body.append(new_coor)
    coor_body.pop(0)

#Check if apple is eaten
    if coor_head == coor_apple:
        eaten = True
        score += 10
        coor_body.insert(0, coor_body[0])  # Increase snake size

#Increase level and speed every 30 points
    if score % 30 == 0 and score != 0:
        level = score // 30 + 1
        speed = max(100, speed - (level * 2))  # Increase speed

    if eaten:
        coor_apple = generate_apple()
        eaten = False

#Drawing section
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(coor_apple[0], coor_apple[1], 10, 10))

    for el in coor_body:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(el[0], el[1], 10, 10))

    pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(coor_head[0], coor_head[1], 10, 10))

    score_update("times new roman", 20, (128, 128, 128))
    pygame.display.flip()
    pygame.time.delay(speed)

pygame.quit()