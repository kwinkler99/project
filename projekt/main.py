import os.path
import random
import pygame
import sys
from pygame.locals import *

global str

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
FPS = 300
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
    text_new_game = font_size1.render(", n - nowa gra", 1, (250, 250, 250), None)

    screen.fill(grey)
    DrawBoard(0, width, 0, screen, black, 199)
    screen.blit(text_render, (width / 3, 10))
    screen.blit(text_new_game, (160, 40))
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


def join_block_RIGHT(lista, screen, points):
    for i in range(3):
        for j in range(2, 0, -1):
            if lista[i][j] != 0 and lista[i][j] == lista[i][j - 1]:
                animation_arrow_RIGHT(j - 1, i, j, lista, screen, points)
                lista[i][j] += lista[i][j - 1]
                lista[i][j - 1] = 0
                points += lista[i][j]
    return points


def join_block_LEFT(lista, screen, points):
    for i in range(3):
        for j in range(2):
            if lista[i][j] != 0 and lista[i][j] == lista[i][j + 1]:
                animation_arrow_LEFT(j + 1, i, j, lista, screen, points)
                lista[i][j] += lista[i][j + 1]
                lista[i][j + 1] = 0
                points += lista[i][j]
    return points


def join_block_UP(lista, screen, points):
    for i in range(3):
        for j in range(2):
            if lista[j][i] != 0 and lista[j][i] == lista[j + 1][i]:
                animation_arrow_UP(j + 1, i, j, lista, screen, points)
                lista[j][i] += lista[j + 1][i]
                lista[j + 1][i] = 0
                points += lista[j][i]
    return points


def join_block_DOWN(lista, screen, points):
    for i in range(3):
        for j in range(2, 0, -1):
            if lista[j][i] != 0 and lista[j][i] == lista[j - 1][i]:
                animation_arrow_DOWN(j - 1, i, j, lista, screen, points)
                lista[j][i] += lista[j - 1][i]
                lista[j - 1][i] = 0
                points += lista[j][i]
    return points


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
def checking_move(safe, lista, move):
    if safe != lista:
        move = 1
    return move


def checking_position(i, j):
    x = 0
    y = 0
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
    letter = ''
    (width, height) = (300, 400)
    lista_ranking = []
    exit = 0
    move = 0
    q = 0
    n = 0

    # pygame init
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Gra 2048")
    screen.fill(grey)

    # screen settings
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Gra 2048")

    # PLAY UNTIL EXIT
    while True:
        while q != 1:
            screen.fill(grey)
            DrawBoard(0, width, 0, screen, black, 199)
            ranking = {'nick': '', 'punktacja': 0}
            name = ''
            copy = []
            copy_score = ''
            safe = []
            points = 0
            x = 45
            lista1 = [0, 0, 0]
            lista2 = [0, 0, 0]
            lista3 = [0, 0, 0]
            lista_main = [lista1, lista2, lista3]
            n = 0
            enter = 0

            # ranking
            while enter != 1:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == event.key == pygame.K_ESCAPE:
                            enter = 1
                            ranking['nick'] = name
                        if event.key == pygame.K_q:
                            letter = 'q'
                            x += 10
                            name += 'q'
                        if event.key == pygame.K_w:
                            letter = 'w'
                            x += 10
                            name += 'w'
                        if event.key == pygame.K_e:
                            letter = 'e'
                            x += 10
                            name += 'e'
                        if event.key == pygame.K_r:
                            letter = 'r'
                            x += 10
                            name += 'r'
                        if event.key == pygame.K_t:
                            letter = 't'
                            x += 10
                            name += 't'
                        if event.key == pygame.K_y:
                            letter = 'y'
                            x += 10
                            name += 'y'
                        if event.key == pygame.K_u:
                            letter = 'u'
                            x += 10
                            name += 'u'
                        if event.key == pygame.K_i:
                            letter = 'i'
                            x += 10
                            name += 'i'
                        if event.key == pygame.K_o:
                            letter = 'o'
                            x += 10
                            name += 'o'
                        if event.key == pygame.K_p:
                            letter = 'p'
                            x += 10
                            name += 'p'
                        if event.key == pygame.K_a:
                            letter = 'a'
                            x += 10
                            name += 'a'
                        if event.key == pygame.K_s:
                            letter = 's'
                            x += 10
                            name += 's'
                        if event.key == pygame.K_d:
                            letter = 'd'
                            x += 10
                            name += 'd'
                        if event.key == pygame.K_f:
                            letter = 'f'
                            x += 10
                            name += 'f'
                        if event.key == pygame.K_g:
                            letter = 'g'
                            x += 10
                            name += 'g'
                        if event.key == pygame.K_h:
                            letter = 'h'
                            x += 10
                            name += 'h'
                        if event.key == pygame.K_j:
                            letter = 'j'
                            x += 10
                            name += 'j'
                        if event.key == pygame.K_k:
                            letter = 'k'
                            x += 10
                            name += 'k'
                        if event.key == pygame.K_l:
                            letter = 'l'
                            x += 10
                            name += 'l'
                        if event.key == pygame.K_z:
                            letter = 'z'
                            x += 10
                            name += 'z'
                        if event.key == pygame.K_x:
                            letter = 'x'
                            x += 10
                            name += 'x'
                        if event.key == pygame.K_c:
                            letter = 'c'
                            x += 10
                            name += 'c'
                        if event.key == pygame.K_v:
                            letter = 'v'
                            x += 10
                            name += 'v'
                        if event.key == pygame.K_b:
                            letter = 'b'
                            x += 10
                            name += 'b'
                        if event.key == pygame.K_n:
                            letter = 'n'
                            x += 10
                            name += 'n'
                        if event.key == pygame.K_m:
                            letter = 'm'
                            x += 10
                            name += 'm'
                        if event.key == pygame.K_SPACE:
                            letter = ' '
                            x += 10
                            name += 'm'

                font = pygame.font.SysFont('arial', 18)
                letter_print = font.render(letter, 1, (250, 250, 250), None)
                nick = font.render('Nick: ', 1, (250, 250, 250), None)
                screen.blit(nick, (10, 10))
                screen.blit(letter_print, (x, 10))
                if letter == 'i' or letter == 'j' or letter == 'l' or letter == 't' or letter == 'f' or letter == 'r':
                    x -= 5
                if letter == 'm' or letter == 'w':
                    x += 5
                letter = ''
                pygame.display.update()

            # safe first block
            first_block(lista_main)
            load_screen(screen, points, lista_main, 4, 4)
            while n != 1:
                load_screen(screen, points, lista_main, 4, 4)
                if END(lista_main):
                    q = 1
                    screen.blit(image_lose, (1, 100))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        q = 1
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_n:
                            n = 1
                        if event.key != pygame.K_u:
                            safe = []
                            # safe sie aktualizuje za kazdym razem niezaleznie od zapisu wiec trzeba uzyc for
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
                            move = checking_move(safe, lista_main, move)
                            # join blocks
                            points = join_block_RIGHT(lista_main, screen, points)
                            move = checking_move(safe, lista_main, move)
                            # repeat moving blocks
                            arrow_right(lista_main, screen, points)

                        if event.key == pygame.K_LEFT:
                            # ARROW - LEFT

                            # moving blocks
                            arrow_left(lista_main, screen, points)
                            move = checking_move(safe, lista_main, move)
                            # join blocks
                            points = join_block_LEFT(lista_main, screen, points)
                            move = checking_move(safe, lista_main, move)
                            # repeat moving blocks
                            arrow_left(lista_main, screen, points)

                        if event.key == pygame.K_UP:
                            # ARROW - UP

                            # moving blocks
                            arrow_up(lista_main, screen, points)
                            move = checking_move(safe, lista_main, move)
                            # join blocks
                            points = join_block_UP(lista_main, screen, points)
                            move = checking_move(safe, lista_main, move)
                            # repeat moving blocks
                            arrow_up(lista_main, screen, points)

                        if event.key == pygame.K_DOWN:
                            # ARROW - DOWN

                            # moving blocks
                            arrow_down(lista_main, screen, points)
                            move = checking_move(safe, lista_main, move)
                            # join blocks
                            points = join_block_DOWN(lista_main, screen, points)
                            move = checking_move(safe, lista_main, move)
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
                                                    if (x == 0 and n == 0) or (x == 100 and n == 1) or (
                                                            x == 200 and n == 2):
                                                        lista_main[j][n] = 2
                                                        exit = 1
                                                        move = 0
                                                if y == 200 and j == 1:
                                                    if (x == 0 and n == 0) or (x == 100 and n == 1) or (
                                                            x == 200 and n == 2):
                                                        lista_main[j][n] = 2
                                                        exit = 1
                                                        move = 0
                                                if y == 300 and j == 2:
                                                    if (x == 0 and n == 0) or (x == 100 and n == 1) or (
                                                            x == 200 and n == 2):
                                                        lista_main[j][n] = 2
                                                        exit = 1
                                                        move = 0

                            #  reset screen and loading again
                            exit = 0

                pygame.display.update()
            ranking['punktacja'] = points
            lista_ranking.append(ranking)
            print(lista_ranking)

        if n == 0:
            screen.blit(image_lose, (1, 100))
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    q = 1
                    sys.exit()


# call function
main()
