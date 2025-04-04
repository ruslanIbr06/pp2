import pygame

'''
Hotkeys:
R - Red color
G - Green color
B - Blue color
E - Eraser
C - Draw Circle
D - Draw Rectangle
Q - Draw Square
T - Draw Right Triangle
Y - Draw Equilateral Triangle
H - Draw Rhombus
F - Brush
Wheel Up - Increase Brush Size
Wheel Down - Decrease Brush Size
'''

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    drawing_mode = 'free'
    points = []
    start_pos = None
    shapes = []
    temp_shape = None
    is_drawing = False
    current_color = (0, 0, 255)

    colors = {
        'blue': (0, 0, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'black': (0, 0, 0),
        'white': (255, 255, 255)
    }

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and (
                   (event.key == pygame.K_w and ctrl_held) or
                   (event.key == pygame.K_F4 and alt_held) or
                   event.key == pygame.K_ESCAPE)):
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: current_color = colors['red']
                elif event.key == pygame.K_g: current_color = colors['green']
                elif event.key == pygame.K_b: current_color = colors['blue']
                elif event.key == pygame.K_e: current_color = colors['white']
                elif event.key == pygame.K_c: drawing_mode = 'circle'
                elif event.key == pygame.K_f: drawing_mode = 'free'
                elif event.key == pygame.K_d: drawing_mode = 'rectangle'
                elif event.key == pygame.K_q: drawing_mode = 'square'
                elif event.key == pygame.K_t: drawing_mode = 'right_triangle'
                elif event.key == pygame.K_y: drawing_mode = 'equilateral_triangle'
                elif event.key == pygame.K_h: drawing_mode = 'rhombus'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    is_drawing = True
                    if drawing_mode == 'free':
                        points.append([])
                    elif drawing_mode in ['rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                        start_pos = event.pos
                elif event.button == 3:
                    radius = max(1, radius - 1)
                elif event.button == 4:
                    radius = min(200, radius + 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    is_drawing = False
                    if start_pos and drawing_mode in ['rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                        end_pos = event.pos
                        shapes.append((drawing_mode, start_pos, end_pos, current_color))
                        start_pos = None
                        temp_shape = None

            if event.type == pygame.MOUSEMOTION:
                if is_drawing and drawing_mode == 'free':
                    position = event.pos
                    points[-1].append(position)
                elif start_pos and drawing_mode in ['rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                    end_pos = event.pos
                    temp_shape = (drawing_mode, start_pos, end_pos, current_color)

        screen.fill((255, 255, 255))

        for shape in shapes:
            drawShape(screen, *shape)

        if temp_shape:
            drawShape(screen, *temp_shape)

        for line in points:
            for i in range(len(line) - 1):
                drawLineBetween(screen, i, line[i], line[i + 1], radius, current_color)

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = i / iterations
        x = int((1 - progress) * start[0] + progress * end[0])
        y = int((1 - progress) * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawShape(screen, mode, start, end, color):
    if mode == 'rectangle':
        pygame.draw.rect(screen, color, pygame.Rect(min(start[0], end[0]), min(start[1], end[1]),
                                                    abs(end[0] - start[0]), abs(end[1] - start[1])), 2)
    elif mode == 'circle':
        center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
        radius = int(((end[0] - start[0])**2 + (end[1] - start[1])**2)**0.5) // 2
        pygame.draw.circle(screen, color, center, radius, 2)
    elif mode == 'square':
        side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
        end_pos = (start[0] + side if end[0] > start[0] else start[0] - side,
                   start[1] + side if end[1] > start[1] else start[1] - side)
        pygame.draw.rect(screen, color, pygame.Rect(min(start[0], end_pos[0]), min(start[1], end_pos[1]),
                                                    side, side), 2)
    elif mode == 'right_triangle':
        points = [start, (start[0], end[1]), end]
        pygame.draw.polygon(screen, color, points, 2)
    elif mode == 'equilateral_triangle':
        side = abs(end[0] - start[0])
        height = int(side * (3**0.5) / 2)
        top = (start[0] + side // 2, start[1])
        left = (start[0], start[1] + height)
        right = (start[0] + side, start[1] + height)
        pygame.draw.polygon(screen, color, [top, left, right], 2)
    elif mode == 'rhombus':
        center_x = (start[0] + end[0]) // 2
        center_y = (start[1] + end[1]) // 2
        dx = abs(end[0] - start[0]) // 2
        dy = abs(end[1] - start[1]) // 2
        points = [(center_x, center_y - dy), (center_x + dx, center_y),
                  (center_x, center_y + dy), (center_x - dx, center_y)]
        pygame.draw.polygon(screen, color, points, 2)

main()
