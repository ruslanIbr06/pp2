import pygame
import random
import time

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
done = False
score = 0
level = 1
speed = 150

# Head and body coordinates
coor_head = [100, 100]
coor_body = [[30, 100], [40, 100], [50, 100], [60, 100], [70, 100], [80, 100], [90, 100], [100, 100]]

# Direction
next_dir = "r"
direc = "r"

# Food data structure
class Food:
    def __init__(self):
        self.position = self.generate_position()
        self.weight = random.choice([1, 3, 5])
        self.spawn_time = time.time()

    def generate_position(self):
        while True:
            x = random.randrange(1, width // 10) * 10
            y = random.randrange(1, height // 10) * 10
            if [x, y] not in coor_body:
                return [x, y]

    def is_expired(self):
        return time.time() - self.spawn_time > 8  # 8 seconds lifetime

# Initial food
current_food = Food()

def score_update(font, size, color):
    score_font = pygame.font.SysFont(font, size)
    score_render = score_font.render(f"Score: {score}  Level: {level}", True, color)
    screen.blit(score_render, (10, 10))

def game_over_message(font, size, color):
    game_font = pygame.font.SysFont(font, size)
    text = game_font.render(f"Game Over, final score: {score}", True, color)
    screen.blit(text, (100, 250))
    pygame.display.update()
    pygame.time.delay(3000)

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

#Collision with self
    for seg in coor_body[:-1]:
        if coor_head == seg:
            game_over_message("times new roman", 50, (255, 0, 0))
            done = True

#Collision with wall
    if coor_head[0] < 0 or coor_head[0] >= width or coor_head[1] < 0 or coor_head[1] >= height:
        game_over_message("times new roman", 50, (255, 0, 0))
        done = True

#Update direction
    if next_dir == "r" and direc != "l":
        direc = "r"
    if next_dir == "l" and direc != "r":
        direc = "l"
    if next_dir == "u" and direc != "d":
        direc = "u"
    if next_dir == "d" and direc != "u":
        direc = "d"

#Move snake head
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

#Eat food
    if coor_head == current_food.position:
        score += current_food.weight * 10
        for _ in range(current_food.weight):
            coor_body.insert(0, coor_body[0])  # Grow per weight
        current_food = Food()

#Replace expired food
    if current_food.is_expired():
        current_food = Food()

#Level and speed increase
    if score % 30 == 0 and score != 0:
        level = score // 30 + 1
        speed = max(80, speed - (level * 2))

#Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(current_food.position[0], current_food.position[1], 10, 10))

    for el in coor_body:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(el[0], el[1], 10, 10))
    pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(coor_head[0], coor_head[1], 10, 10))

    score_update("times new roman", 20, (128, 128, 128))
    pygame.display.flip()
    pygame.time.delay(speed)

pygame.quit()
