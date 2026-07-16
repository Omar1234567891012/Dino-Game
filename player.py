import pygame

class Dino:

    def __init__(self):
        self.x = 120
        self.y = 280
        self.vy = 0
        self.gravity = 0.8
        self.ground = 280

    def jump(self):
        if self.y >= self.ground:
            self.vy = -15

    def update(self):
        self.vy += self.gravity
        self.y += self.vy

        if self.y > self.ground:
            self.y = self.ground
            self.vy = 0

    def rect(self):
        return pygame.Rect(self.x, self.y, 60, 70)

    def draw(self, screen, color):

    # Körper
       pygame.draw.rect(screen, color, (self.x, self.y + 20, 60, 35))

    # Kopf
       pygame.draw.rect(screen, color, (self.x + 45, self.y, 30, 30))

    # BEINE (neu)
       pygame.draw.rect(screen, color, (self.x + 10, self.y + 55, 10, 25))
       pygame.draw.rect(screen, color, (self.x + 35, self.y + 55, 10, 25))

    # kleiner Fuß-Effekt
       pygame.draw.rect(screen, (0, 0, 0), (self.x + 10, self.y + 78, 10, 5))
       pygame.draw.rect(screen, (0, 0, 0), (self.x + 35, self.y + 78, 10, 5))
