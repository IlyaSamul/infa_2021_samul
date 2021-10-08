import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 255, 255), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 3)
circle(screen, (255, 0, 0), (155, 180), 25)
circle(screen, (0, 0, 0), (155, 180), 25, 1)
circle(screen, (255, 0, 0), (245, 180), 20)
circle(screen, (0, 0, 0), (245, 180), 20, 1)
circle(screen, (0, 0, 0), (155, 180), 11)
circle(screen, (0, 0, 0), (245, 180), 11)
rect(screen, (0, 0, 0), (155, 250, 90, 20))
line(screen, (0, 0, 0), (100, 100), (190, 170), 15)
line(screen, (0, 0, 0), (210, 170), (300, 135), 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()