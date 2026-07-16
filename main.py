import pygame

import particles
from player import Dino
from objects import Coin, Obstacle, SpeedOrb, StarPowerUp, MagnetOrb, GravityOrb
from menu import Menu
from shop import Shop
from save import load_save, save_game

pygame.init()
pygame.mixer.init()

coin_sound = pygame.mixer.Sound("assets/sounds/Coin Pickup.wav")
jump_sound = pygame.mixer.Sound("assets/sounds/Jumpsound.wav")
hit_sound = pygame.mixer.Sound("assets/sounds/Hit sound.wav")
power_sound = pygame.mixer.Sound("assets/sounds/Powerup sound.wav")

WIDTH = 1000
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)

save = load_save()

coins_total = save["coins"]
skin = save["skin"]

skins = {
    "gray": (70,70,70),
    "blue": (80,160,255),
    "green": (0,180,0),
    "yellow": (255,255,0),
    "purple": (135,225,0),
    "red": (255,0,0),
}

dino = Dino()
menu = Menu(WIDTH, HEIGHT)
shop = Shop()

obstacles = [Obstacle(900), Obstacle(1300)]
coins = [Coin(), Coin()]
star = StarPowerUp()
gravity_orb = GravityOrb()
magnet = MagnetOrb()
speed_orb = SpeedOrb()

state = "MENU"

speed = 8
score = 0
highscore = 0

invincible = 0

magnet_active = False
magnet_timer = 0

speed_active = False
speed_timer = 0

gravity_active = False
gravity_timer = 0

running = True

while running:

    clock.tick(60)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            save_game({"coins": coins_total, "skin": skin})
            running = False

    # MENU
    if state == "MENU":

        menu.update()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if menu.play_btn.collidepoint(mx, my):
                    state = "PLAY"

                if menu.shop_btn.collidepoint(mx, my):
                    state = "SHOP"

                if menu.quit_btn.collidepoint(mx, my):
                    running = False

        menu.draw(screen, coins_total, highscore)
        pygame.display.flip()
        continue

    # SHOP
    if state == "SHOP":

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = "MENU"

        shop.draw(screen, font, coins_total)
        pygame.display.flip()
        continue

    # PLAY
    # if state == "GAMEOVER":
    #
    #     for event in events:
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_ESCAPE:
    #                 state = "MENU"
    #
    #     continue

    if state == "PLAY":

        player_rect = dino.rect()

        if player_rect.colliderect(speed_orb.rect):

            speed_active = True
            speed_timer = pygame.time.get_ticks()
            speed_orb.rect.x = 5000

            if speed_active:

                if pygame.time.get_ticks() - speed_timer < 6000:
                    speed = 14
                else:
                    speed_active = False
                    speed = 8

        if player_rect.colliderect(magnet.rect):
            magnet_active = True
            magnet_timer = pygame.time.get_ticks()
            magnet.rect.x = 4000

            if magnet_active:

                if pygame.time.get_ticks() - magnet_timer < 6000:

                  for c in coins:
                    dx = dino.x - c.rect.x
                    dy = dino.y - c.rect.y

                    c.rect.x += dx * 0.08
                    c.rect.y += dy * 0.08

            else:
                magnet_active = False

        if player_rect.colliderect(gravity_orb.rect):
            gravity_active = True
            gravity_timer = pygame.time.get_ticks()
            gravity_orb.rect.x = 4000

            if gravity_active:

                if pygame.time.get_ticks() - gravity_timer < 8000:

                   dino.gravity = 0.3

                else:

                   gravity_active = False
                   dino.gravity = 0.8

        for c in coins:

            if player_rect.colliderect(c.rect):
              coins_total += 1
              coin_sound.play()

            particles.spawn(c.rect.x, c.rect.y, (225,215,0))

            c.rect.x = 2000

        for event in events:

            if event.type == pygame.KEYDOWN:

                 if event.key == pygame.K_SPACE:
                    dino.jump()
                    jump_sound.play()

        for obs in obstacles:

            if player_rect.colliderect(obs.rect):
               hit_sound.play()
               state = "GAMEOVER"

        dino.update()
        player_rect = dino.rect()

        if invincible > 0:
            invincible -= 1

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump()

        for obs in obstacles:
            obs.update(speed)
            if player_rect.colliderect(obs.rect):
                if invincible <= 0:
                    state = "MENU"

        for c in coins:
            c.update(speed)
            if player_rect.colliderect(c.rect):
                coins_total += 1
                c.rect.x = 2000

        star.update(speed)

        if player_rect.colliderect(star.rect):
            invincible = 300
            star.rect.x = 3000

        speed += 0  # stabil

        score += 1
        if score > highscore:
            highscore = score

        screen.fill((135,206,235))

        pygame.draw.line(screen, (0,0,0), (0,360), (WIDTH,360), 3)

        dino.draw(screen, skins[skin])
        particles.update(screen)

        for obs in obstacles:
            obs.draw(screen)

        for c in coins:
            c.draw(screen)

        star.draw(screen)

        pygame.display.flip()

pygame.quit()
