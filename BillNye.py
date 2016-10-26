import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAY = pygame.display.set_mode((1600, 1066), 0, 32)
pygame.display.set_caption('Bill Nye')

BLACK = (0, 0, 0)
WHITE= (255, 255, 255) # red, green, blue in 8-bits
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

billnye = pygame.image.load('images\BillNye.jpg')
imagerect = billnye.get_rect()

def drawNye():
    DISPLAY.blit(billnye, imagerect)
    pygame.display.flip()

drawNye()

glasses = pygame.image.load('images\glasses.png')

def drawGlasses():
    DISPLAY.blit(glasses, (670, 120))
    pygame.display.flip()

def gunOne():
    pxarray = pygame.PixelArray(DISPLAY)
    pxarray [40:200, 200:250] = (254,70,5)



while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_g:
           drawGlasses()
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_h:
           gunOne()

pygame.display.update()