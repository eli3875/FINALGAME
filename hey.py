import pygame
import random
import time

WON = False
BOMBA = False
TP = False
col = 50
row = 25
Y = int(col * 20)
X = int(row * 20)
run = True
start_timer = 0

KEYS = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

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

# bomb
pygame.display.set_caption('Lin')
bomb_pic = pygame.image.load("IMG_3500.jpeg")
bomb_pic = pygame.transform.scale(bomb_pic, (1000, 500))

# wiining
pygame.display.set_caption('Win')
WININGPIC = pygame.image.load("IMG_3506.png")
WININGPIC = pygame.transform.scale(WININGPIC, (1000, 500))

# Background
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (Y, X))

# background(grey)
background_grey = pygame.image.load("background(grey).png")
background_grey = pygame.transform.scale(background_grey, (Y, X))

# beni(grey)
beni_grey = pygame.image.load("beni(grey).png")
beni_grey = pygame.transform.scale(beni_grey, (player_size_x * 20, player_size_y * 20))

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
    bomb_list.append((bomb_row, bomb_col))

imp_bomb = pygame.image.load("bomb(grey).png")
imp_bomb = pygame.transform.scale(imp_bomb, (3 * 20, 1 * 20))

# shaked
pygame.display.set_caption('shaked')
shaked_size_width = 3
shaked_size_height = 4
imp_sked = pygame.image.load("sked.png")
imp_sked = pygame.transform.scale(imp_sked, (shaked_size_width * 20, shaked_size_height * 20))

for i in range(shaked_size_height):
    for j in range(shaked_size_width):
        playerboard[row - i - 1][col - j - 1] = 3

cotton_list = []
for cotton in range(20):
    cotton_row = random.randint(0, 24)
    cotton_col = random.randint(0, 49)
    playerboard[cotton_row][cotton_col] = 4
    cotton_list.append((cotton_row, cotton_col))
cotton_img = pygame.image.load("pixil-frame-0 (3).png")
cotton_img = pygame.transform.scale(cotton_img, (3 * 20, 3 * 20))



teleport_list = []
for teleport in range(5):
    teleport_row = random.randint(4, 20)
    teleport_col = random.randint(0, 49)
    playerboard[teleport_row][teleport_col] = 5
    teleport_list.append((teleport_row, teleport_col))
print(teleport_list)
print(teleport_list[0][0])

teleport_img = pygame.image.load("art.png")
teleport_img = pygame.transform.scale(teleport_img, (3 * 20, 1 * 20))

if playerboard[index_benni_row + 3][index_benni_col + 1] == 5:
    playerboard[index_benni_row][index_benni_col] = random.sample(teleport_list, 1)
for w in playerboard:
    print(w)
screen.blit(imp, (index_benni_row, index_benni_col))

working = True
while working:
    # screen.fill("dark green")
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            working = False

        # game functions
        if WON:
            print("won")
            working = False
            screen.blit(WININGPIC, (0, 0))
            pygame.display.update()
            time.sleep(4)

        # if BOMBA:
        #     screen.blit(bomb_pic, (0, 0))
        #     pygame.display.update()
        #     time.sleep(4)
        #     working = False

        # if TP:
        #     playerboard[index_benni_row][index_benni_col] = random.sample(teleport_list, 1)
        #     pygame.display.update()
        #     time.sleep(4)
        #     TP = False
        # movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            index_benni_col -= 1

            if index_benni_col < 0:
                index_benni_col = 0
            else:
                if playerboard[index_benni_row + 3][index_benni_col + 1] == 3:
                    WON = True
                if playerboard[index_benni_row + 3][index_benni_col + 1] == 2:
                    BOMBA = True
                if playerboard[index_benni_row + 3][index_benni_col] == 3:
                    WON = True
                if playerboard[index_benni_row + 3][index_benni_col] == 2:
                    BOMBA = True
                if playerboard[index_benni_row + 3][index_benni_col  -2] == 5:
                    ran = random.randint(0, 4)
                    ran2 = random.randint(0, 1)
                    index_benni_col = teleport_list[ran][ran2]
                    index_benni_row = teleport_list[ran][ran2] - 3
                    playerboard[teleport_list[0][0]][teleport_list[0][1]] = 1
                    playerboard[index_benni_row - 1][index_benni_col] = 0
                    # screen.blit(imp, (index_benni_col, index_benni_row))
                    # index_benni_col = 0
                    # index_benni_row = 0

                # playerboard[index_benni_row][index_benni_col] = 1
                # playerboard[index_benni_row][index_benni_col + 1] = 0

        if keys[pygame.K_RIGHT]:

            if index_benni_col < 48:
                index_benni_col += 1
                if playerboard[index_benni_row + 3][index_benni_col + 1] == 3:
                    WON = True
                if playerboard[index_benni_row + 3][index_benni_col + 1] == 2:
                    BOMBA = True
                if playerboard[index_benni_row + 3][index_benni_col] == 3:
                    WON = True
                if playerboard[index_benni_row + 3][index_benni_col] == 2:
                    BOMBA = True
                if playerboard[index_benni_row + 3][index_benni_col+ 1] == 5:
                    ran = random.randint(0, 4)
                    ran2 = random.randint(0, 1)
                    index_benni_col = teleport_list[ran][ran2]
                    index_benni_row = teleport_list[ran][ran2] - 3
                    playerboard[teleport_list[0][0]][teleport_list[0][1]] = 1
                    playerboard[index_benni_row - 1][index_benni_col] = 0

                # playerboard[index_benni_row][index_benni_col] = 1
                # playerboard[index_benni_row][index_benni_col - 1] = 0

            else:
                index_benni_col = 48

        if keys[pygame.K_UP]:

            if index_benni_row == 0:
                index_benni_row = 0


            else:
                index_benni_row -= 1
                if playerboard[index_benni_row + 3][index_benni_col + 1] == 3:
                    WON = True
                if playerboard[index_benni_row + 3][index_benni_col + 1] == 2:
                    BOMBA = True
                if playerboard[index_benni_row + 3][index_benni_col] == 3:
                    WON = True
                if playerboard[index_benni_row + 3][index_benni_col] == 2:
                    BOMBA = True
                if playerboard[index_benni_row + 3][index_benni_col] == 5 or playerboard[index_benni_row + 3][index_benni_col - 1] == 5 or playerboard[index_benni_row + 3][index_benni_col -2] == 5:
                    ran = random.randint(0, 4)
                    ran2 = random.randint(0, 1)
                    index_benni_col = teleport_list[ran][ran2]
                    index_benni_row = teleport_list[ran][ran2] - 3
                    playerboard[teleport_list[0][0]][teleport_list[0][1]] = 1
                    playerboard[index_benni_row - 1][index_benni_col] = 0


        if keys[pygame.K_DOWN]:

            if index_benni_row == 21:
                index_benni_row = 21

            else:
                index_benni_row += 1
                if playerboard[index_benni_row + 3][index_benni_col + 1] == 3:
                    WON = True
                if playerboard[index_benni_row + 3][index_benni_col + 1] == 2:
                    BOMBA = True
                if playerboard[index_benni_row + 3][index_benni_col] == 3:
                    WON = True
                if playerboard[index_benni_row + 3][index_benni_col] == 2:
                    BOMBA = True
                if playerboard[index_benni_row + 3][index_benni_col] == 5 or playerboard[index_benni_row + 3][index_benni_col - 1] == 5 or playerboard[index_benni_row + 3][index_benni_col -2] == 5:
                    ran = random.randint(0, 4)
                    ran2 = random.randint(0, 1)
                    index_benni_col = teleport_list[ran][1]
                    index_benni_row = teleport_list[ran][0] - 3
                    # playerboard[teleport_list[0][0]][teleport_list[0][1]] = 1
                    # playerboard[index_benni_row - 1][index_benni_col] = 0

        # if keys[pygame.K_0]:
        #     file = open("saving_game")
        #     file.write(
        #
        #     )

        if keys[pygame.K_RETURN]:
            screen.blit(background_grey, (0, 0))

            for rows in range(0, 1010, int(1000 / 50)):
                for cols in range(0, 510, int(500 / 25)):
                    rect11 = pygame.Rect(0, 0, rows, cols)
                    for i in bomb_list:
                        screen.blit(imp_bomb, ((i[1] * 1000 / 50), i[0] * 500 / 25))

                    pygame.draw.rect(screen, "black", rect11, 1)
                    screen.blit(beni_grey, (index_benni_col * 20, index_benni_row * 20))
                    screen.blit(imp_sked, (940, 420))

                    pygame.display.update()
            time.sleep(1)
        pygame.display.update()

        import json

        data = {
            'benicol': index_benni_col,
            'benirow': index_benni_row,
            'player_board_pos': playerboard,
            'cotoon': cotton_list,
            'bobmbaclob': bomb_list
        }

        if event.type == pygame.KEYDOWN:
            for i in KEYS:
                if event.key == i:
                    start_timer = pygame.time.get_ticks()
        if event.type == pygame.KEYUP:
            for i in range(len(KEYS)):
                if event.key == KEYS[i]:
                    end_timer = pygame.time.get_ticks()
                    if end_timer - start_timer >= 1000:
                        file = open("data_jason.txt"+ str(i), "r")
                        game_state = json.load(file)
                        index_benni_col = game_state['benicol']
                        index_benni_row = game_state['benirow']
                        playerboard = game_state['player_board_pos']
                        cotton_list = game_state['cotoon']
                        bomb_list = game_state['bobmbaclob']

                    else:
                        if end_timer - start_timer <= 1000:
                            file = open("data_jason.txt" + str(i), "w")
                            json.dump(data, file)
                        pygame.display.update()
                pygame.display.update()

        screen.blit(background, (0, 0))
        for i in cotton_list:
            screen.blit(cotton_img, ((i[1] * 1010 / 50), i[0] * 510 / 25))
        screen.blit(imp, (index_benni_col * 20, index_benni_row * 20))
        screen.blit(imp_sked, (940, 420))
        for i in teleport_list:
            screen.blit(teleport_img, ((i[1] * 1000 / 50), i[0] * 500 / 25))
        pygame.display.update()

pygame.quit()
