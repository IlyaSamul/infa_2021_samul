import math
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((454, 300))


def house(x, y, a):
    b = 85*a/110
    rect(screen, (150, 75, 0),    (x, y, a, b))
    rect(screen, (0, 0, 0),       (x, y, a, b), 1)
    rect(screen, (48, 213, 200),  (x + a / 3, y + b / 3, a / 3, b / 3))
    rect(screen, (205, 133, 63),  (x + a / 3, y + b / 3, a / 3, b / 3), 1)
    polygon(screen, (255, 0, 0),  ((x, y), (x + a, y), (x + a / 2, y - 65 * a / 110)))
    polygon(screen, (0, 0, 0),    ((x, y), (x + a, y), (x + a / 2, y - 65 * a / 110)), 1)


def clouds(x, y, r):
    circle(screen, (255, 255, 255),  (x + r * 7 / 5, y - r * 4 / 5), r)
    circle(screen, (0, 0, 0),        (x + r * 7 / 5, y - r * 4 / 5), r, 1)
    circle(screen, (255, 255, 255),  (x + r * 12 / 5, y - r * 4 / 5), r)
    circle(screen, (0, 0, 0),        (x + r *  12 / 5, y - r * 4 / 5), r, 1)
    circle(screen, (255, 255, 255),  (x, y), r)
    circle(screen, (0, 0, 0),        (x, y), r, 1)
    circle(screen, (255, 255, 255),  (x + r, y), r)
    circle(screen, (0, 0, 0),        (x + r, y), r, 1)
    circle(screen, (255, 255, 255),  (x + 2 * r, y), r)
    circle(screen, (0, 0, 0),        (x + 2 * r, y), r, 1)
    circle(screen, (255, 255, 255),  (x + 3 * r, y), r)
    circle(screen, (0, 0, 0),        (x + 3 * r, y), r, 1)


def tree(x, y, r):
    rect(screen, (101, 67, 33),    (x, y, r * 4 / 5, r * 12 / 5))
    rect(screen, (0, 0, 0),        (x, y, r * 4 / 5, r * 12 / 5), 1)
    circle(screen, (23, 114, 69),  (x + r * 2 / 5, y - r * 14 / 5), r)
    circle(screen, (0, 0, 0),      (x + r * 2 / 5, y - r * 14 / 5), r, 1)
    circle(screen, (23, 114, 69),  (x - r * 3 / 5, y - r * 9 / 5), r)
    circle(screen, (0, 0, 0),      (x - r * 3 / 5, y - r * 9 / 5), r, 1)
    circle(screen, (23, 114, 69),  (x + r * 7 / 5, y - r * 9 / 5), r)
    circle(screen, (0, 0, 0),      (x + r * 7 / 5, y - r * 9 / 5), r, 1)
    circle(screen, (23, 114, 69),  (x + r * 2 / 5, y - r * 4 / 5), r)
    circle(screen, (0, 0, 0),      (x + r * 2 / 5, y - r * 4 / 5), r, 1)
    circle(screen, (23, 114, 69),  (x - r * 2 / 5, y - r / 5), r)
    circle(screen, (0, 0, 0),      (x - r * 2 / 5, y - r / 5), r, 1)
    circle(screen, (23, 114, 69),  (x + r * 6 / 5, y - r / 5), r)
    circle(screen, (0, 0, 0),      (x + r * 6 / 5, y - r / 5), r, 1)


def sun(x, y, r):
    a = 0
    da = math.pi / 20
    q = [0] * 40
    for i in range(20):
        q[2 * i] = (x + r * math.cos(a), y - r * math.sin(a))
        a += da
        q[2 * i + 1] = (x + 0.9 * r * math.cos(a), y - 0.9 * r * math.sin(a))
        a += da
    polygon(screen, (255, 192, 203), q)
    polygon(screen, (0, 0, 0), q, 1)


xh1 = 70;    yh1 = 180;     ah1 = 110
xh2 = 300;   yh2 = 180;     ah2 = 70   

xc1 = 230;  yc1 = 70;   rc1 = 15
xc2 = 110;  yc2 = 50;   rc2 = 18
xc3 = 350;  yc3 = 60;   rc3 = 21

xt1 = 220;  yt1 = 190;  rt1 = 25
xt2 = 400;  yt2 = 190;  rt2 = 15

xs = 40
ys = 40
rs = 30


rect(screen, (175, 238, 238), (0, 0, 454, 150))
rect(screen, (26, 148, 49), (0, 150, 454, 150))
house(xh1, yh1, ah1)
house(xh2, yh2, ah2)
clouds(xc1, yc1, rc1)
clouds(xc2, yc2, rc2)
clouds(xc3, yc3, rc3)
tree(xt1, yt1, rt1)
tree(xt2, yt2, rt2)
sun(xs, ys, rs)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
