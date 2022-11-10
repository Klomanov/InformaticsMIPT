import time

from Gun import GunType
import pygame
from Bomber import BomberType

from Constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
bullet = 0
score = 0
balls = []
targets = []
score_font = pygame.font.SysFont('comicSans', 30)
inst_font = pygame.font.SysFont('comicSans', 22)

clock = pygame.time.Clock()
gun = GunType(screen, GUN_SPAWN)
bomber = BomberType(screen)
last_spawn_time = 0
last_hit_time = None
start_time = time.time()
finished = False
text = INSTRUCTIONS_TEXT.split("\n")

while not finished:
    if time.time() - start_time <= INSTRUCTIONS_DURATION:
        for i in range(len(text)):
            t = inst_font.render(text[i], False, BLACK)
            screen.blit(t, (30, 10 + i * 25))
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    else:
        screen.fill(WHITE)
        gun.draw()
        bomber.draw()
        for b in balls:
            b.draw()
        for t in targets:
            t.draw()
        score_text = score_font.render(f"{score}", False, BLACK)
        keys = pygame.key.get_pressed()

        screen.blit(score_text, (10, 50))

        pygame.display.update()

        clock.tick(FPS)

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            gun.vx = 10
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            gun.vx = -10
        else:
            gun.vx = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gun.fire2_start(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    new_ball = gun.strike(SMALL_BULLETS_R, SMALL_BULLETS_POWER)
                    balls.append(new_ball)
                    if len(balls) > 5:
                        balls.pop(0)
                elif event.button == 1:
                    new_ball = gun.strike(BIG_BULLETS_R, BIG_BULLETS_POWER)
                    balls.append(new_ball)
                    if len(balls) > 5:
                        balls.pop(0)

            elif event.type == pygame.MOUSEMOTION:
                gun.targetting(event)

        gun.move(gravity=False)
        bomber.move(gravity=False)

        for b in balls:
            b.move()
            for t in targets:
                if b.is_collide(t) and round(b.vy, 2) != 0:
                    score += t.points
                    targets.remove(t)

        for t in targets:
            t.move()
            if t.is_collide(gun) and not gun.invincible:
                score -= t.points
                gun.hit()
                last_hit_time = time.time()

        if time.time() - last_spawn_time > TARGET_SPAWN_DELAY and len(targets) < 5:
            last_spawn_time = time.time()
            target = bomber.strike()
            targets.append(target)

        if gun.color == RED and time.time() - last_hit_time > RED_DURATION:
            gun.color = TANK_COLOR
        if gun.invincible and time.time() - last_hit_time > INVINCIBLE_DURATION:
            gun.invincible = False

        gun.power_up()

pygame.quit()
