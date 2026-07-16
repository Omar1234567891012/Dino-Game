import pygame
import random

particles = []

def spawn(x, y, color):
    for _ in range(8):
        particles.append([
            x,
            y,
            random.randint(-3,3),
            random.randint(-5,-1),
            30,
            color
        ])

def update(screen):

    for p in particles[:]:

        p[0] += p[2]
        p[1] += p[3]
        p[4] -= 1

        pygame.draw.circle(screen, p[5], (int(p[0]), int(p[1])), 3)

        if p[4] <= 0:
            particles.remove(p)
