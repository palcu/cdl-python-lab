# http://ocw.cs.pub.ro/courses/programare/laboratoare/python#exercitii

import pygame
from pygame.locals import *

w_size = 400
h_size = 400
screen = pygame.display.set_mode((w_size, h_size), DOUBLEBUF)

blue_color = (0, 0, 255)
black_color = (0, 0, 0)
p_x = 10
p_y = 200
radius = 20

running = True
increment = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                increment = True

    if increment:
        p_x = p_x + 1

    position = [p_x, p_y]

    screen.fill(black_color)
    pygame.draw.circle(screen, blue_color, position, radius)
    pygame.display.flip()

pygame.quit()
