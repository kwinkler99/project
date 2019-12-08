import pygame, sys
import random
import os.path
from pygame.locals import *
#color
white = (255, 255, 255)
grey = (0x99, 0x99, 0x99)
black=(0x00, 0x00, 0x00)
red = (255,0,0)

#useful data
(width, height) = (300, 400)
lista1=[]
lista2=[]
lista3=[]
lista_main=[lista1,lista2,lista3]
lista_main1=[lista1,lista2,lista3]

#text
text='Gra 2048'



def DrawBoard(x, y, height, screen, color, line):
   pygame.draw.lines(screen, color, False, [(x,height), (y,height)], line)


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
for i in range (0, 3, 1):
   for j in range(0, 3, 1):
      if (y == 100 and i == 0) or (y == 200 and i == 1) or (y == 300 and i == 2):
            if y == 100 and i == 0:
               if (x == 0 and j == 0) or (x == 100 and j == 1) or (x == 200 and j == 2):
                  lista1.append(2)
                  lista2.append(0)
                  lista3.append(0)
               else:
                  lista1.append(0)
            if y == 200 and i == 1:
               if (x == 0 and j == 0) or (x == 100 and j == 1) or (x == 200 and j == 2):
                  lista2.append(2)
                  lista1.append(0)
                  lista3.append(0)
               else:
                  lista2.append(0)
            if y == 300 and i == 2:
               if (x == 0 and j == 0) or (x == 100 and j == 1) or (x == 200 and j == 2):
                  lista3.append(2)
                  lista1.append(0)
                  lista2.append(0)
               else:
                  lista3.append(0)
      else:
         if y != 100:
            lista1.append(0)
         if y != 200:
            lista2.append(0)
         if y != 300:
            lista3.append(0)
         break


lista_main=[lista1,lista2,lista3]





def input(events):
   for event in events:
      if event.type == QUIT:
         sys.exit(0)

# działaj aż do przerwania
while True:
   input(pygame.event.get())
   screen.blit(text_render, (width/3, (height-50)/9))
   for i in range(0, 3, 1):
      for j in range(0, 3, 1):
         if lista_main[i][j] == 2:
            screen.blit(image_2,(x,y))
   pygame.display.update()