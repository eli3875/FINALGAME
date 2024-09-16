import pygame
pygame.init()
import pygame
col = 50
line = 25
beni_size_x = 2
beni_size_y = 4

screen_row = int((col * 20)+10)
screen_col = int((line * 20)+10)
player = 1
bomb = 2

index_benni_row = 0
index_benni_col = 0

playerboard = []

for i in range(line):
    playerboard.append([])
    for j in range(col):
        playerboard[i].append(0)

pygame.init()
for i in playerboard:
    print(i)
screen = pygame.display.set_mode((screen_row,screen_col))
pygame.display.set_caption("ben and sked")
imp = pygame.image.load("pixil-frame-0.png")
imp = pygame.transform.scale(imp, ((beni_size_x * 20,beni_size_y * 20)))
#sked
sked_size_x = 3
sked_size_y = 4
index_sked_row = 920
index_sked_col = 410
imp_sked = pygame.image.load("sked.png")
imp_sked = pygame.transform.scale(imp_sked, ((sked_size_x * 20,(sked_size_y * 20))))
#bomb
imp_bomb = pygame.image.load("bomb.png")
working = True
while working:

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            working = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        index_benni_row -= 1

    if keys[pygame.K_RIGHT]:
        index_benni_row += 1

    if keys[pygame.K_UP]:
        index_benni_col -= 1

    if keys[pygame.K_DOWN]:
        index_benni_col += 1
    x = 90

    screen.fill("dark green")
    screen.blit(imp, (index_benni_row, index_benni_col))
    screen.blit(imp_sked, (index_sked_row, index_sked_col))
    for rows in range(0 , screen_row,int(screen_row / 50)):
        for cols in range(0 , screen_col ,int(screen_col/25)):
            rect1 = pygame.Rect(0, 0, rows, cols)
            pygame.draw.rect(screen, "black", rect1, 1)
    pygame.display.update()

