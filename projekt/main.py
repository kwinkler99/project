import pygame, sys
import random
import os.path
from pygame.locals import *


def DrawBoard(x, y, height, screen, color, line):
   pygame.draw.lines(screen, color, False, [(x,height), (y,height)], line)


def main():
   # color
   white = (255, 255, 255)
   grey = (0x99, 0x99, 0x99)
   black = (0x00, 0x00, 0x00)
   red = (255, 0, 0)

   # useful data
   (width, height) = (300, 400)
   lista1 = [0, 0, 0]
   lista2 = [0, 0, 0]
   lista3 = [0, 0, 0]
   lista_main = [lista1, lista2, lista3]
   exit = 0

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

   #draw first block
   x=random.choice([0,100,200])
   y=random.choice([100,200,300])

   #safe first block to the list
   for j in range(0,3,1):
      for n, i in enumerate(lista_main[j]):
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
            #creating new blocks
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == K_UP:
               while exit == 0:
                  x = random.choice([0, 100, 200])
                  y = random.choice([100, 200, 300])
                  for j in range(0, 3, 1):
                     for n, i in enumerate(lista_main[j]):
                        if lista_main[j][n] == 0:
                           if (y == 100 and j == 0) or (y == 200 and j == 1) or (y == 300 and j == 2):
                              if y == 100 and j == 0:
                                 if (x == 0 and n == 0) or (x == 100 and n == 1) or (x == 200 and n == 2):
                                    lista_main[j][n] = 2
                                    exit = 1
                              if y == 200 and j == 1:
                                 if (x == 0 and n == 0) or (x == 100 and n == 1) or (x == 200 and n == 2):
                                    lista_main[j][n] = 2
                                    exit = 1
                              if y == 300 and j == 2:
                                 if (x == 0 and n == 0) or (x == 100 and n == 1) or (x == 200 and n == 2):
                                    lista_main[j][n] = 2
                                    exit = 1
               exit = 0




   #loading images
      for i in range(0, 3, 1):
         for j in range(0, 3, 1):
            if lista_main[i][j] == 2:
               screen.blit(image_2,(x,y))
            if lista_main[i][j] == 4:
               screen.blit(image_4,(x,y))
            if lista_main[i][j] == 8:
               screen.blit(image_8,(x,y))
            if lista_main[i][j] == 16:
               screen.blit(image_16,(x,y))
            if lista_main[i][j] == 32:
               screen.blit(image_32,(x,y))
            if lista_main[i][j] == 64:
               screen.blit(image_64,(x,y))
            if lista_main[i][j] == 128:
               screen.blit(image_128,(x,y))
            if lista_main[i][j] == 256:
               screen.blit(image_256,(x,y))
            if lista_main[i][j] == 512:
               screen.blit(image_512,(x,y))
            if lista_main[i][j] == 1024:
               screen.blit(image_1024,(x,y))
            if lista_main[i][j] == 2048:
               screen.blit(image_2048,(x,y))
      pygame.display.update()

#call function
main()