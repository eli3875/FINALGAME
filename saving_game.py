import pygame

import random
import time
start_timer = 0
run = False
pygame.init()
# while run == True:
    # yvalue += 1

screen = pygame.display.set_mode(((50 * 20), (25 * 20)))
working = True
while working:
    # screen.fill("dark green")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                start_timer = pygame.time.get_ticks()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_0:
                end_timer = pygame.time.get_ticks()
                if end_timer - start_timer >= 1000:
                    print("highr")
                else:
                    if end_timer - start_timer <= 1000:
                        print("lower")

