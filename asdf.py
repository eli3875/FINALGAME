import time
import pygame
import random
import time
import pygame
pygame.init()
import pygame
col = 50
line = 25
beni_size_x = 2
beni_size_y = 4
val = 1
screen_row = int((col * 20)+10)
screen_col = int((line * 20)+10)
player = 1
bomb = 2

index_benni_row = 0
index_benni_col = 0
pygame.display.set_caption("ben and sked")
imp = pygame.image.load("pixil-frame-0.png")
imp = pygame.transform.scale(imp, ((beni_size_x * 20,beni_size_y * 20)))

playerboard = []

for i in range(line):
    playerboard.append([])
    for j in range(col):
        playerboard[i].append(0)
        playerboard[index_benni_row][index_benni_col] = 1
        print("_____")

pygame.init()
for i in playerboard:
    print(i)
screen = pygame.display.set_mode((screen_row,screen_col))
working = True
while working:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            working = False
        screen.fill("dark green")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(imp, (index_benni_row, index_benni_col))
            index_benni_col -= val
            if index_benni_col < 0:
                index_benni_col = 0
            else:
                playerboard[index_benni_row][index_benni_col] = 1
                playerboard[index_benni_row][index_benni_col + 1] = 0
            for w in playerboard:
                print(w)
            print("----")
        if keys[pygame.K_RIGHT]:
            screen.blit(imp, (index_benni_row, index_benni_col))
            index_benni_col += val
            if index_benni_col < 50:
                playerboard[index_benni_row][index_benni_col] = 1
                playerboard[index_benni_row][index_benni_col - 1] = 0
            else:
                index_benni_col = 49
            for w in playerboard:
                print(w)
            print("----")
        if keys[pygame.K_UP]:
            screen.blit(imp, (index_benni_row, index_benni_col))
            index_benni_row -= val
            if index_benni_row < 0:
                index_benni_col = 0
            else:
                playerboard[index_benni_row][index_benni_col] = 1
                playerboard[index_benni_row +1][index_benni_col] = 0

            for w in playerboard:
                print(w)
            print("----")
        if keys[pygame.K_DOWN]:
            screen.blit(imp, (index_benni_row, index_benni_col))
            index_benni_row += val
            if index_benni_col < 25:
                playerboard[index_benni_row][index_benni_col] = 1
                playerboard[index_benni_row - 1][index_benni_col] = 0

            else:
                index_benni_row = 24
            playerboard[index_benni_row][index_benni_col] = 1
            for w in playerboard:
                print(w)
            print("----")

        # screen.blit(imp, (index_benni_row, index_benni_col))
    pygame.display.update()
    # x = 90

    # screen.fill("dark green")
    # screen.blit(imp, (index_benni_row, index_benni_col))
    # screen.blit(imp_sked, (index_sked_row, index_sked_col))
    # for rows in range(0 , screen_row,int(screen_row / 50)):
    #     for cols in range(0 , screen_col ,int(screen_col/25)):
    #         rect1 = pygame.Rect(0, 0, rows, cols)
    #         pygame.draw.rect(screen, "black", rect1, 1)


