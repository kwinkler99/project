import pygame, sys
import random
import os.path
from pygame.locals import *


def DrawBoard(x, y, height, screen, color, line):
   pygame.draw.lines(screen, color, False, [(x,height), (y,height)], line)

##function ending gre
def END(screen, image, lista):
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
         if lista[2][i] != lista[2][i+1]:
            help += 1
         if lista[i][2] != lista[i+1][2]:
            help += 1

      if help == 8:
         return screen.blit(image, (1,100))

def arrow_up(lista):
   ##ARROW - UP

   ##moving blocks
   for i in range(3):
      for j in range(3):
         if lista[j][i] == 0:
            for k in range(j + 1, 3):
               if lista[k][i] != 0:
                  lista[j][i] = lista[k][i]
                  lista[k][i] = 0
                  break
   return lista



def main():
   # color
   grey = (0x99, 0x99, 0x99)
   black = (0x00, 0x00, 0x00)

   # useful data
   (width, height) = (300, 400)
   lista1 = [0, 0, 0]
   lista2 = [0, 0, 0]
   lista3 = [0, 0, 0]
   lista_main = [lista1, lista2, lista3]
   exit = 0
   move = 0
   copy = []
   safe = []

   # text
   text = 'Gra 2048'

   #pygame init
   pygame.init()

   #screen settings
   screen = pygame.display.set_mode((width, height))
   pygame.display.set_caption("Gra 2048")
   screen.fill(grey)
   DrawBoard(0, width, 0, screen, black, 199)
   font_size=pygame.font.SysFont("dejavusans", 20)
   text_render = font_size.render(text, 1, (250, 250, 250), None)

   #loading images
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

   #draw first block
   x=random.choice([0,100,200])
   y=random.choice([100,200,300])

   #safe first block to the list
   for j in range(0,3,1):
      for n in range(len(lista_main[j])):
         if (y == 100 and j == 0) or (y == 200 and j == 1) or (y == 300 and j == 2):
            if y == 100 and j == 0:
               if (x == 0 and n == 0) or (x == 100 and n == 1) or (x == 200 and n == 2):
                  lista_main[j][n] = 2
            if y == 200 and j == 1:
               if (x == 0 and n == 0) or (x == 100 and n == 1) or (x == 200 and n == 2):
                  lista_main[j][n] = 2
            if y == 300 and j == 2:
               if (x == 0 and n == 0) or (x == 100 and n == 1) or (x == 200 and n == 2):
                  lista_main[j][n] = 2


   #PLAY UNTIL EXIT
   while True:
      screen.blit(text_render, (width/3, (height-50)/9))


      for event in pygame.event.get():
         if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit()
         if event.type == KEYDOWN:
            safe = []
            for i in range(3):
               for j in range(3):
                  copy.append(lista_main[i][j])
               safe += [copy]
               copy = []
         if event.type == KEYUP:
            if event.key ==pygame.K_RIGHT:

               ##ARROW - RIGHT

               ##moving blocks
               for i in range(3):
                  for j in range(2, -1, -1):
                     if lista_main[i][j] == 0:
                        for k in range(j-1, -1, -1):
                           if lista_main[i][k] != 0:
                              lista_main[i][j] = lista_main[i][k]
                              lista_main[i][k] = 0
                              move = 1
                              break
               ##join blocks
               for i in range(3):
                  for j in range(2, 0, -1):
                     if lista_main[i][j] != 0 and lista_main[i][j] == lista_main[i][j-1]:
                        lista_main[i][j] += lista_main[i][j-1]
                        lista_main[i][j-1] = 0
                        move = 1
               ##repeat moving blocks
               for i in range(3):
                  for j in range(2, -1, -1):
                     if lista_main[i][j] == 0:
                        for k in range(j-1, -1, -1):
                           if lista_main[i][k] != 0:
                              lista_main[i][j] = lista_main[i][k]
                              lista_main[i][k] = 0
                              break

            if event.key == pygame.K_LEFT:

               ##ARROW - LEFT

               ##moving blocks
               for i in range(3):
                  for j in range(3):
                     if lista_main[i][j] == 0:
                        for k in range(j+1,3):
                           if lista_main[i][k] != 0:
                              lista_main[i][j] = lista_main[i][k]
                              lista_main[i][k] = 0
                              move = 1
                              break
               ##join blocks
               for i in range(3):
                  for j in range(2):
                     if lista_main[i][j] != 0 and lista_main[i][j] == lista_main[i][j+1]:
                        lista_main[i][j] += lista_main[i][j+1]
                        lista_main[i][j+1] = 0
                        move = 1
               ##repeat moving blocks
               for i in range(3):
                  for j in range(3):
                     if lista_main[i][j] == 0:
                        for k in range(j+1,3):
                           if lista_main[i][k] != 0:
                              lista_main[i][j] = lista_main[i][k]
                              lista_main[i][k] = 0
                              break

            if event.key == pygame.K_UP:

               ##ARROW - UP

               ##moving blocks
               arrow_up(lista_main)
               if safe != lista_main:
                  move = 1

               ##join blocks
               for i in range(3):
                  for j in range(2):
                     if lista_main[j][i] != 0 and lista_main[j][i] == lista_main[j+1][i]:
                        lista_main[j][i] += lista_main[j+1][i]
                        lista_main[j+1][i] = 0
                        move = 1
               ##repeat moving blocks
               arrow_up(lista_main)

            if event.key == pygame.K_DOWN:

               ##ARROW - DOWN

               ##moving blocks
               for i in range(3):
                  for j in range(2, -1, -1):
                     if lista_main[j][i] == 0:
                        for k in range(j - 1, -1, -1):
                           if lista_main[k][i] != 0:
                              lista_main[j][i] = lista_main[k][i]
                              lista_main[k][i] = 0
                              move = 1
                              break
               ##join blocks
               for i in range(3):
                  for j in range(2, 0, -1):
                     if (lista_main[j][i] != 0 and lista_main[j][i] == lista_main[j - 1][i]):
                        lista_main[j][i] += lista_main[j - 1][i]
                        lista_main[j - 1][i] = 0
                        move = 1
               ##repeat moving blocks
               for i in range(3):
                  for j in range(2, -1, -1):
                     if lista_main[j][i] == 0:
                        for k in range(j - 1, -1, -1):
                           if lista_main[k][i] != 0:
                              lista_main[j][i] = lista_main[k][i]
                              lista_main[k][i] = 0
                              break

            #creating new blocks
            if (event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == K_UP) and move == 1:
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

               ## reset screen and loading again
               screen.fill(grey)
               DrawBoard(0, width, 0, screen, black, 199)
               exit = 0

            # loading images
         for i in range(0, 3, 1):
            for j in range(0, 3, 1):
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

               if lista_main[i][j] == 2:
                  screen.blit(image_2, (x, y))
               if lista_main[i][j] == 4:
                  screen.blit(image_4, (x, y))
               if lista_main[i][j] == 8:
                  screen.blit(image_8, (x, y))
               if lista_main[i][j] == 16:
                  screen.blit(image_16, (x, y))
               if lista_main[i][j] == 32:
                  screen.blit(image_32, (x, y))
               if lista_main[i][j] == 64:
                  screen.blit(image_64, (x, y))
               if lista_main[i][j] == 128:
                  screen.blit(image_128, (x, y))
               if lista_main[i][j] == 256:
                  screen.blit(image_256, (x, y))
               if lista_main[i][j] == 512:
                  screen.blit(image_512, (x, y))
               if lista_main[i][j] == 1024:
                  screen.blit(image_1024, (x, y))
               if lista_main[i][j] == 2048:
                  screen.blit(image_2048, (x, y))
                  screen.blit(image_win,(0,100))

         END(screen, image_lose, lista_main)

      pygame.display.update()

#call function
main()