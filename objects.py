import pygame
import random

WIDTH = 1000

class Obstacle:

    def __init__(self, x):
        self.rect = pygame.Rect(x, 280, 30, 80)

    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.rect.x = WIDTH + random.randint(200, 500)

    def draw(self, screen):
        pygame.draw.rect(screen, (0,180,0), self.rect)


class Coin:

    def __init__(self):
        self.rect = pygame.Rect(
            random.randint(600, 2000),
            random.randint(180, 300),
            15,
            15
        )

    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.rect.x = WIDTH + random.randint(300, 1000)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,215,0), self.rect.center, 8)


class StarPowerUp:

    def __init__(self):
        self.rect = pygame.Rect(random.randint(1500, 3000), 250, 20, 20)

    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.rect.x = WIDTH + random.randint(2000, 4000)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,0), self.rect.center, 10)


class GravityOrb:

    def __init__(self):
        self.rect = pygame.Rect(random.randint(2000, 5000), 220, 20, 20)

    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.rect.x = WIDTH + random.randint(2000, 5000)

    def draw(self, screen):
        pygame.draw.circle(screen, (100,150,255), self.rect.center, 10)


class MagnetOrb:

    def __init__(self):
        self.rect = pygame.Rect(random.randint(2000, 5000), 200, 20, 20)

    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.rect.x = WIDTH + random.randint(2000, 5000)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,0,255), self.rect.center, 10)


class SpeedOrb:

    def __init__(self):
        self.rect = pygame.Rect(random.randint(2500, 6000), 220, 20, 20)

    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.rect.x = WIDTH + random.randint(2500, 6000)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,0), self.rect.center, 10)
