import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAY = pygame.display.set_mode((1600, 1066), 0, 32)

billnye = pygame.image.load('C:\Users\SC191991\downloads\BillNye.jpg')
imagerect = billnye.get_rect()

def drawNye():
    DISPLAY.blit(billnye, imagerect)
    pygame.display.flip()

while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()