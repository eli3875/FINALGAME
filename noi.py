import pygame
import random
import time

col = 50
row = 25
Y = int(col * 20)
X = int(row * 20)

#
pygame.init()

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

playerboard = []

for i in range(row):
    playerboard.append([])
    for j in range(col):
        playerboard[i].append(0)
        playerboard[index_benni_row][index_benni_col] = 1
bomb_list = []
for bomb_times in range(20):
    bomb_row = random.randint(0, 24)
    bomb_col = random.randint(0, 49)
    playerboard[bomb_row][bomb_col] = 2
    bomb_list.append((bomb_row,bomb_col))




screen.blit(imp, (index_benni_row, index_benni_col))
# shaked
# pygame.display.set_caption('shaked')
imp_sked = pygame.image.load("skeddd.png")
imp_sked = pygame.transform.scale(imp_sked, (3 * 20, 4 * 20))


#cotton
cotton_list = []
for cotton in range(20):
    cotton_row = random.randint(0, 24)
    cotton_col = random.randint(0, 49)
    playerboard[cotton_row][cotton_col] = 4
    cotton_list.append((cotton_row, cotton_col))
cotton_img = pygame.image.load("pixil-frame-0 (3).png")
cotton_img = pygame.transform.scale(cotton_img, (3 * 20, 3 * 20))
for w in playerboard:
    print(w)



#bomb
imp_bomb = pygame.image.load("bomb.png")
imp_bomb = pygame.transform.scale(imp_bomb, (3 * 20, 1 * 20))



#background
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (Y, X))


#background(grey)
background_grey = pygame.image.load("background(grey).png")
background_grey = pygame.transform.scale(background_grey, (Y, X))



#beni(grey)
beni_grey = pygame.image.load("beni(grey).png")
beni_grey = pygame.transform.scale(beni_grey, (player_size_x * 20, player_size_y * 20))


working = True
while working:
    # screen.fill("dark green")
    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            working = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            index_benni_col -= 1

            if index_benni_col < 0:
                index_benni_col = 0
            else:
                if playerboard[index_benni_row][index_benni_col] in bomb_list: #need to add some thing to this
                    screen.fill("blue")
                    time.sleep(5)
                    working = False
                playerboard[index_benni_row][index_benni_col] = 1
                playerboard[index_benni_row][index_benni_col + 1] = 0

            for w in playerboard:
                print(w)
            print("----")
        if keys[pygame.K_RIGHT]:

            if index_benni_col < 48:
                index_benni_col += 1
                playerboard[index_benni_row][index_benni_col] = 1
                playerboard[index_benni_row][index_benni_col - 1] = 0


            else:
                index_benni_col = 48

            for w in playerboard:
                print(w)
            print("----")
        if keys[pygame.K_UP]:


            if index_benni_row == 0:
                index_benni_row = 0


            else:
                index_benni_row -= 1
                playerboard[index_benni_row][index_benni_col] = 1
                playerboard[index_benni_row + 1][index_benni_col] = 0

            for w in playerboard:
                print(w)
            print("----")
        if keys[pygame.K_DOWN]:

            if index_benni_row == 21:
                index_benni_row = 21


            else:
                index_benni_row += 1
                playerboard[index_benni_row][index_benni_col] = 1
                playerboard[index_benni_row - 1][index_benni_col] = 0

            for w in playerboard:
                print(w)
            print("----")

        if keys[pygame.K_END]:
            screen.blit(background_grey, (0,0))
            for rows in range(0, 1010, int(1010 / 50)):
                for cols in range(0, 510, int(510 / 25)):
                    rect11 = pygame.Rect(0, 0, rows, cols)

                    pygame.draw.rect(screen, "black", rect11, 1)
                    screen.blit(beni_grey, (index_benni_col * 20, index_benni_row * 20))
                    screen.blit(imp_sked, (940, 420))
                for i in bomb_list:
                    screen.blit(imp_bomb, ((i[1] * 1000 / 50),i[0] * 500/25))

                pygame.display.update()
            time.sleep(1)
            pygame.display.update()
        screen.blit(background, (0, 0))
        screen.blit(imp, (index_benni_col * 20, index_benni_row * 20))
        screen.blit(imp_sked, (940, 420))
        for i in cotton_list:
            screen.blit(cotton_img, ((i[1] * 1010 / 50), i[0] * 510 / 25))
        pygame.display.update()
        pygame.display.update()