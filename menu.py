import pygame

class Menu:

    def __init__(self, w, h):
        self.play_btn = pygame.Rect(400, 150, 200, 60)
        self.shop_btn = pygame.Rect(400, 230, 200, 60)
        self.quit_btn = pygame.Rect(400, 310, 200, 60)

        self.font = pygame.font.SysFont(None, 50)
        self.title = pygame.font.SysFont(None, 80)

        self.cloud_x = 0
        self.w = w

    def update(self):
        self.cloud_x += 1
        if self.cloud_x > self.w:
            self.cloud_x = -200

    def draw(self, screen, coins, highscore):

        screen.fill((135,206,235))

        pygame.draw.circle(screen, (255,255,255), (self.cloud_x, 80), 30)

        screen.blit(self.title.render("DINO RUN (by Omar)", True, (0,0,0)), (280, 40))

        pygame.draw.rect(screen, (0,200,0), self.play_btn)
        pygame.draw.rect(screen, (0,150,200), self.shop_btn)
        pygame.draw.rect(screen, (200,0,0), self.quit_btn)

        screen.blit(self.font.render("PLAY", True, (255,255,255)), (455,160))
        screen.blit(self.font.render("SHOP", True, (255,255,255)), (450,240))
        screen.blit(self.font.render("QUIT", True, (255,255,255)), (450,320))

        screen.blit(self.font.render(f"Coins: {coins}", True, (0,0,0)), (20,20))
        screen.blit(self.font.render(f"Highscore: {highscore}", True, (0,0,0)), (20,60))
