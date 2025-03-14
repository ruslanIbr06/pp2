import pygame
import math
import time
pygame.init()




width, height = 1000, 1000
center = (width // 2, height // 2)

clock_bg = pygame.image.load("clock.png")
minute = pygame.image.load("min_hand.png")
second = pygame.image.load("sec_hand.png")

clock_bg = pygame.transform.scale(clock_bg, (width, height))

minuteRect = minute.get_rect()
secondRect = second.get_rect()

screen = pygame.display.set_mode((width, height))

def rotateImage(image, angle, pivot):
    rotatedImage = pygame.transform.rotate(image, angle)
    new_rect = rotatedImage.get_rect(center=pivot)
    return rotatedImage, new_rect

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_bg, (0, 0))

    t = time.localtime()
    seconds = t.tm_sec
    minutes = t.tm_min

    secAngle = -seconds * 6
    minAngle = -minutes * 6

    rotatedSec, secRect = rotateImage(second, secAngle, center)
    rotatedMin, minRect = rotateImage(minute, minAngle, center)

    screen.blit(rotatedMin, minRect)
    screen.blit(rotatedSec, secRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.time.delay(1000)

pygame.quit()
