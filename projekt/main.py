import os.path
import random
import pygame
import sys
from pygame.locals import *

# color
grey = (0x99, 0x99, 0x99)
black = (0x00, 0x00, 0x00)

# text
text = 'Gra 2048'

# loading images
image_2 = pygame.image.load(os.path.join("Number", "2.bmp"))
image_4 = pygame.image.load(os.path.join("Number", "4.bmp"))
image_8 = pygame.image.load(os.path.join("Number", "8.bmp"))
image_16 = pygame.image.load(os.path.join("Number", "16.bmp"))
image_32 = pygame.image.load(os.path.join("Number", "32.bmp"))
image_64 = pygame.image.load(os.path.join("Number", "64.bmp"))
image_128 = pygame.image.load(os.path.join("Number", "128.bmp"))
image_256 = pygame.image.load(os.path.join("Number", "256.bmp"))
image_512 = pygame.image.load(os.path.join("Number", "512.bmp"))
image_1024 = pygame.image.load(os.path.join("Number", "1024.bmp"))
image_2048 = pygame.image.load(os.path.join("Number", "2048.bmp"))
image_lose = pygame.image.load(os.path.join("Number", "Przegrales.jpg"))
image_win = pygame.image.load(os.path.join("Number", "Wygrales.jpg"))

# data
FPS = 150
fpsClock = pygame.time.Clock()


def DrawBoard(x, y, height, screen, color, line):
    pygame.draw.lines(screen, color, False, [(x, height), (y, height)], line)


# function ending game
def END(lista):
    help = 0
    n = 0
    for k in range(3):
        for h in range(3):
            if lista[k][h] != 0:
                n += 1
    if n == 9:
        for i in range(2):
            for j in range(2):
                if lista[i][j] != lista[i][j + 1] and lista[i][j] != lista[i + 1][j]:
                    help += 1
            if lista[2][i] != lista[2][i + 1]:
                help += 1
            if lista[i][2] != lista[i + 1][2]:
                help += 1

        if help == 8:
            return True


def load_screen(screen, points, lista, movex, movey):
    (width, height) = (300, 400)
    font_size = pygame.font.SysFont("dejavusans", 20)
    font_size1 = pygame.font.SysFont('arial', 18)
    text_render = font_size.render(text, 1, (250, 250, 250), None)
    text_map = font_size1.render("u - cofnięcie ruchu", 1, (250, 250, 250), None)
    text_time = font_size1.render("Czas: ", 1, (250, 250, 250), None)
    text_score = font_size1.render("Punktacja: ", 1, (250, 250, 250), None)

    screen.fill(grey)
    DrawBoard(0, width, 0, screen, black, 199)
    screen.blit(text_render, (width / 3, 10))
    screen.blit(text_map, (10, 40))
    screen.blit(text_score, (10, 60))
    screen.blit(text_time, (10, 80))
    score(screen, points)
    time(screen)
    for i in range(3):
        for j in range(3):
            if i != movex or j != movey:
                image(lista, screen, i, j)


def image(lista_main, screen, i, j):
    position = checking_position(i, j)

    if lista_main[i][j] == 2:
        screen.blit(image_2, position)
    if lista_main[i][j] == 4:
        screen.blit(image_4, position)
    if lista_main[i][j] == 8:
        screen.blit(image_8, position)
    if lista_main[i][j] == 16:
        screen.blit(image_16, position)
    if lista_main[i][j] == 32:
        screen.blit(image_32, position)
    if lista_main[i][j] == 64:
        screen.blit(image_64, position)
    if lista_main[i][j] == 128:
        screen.blit(image_128, position)
    if lista_main[i][j] == 256:
        screen.blit(image_256, position)
    if lista_main[i][j] == 512:
        screen.blit(image_512, position)
    if lista_main[i][j] == 1024:
        screen.blit(image_1024, position)
    if lista_main[i][j] == 2048:
        screen.blit(image_2048, position)
        screen.blit(image_win, (0, 100))


def image_for_the_arrows(i, k, x, y, screen, lista):
    if lista[k][i] == 2:
        screen.blit(image_2, (x, y))
    if lista[k][i] == 4:
        screen.blit(image_4, (x, y))
    if lista[k][i] == 8:
        screen.blit(image_8, (x, y))
    if lista[k][i] == 16:
        screen.blit(image_16, (x, y))
    if lista[k][i] == 32:
        screen.blit(image_32, (x, y))
    if lista[k][i] == 64:
        screen.blit(image_64, (x, y))
    if lista[k][i] == 128:
        screen.blit(image_128, (x, y))
    if lista[k][i] == 256:
        screen.blit(image_256, (x, y))
    if lista[k][i] == 512:
        screen.blit(image_512, (x, y))
    if lista[k][i] == 1024:
        screen.blit(image_1024, (x, y))
    if lista[k][i] == 2048:
        screen.blit(image_2048, (x, y))
        screen.blit(image_win, (0, 100))
    pygame.display.update()
    fpsClock.tick(FPS)


def animation_arrow_UP(k, i, j, lista, screen, points):
    (x, y) = checking_position(k, i)
    z = y
    while y != z - (k - j) * 100:
        y -= 5
        image_for_the_arrows(i, k, x, y, screen, lista)
        load_screen(screen, points, lista, k, i)


def animation_arrow_DOWN(k, i, j, lista, screen, points):
    (x, y) = checking_position(k, i)
    z = y
    while y != z + (j - k) * 100:
        y += 5
        image_for_the_arrows(i, k, x, y, screen, lista)
        load_screen(screen, points, lista, k, i)


def animation_arrow_LEFT(k, i, j, lista, screen, points):
    (x, y) = checking_position(i, k)
    z = x
    while x != z - (k - j) * 100:
        x -= 5
        image_for_the_arrows(k, i, x, y, screen, lista)
        load_screen(screen, points, lista, i, k)


def animation_arrow_RIGHT(k, i, j, lista, screen, points):
    (x, y) = checking_position(i, k)
    z = x
    while x != z - (k - j) * 100:
        x += 5
        image_for_the_arrows(k, i, x, y, screen, lista)
        load_screen(screen, points, lista, i, k)


# ARROW
def arrow_up(lista, screen, points):
    for i in range(3):
        for j in range(3):

            if lista[j][i] == 0:
                for k in range(j + 1, 3):
                    if lista[k][i] != 0:
                        animation_arrow_UP(k, i, j, lista, screen, points)
                        lista[j][i] = lista[k][i]
                        lista[k][i] = 0
                        break
    return lista


def arrow_down(lista, screen, points):
    for i in range(3):
        for j in range(2, -1, -1):
            if lista[j][i] == 0:
                for k in range(j - 1, -1, -1):
                    if lista[k][i] != 0:
                        animation_arrow_DOWN(k, i, j, lista, screen, points)
                        lista[j][i] = lista[k][i]
                        lista[k][i] = 0
                        break
    return lista


def arrow_right(lista, screen, points):
    for i in range(3):
        for j in range(2, -1, -1):
            if lista[i][j] == 0:
                for k in range(j - 1, -1, -1):
                    if lista[i][k] != 0:
                        animation_arrow_RIGHT(k, i, j, lista, screen, points)
                        lista[i][j] = lista[i][k]
                        lista[i][k] = 0
                        break


def arrow_left(lista, screen, points):
    for i in range(3):
        for j in range(3):
            if lista[i][j] == 0:
                for k in range(j + 1, 3):
                    if lista[i][k] != 0:
                        animation_arrow_LEFT(k, i, j, lista, screen, points)
                        lista[i][j] = lista[i][k]
                        lista[i][k] = 0
                        break
    return lista


############################
def checking_position(i, j):
    if i == 0 and j == 0:
        x = 0
        y = 100
    elif i == 0 and j == 1:
        x = 100
        y = 100
    elif i == 0 and j == 2:
        x = 200
        y = 100

    elif i == 1 and j == 0:
        x = 0
        y = 200
    elif i == 1 and j == 1:
        x = 100
        y = 200
    elif i == 1 and j == 2:
        x = 200
        y = 200

    elif i == 2 and j == 0:
        x = 0
        y = 300
    elif i == 2 and j == 1:
        x = 100
        y = 300
    elif i == 2 and j == 2:
        x = 200
        y = 300
    return x, y


def score(screen, points):
    font = pygame.font.SysFont('arial', 18)
    screen.blit(font.render(str(points), 1, (255, 255, 255)), (100, 60))


def time(screen):
    font = pygame.font.SysFont('arial', 18)
    if (pygame.time.get_ticks() // 1000) % 60 < 10:
        time = font.render(
            str((pygame.time.get_ticks() // 1000) // 60) + ':' + '0' + str((pygame.time.get_ticks() // 1000) % 60), 1,
            (250, 250, 250))
    else:
        time = font.render(
            str((pygame.time.get_ticks() // 1000) // 60) + ':' + str((pygame.time.get_ticks() // 1000) % 60), 1,
            (250, 250, 250))

    screen.blit(time, (60, 80))


def first_block(lista):
    # draw first block
    x = random.choice([0, 100, 200])
    y = random.choice([100, 200, 300])

    # safe first block to the list
    for j in range(0, 3, 1):
        for n in range(len(lista[j])):
            if (y == 100 and j == 0) or (y == 200 and j == 1) or (y == 300 and j == 2):
                if y == 100 and j == 0:
                    if (x == 0 and n == 0) or (x == 100 and n == 1) or (x == 200 and n == 2):
                        lista[j][n] = 2
                if y == 200 and j == 1:
                    if (x == 0 and n == 0) or (x == 100 and n == 1) or (x == 200 and n == 2):
                        lista[j][n] = 2
                if y == 300 and j == 2:
                    if (x == 0 and n == 0) or (x == 100 and n == 1) or (x == 200 and n == 2):
                        lista[j][n] = 2


# GAME
def main():
    # useful data
    (width, height) = (300, 400)
    exit = 0
    move = 0
    copy = []
    copy_score = ''
    safe = []
    points = 0
    lista1 = [0, 0, 0]
    lista2 = [0, 0, 0]
    lista3 = [0, 0, 0]
    lista_main = [lista1, lista2, lista3]

    # pygame init
    pygame.init()

    # screen settings
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Gra 2048")
    screen.fill(grey)
    DrawBoard(0, width, 0, screen, black, 199)

    # safe first block
    first_block(lista_main)

    # PLAY UNTIL EXIT
    while True:
        load_screen(screen, points, lista_main, 4, 4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit()
            if event.type == KEYDOWN:
                if event.key != pygame.K_u:
                    safe = []
                    for i in range(3):
                        for j in range(3):
                            copy.append(lista_main[i][j])
                        safe += [copy]
                        copy = []
                    copy_score = points
            if event.type == KEYUP:
                if event.key == pygame.K_u and safe != []:
                    lista_main = safe
                    points = copy_score
                    screen.fill(grey)
                    DrawBoard(0, width, 0, screen, black, 199)
                if event.key == pygame.K_RIGHT:

                    # ARROW - RIGHT

                    # moving blocks
                    arrow_right(lista_main, screen, points)
                    if safe != lista_main:
                        move = 1
                    # join blocks
                    for i in range(3):
                        for j in range(2, 0, -1):
                            if lista_main[i][j] != 0 and lista_main[i][j] == lista_main[i][j - 1]:
                                lista_main[i][j] += lista_main[i][j - 1]
                                lista_main[i][j - 1] = 0
                                points += lista_main[i][j]
                                move = 1

                    # repeat moving blocks
                    arrow_right(lista_main, screen, points)

                if event.key == pygame.K_LEFT:

                    # ARROW - LEFT

                    # moving blocks
                    arrow_left(lista_main, screen, points)
                    if safe != lista_main:
                        move = 1
                    # join blocks
                    for i in range(3):
                        for j in range(2):
                            if lista_main[i][j] != 0 and lista_main[i][j] == lista_main[i][j + 1]:
                                lista_main[i][j] += lista_main[i][j + 1]
                                lista_main[i][j + 1] = 0
                                points += lista_main[i][j]
                                move = 1
                    # repeat moving blocks
                    arrow_left(lista_main, screen, points)

                if event.key == pygame.K_UP:

                    # ARROW - UP

                    # moving blocks
                    arrow_up(lista_main, screen, points)
                    if safe != lista_main:
                        move = 1
                    # join blocks
                    for i in range(3):
                        for j in range(2):
                            if lista_main[j][i] != 0 and lista_main[j][i] == lista_main[j + 1][i]:
                                lista_main[j][i] += lista_main[j + 1][i]
                                lista_main[j + 1][i] = 0
                                points += lista_main[j][i]
                                move = 1
                    # repeat moving blocks
                    arrow_up(lista_main, screen, points)

                if event.key == pygame.K_DOWN:

                    # ARROW - DOWN

                    # moving blocks
                    arrow_down(lista_main, screen, points)
                    if safe != lista_main:
                        move = 1
                    # join blocks
                    for i in range(3):
                        for j in range(2, 0, -1):
                            if lista_main[j][i] != 0 and lista_main[j][i] == lista_main[j - 1][i]:
                                lista_main[j][i] += lista_main[j - 1][i]
                                lista_main[j - 1][i] = 0
                                points += lista_main[j][i]
                                move = 1
                    # repeat moving blocks
                    arrow_down(lista_main, screen, points)

                # creating new blocks
                if (
                        event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == K_UP) and move == 1:

                    while exit == 0:
                        x = random.choice([0, 100, 200])
                        y = random.choice([100, 200, 300])
                        for j in range(0, 3, 1):
                            for n in range(len(lista_main)):
                                if lista_main[j][n] == 0:
                                    if (y == 100 and j == 0) or (y == 200 and j == 1) or (y == 300 and j == 2):
                                        if y == 100 and j == 0:
                                            if (x == 0 and n == 0) or (x == 100 and n == 1) or (x == 200 and n == 2):
                                                lista_main[j][n] = 2
                                                exit = 1
                                                move = 0
                                        if y == 200 and j == 1:
                                            if (x == 0 and n == 0) or (x == 100 and n == 1) or (x == 200 and n == 2):
                                                lista_main[j][n] = 2
                                                exit = 1
                                                move = 0
                                        if y == 300 and j == 2:
                                            if (x == 0 and n == 0) or (x == 100 and n == 1) or (x == 200 and n == 2):
                                                lista_main[j][n] = 2
                                                exit = 1
                                                move = 0

                    #  reset screen and loading again
                    screen.fill(grey)
                    exit = 0

            if END(lista_main):
                screen.blit(image_lose, (1, 100))

        pygame.display.update()


# call function
main()
