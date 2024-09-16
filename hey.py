import pygame

col = 50
line = 25

player = 1
bomb = 2

playerboard = []

for i in range(line):
    playerboard.append([])
    for j in range(col):
        playerboard[i].append(0)

for i in playerboard:
    print(i)

pygame.init()
X = col * 20
Y = line * 20

index_benni_row = 0
index_benni_col = 0

screen = pygame.display.set_mode((X, Y))

#beniimg
pygame.display.set_caption('image')
imp = pygame.image.load("pixil-frame-0.png").convert()

screen.blit(imp, (index_benni_row, index_benni_col))


pygame.display.flip()

working = True
while (working):

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


    screen.fill("yellow")
    screen.blit(imp, (index_benni_row, index_benni_col))
    pygame.display.update()



pygame.quit()
