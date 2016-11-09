import pygame, sys
from pygame.locals import *

pygame.init()

WIDTH = 1400
HEIGHT = 932
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Bill Nye')

BLACK = (0, 0, 0)
WHITE= (255, 255, 255) # red, green, blue in 8-bits
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colourImage = pygame.image.load('images\BillNyePlus.jpg')

DISPLAY.blit(colourImage, (0, 0))
pygame.display.flip()

pxarray = pygame.PixelArray(DISPLAY)
del pxarray

def Greyscale():
    DISPLAY.blit(colourImage, (0, 0))
    pygame.display.flip()
    pxarray = pygame.PixelArray(DISPLAY)
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b

            GREY = (RED + GREEN + BLUE)/3

            pxarray[x, y] = (GREY, GREY, GREY)
    del pxarray

def redColour():
    DISPLAY.blit(colourImage, (0, 0))
    pygame.display.flip()
    pxarray = pygame.PixelArray(DISPLAY)
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (RED, 255 - GREEN, 255- BLUE)

def greenColour():
    DISPLAY.blit(colourImage, (0, 0))
    pygame.display.flip()
    pxarray = pygame.PixelArray(DISPLAY)
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (255 - RED, GREEN, 255- BLUE)

def blueColour():
    DISPLAY.blit(colourImage, (0, 0))
    pygame.display.flip()
    pxarray = pygame.PixelArray(DISPLAY)
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (255 - RED, 255 - GREEN, BLUE)

def invertColour():
    pxarray = pygame.PixelArray(DISPLAY)
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (255 - RED, 255 - GREEN, 255 - BLUE)
    del pxarray

def BlackWhite():
    DISPLAY.blit(colourImage, (0, 0))
    pygame.display.flip()
    pxarray = pygame.PixelArray(DISPLAY)
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b

            GREY = (RED + GREEN + BLUE)
            if GREY < 400:
                pxarray[x, y] = (0, 0, 0)
            else:
                pxarray[x, y] = (255, 255, 255)

    del pxarray

while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_1:
           Greyscale()
           pygame.display.flip()
           pygame.image.save(DISPLAY, 'images\BillNyeGrey.jpg')
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_2:
           redColour()
           invertColour()
           pygame.display.flip()
           pygame.image.save(DISPLAY, 'images\BillNyeRed.jpg')
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_3:
           greenColour()
           invertColour()
           pygame.display.flip()
           pygame.image.save(DISPLAY, 'images\BillNyeGreen.jpg')
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_4:
           blueColour()
           invertColour()
           pygame.display.flip()
           pygame.image.save(DISPLAY, 'images\BillNyeBlue.jpg')
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_5:
           BlackWhite()
           pygame.display.flip()
           pygame.image.save(DISPLAY, 'images\BillNyeBlackWhite.jpg')

pygame.display.update()