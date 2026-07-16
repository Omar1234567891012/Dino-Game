import pygame

class Shop:

    def draw(self, screen, font, coins):

        screen.fill((30,30,30))

        screen.blit(font.render("SHOP (ESC = Back)", True, (255,255,255)), (300, 50))
        screen.blit(font.render(f"Coins: {coins}", True, (255,255,0)), (400, 120))
