import pygame
import random
import time

col = 50
row = 25
Y = int(col * 20)
X = int(row * 20)

val = 1


screen = pygame.display.set_mode((Y, X))

rectungle = pygame.Rect(30, 30, 60, 60)

# #beniimg
player_size_x = 2
player_size_y = 4
#
pygame.display.set_caption('beni')
imp = pygame.image.load("pixil-frame-0.png")
imp = pygame.transform.scale(imp, (player_size_x * 20, player_size_y * 20))
index_benni_row = 0
index_benni_col = 0
bomb_index_x = random.randint(0, 24)
bomb_index_y = random.randint(0, 49)
playerboard = []
print(bomb_index_x)
print(bomb_index_y)
for i in range(row):
    playerboard.append([])
    for j in range(col):
        playerboard[i].append(0)
        playerboard[index_benni_row][index_benni_col] = 1

for player_row in range(4):
    for player_col in range(2):
        playerboard[player_row][player_col] = 1


for bomb_times in range(20):
    playerboard[random.randint(0, 24)][random.randint(0, 49)] = 2


for w in playerboard:
    print(w)
screen.blit(imp, (index_benni_row, index_benni_col))
#shaked
pygame.display.set_caption('shaked')
imp_sked = pygame.image.load("sked.png")
imp_sked = pygame.transform.scale(imp_sked, (3 * 20, 4 * 20))

working = True
while working:
    screen.fill("dark green")
    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            working = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(imp, (index_benni_row, index_benni_col))
            player_size_x -= val
            if index_benni_col < 0:
                index_benni_col = 0

            else:
                # if playerboard[index_benni_row][index_benni_col] == 2: #need to add some thing to this
                #     screen.fill("blue")
                    # time.sleep(5)
                    # working = False
                for player_row in range(player_size_y):
                    for player_col in range(player_size_x):
                        playerboard[player_row][player_col] = 1
                        playerboard[player_row][player_col + 2] = 0
                        playerboard[player_row][player_col - 2] = 0
            for w in playerboard:
                print(w)
            print("----")
        if keys[pygame.K_RIGHT]:
            screen.blit(imp, (index_benni_row, index_benni_col))
            player_size_x += val
            if index_benni_col < 50:
                # if playerboard[index_benni_row][index_benni_col] == 2:
                #     screen.fill("blue")
                #     pygame.display.update()
                #     time.sleep(5)
                #     working = False
                # else:    # working = False
                for player_row in range(player_size_y):
                    for player_col in range(player_size_x):
                        playerboard[player_row][player_col] = 1
                        playerboard[player_row][player_col - 2] = 0
            else:
                index_benni_col = 49
            for w in playerboard:
                print(w)
            print("----")
        if keys[pygame.K_UP]:
            screen.blit(imp, (index_benni_row, index_benni_col))
            player_size_y -= val
            if index_benni_row < 0:
                index_benni_col = 0
            else:
                # if playerboard[index_benni_row][index_benni_col] == 2:
                #     screen.fill("blue")
                    # time.sleep(5)
                    # working = False
                for player_row in range(player_size_y):
                    for player_col in range(player_size_x):
                        playerboard[player_row][player_col] = 1
                        playerboard[player_row + 2][player_col] = 0
                        playerboard[player_row - 2][player_col] = 0

            for w in playerboard:
                print(w)
            print("----")
        if keys[pygame.K_DOWN]:
            screen.blit(imp, (index_benni_row, index_benni_col))
            player_size_x += val
            if index_benni_col < 25:
                if playerboard[index_benni_row][index_benni_col] == 2:
                    screen.fill("red")
                    # time.sleep(5)
                    # working = False
                for player_row in range(player_size_y):
                    for player_col in range(player_size_x):
                        playerboard[player_row][player_col] = 1
                        playerboard[player_row][player_col + 2] = 0
                        playerboard[player_row][player_col - 2] = 0


            else:
                index_benni_row = 24
            playerboard[index_benni_row][index_benni_col] = 1
            for w in playerboard:
                print(w)
            print("----")

        if keys[pygame.K_END]:
            screen.fill("dark grey")
            for rows in range(0, 1010, int(1010 / 50)):
                for cols in range(0, 510, int(510 / 25)):
                    rect11 = pygame.Rect(0, 0, rows, cols)

                    pygame.draw.rect(screen, "black", rect11, 1)
                    screen.blit(imp, (index_benni_row, index_benni_col))
                    screen.blit(imp_sked, (940, 420))

                pygame.display.update()
            time.sleep(1)
            pygame.display.update()
    screen.blit(imp, (index_benni_row, index_benni_col))
    screen.blit(imp_sked, (940, 420))
    pygame.display.update()
    pygame.display.update()
# pygame.quit()