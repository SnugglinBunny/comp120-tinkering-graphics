import pygame, sys
from pygame.locals import *

<<<<<<< HEAD
pygame.init()

WIDTH = 1400
HEIGHT = 932
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Bill Nye')
=======
HEIGHT = 1400
WIDTH = 932
DISPLAY = pygame.display.set_mode((HEIGHT, WIDTH), 0, 32)
pygame.display.set_caption('Bill Nye')
clock = pygame.time.Clock()
colourImage = pygame.image.load('images\BillNyePlus.jpg')
delay = 200
red = False
green = True
blue = False
pxarray = pygame.PixelArray(DISPLAY)
del pxarray

DISPLAY.blit(colourImage, [0, 0])
pygame.time.delay(delay)
pygame.display.flip()
pygame.image.save(DISPLAY, 'images\BillyNyeplus.jpg')
# DISPLAY.blit(colourImage, [700, 0])
# pygame.time.delay(delay)
# pygame.display.flip()
# DISPLAY.blit(colourImage, [0, 466])
# pygame.time.delay(delay)
# pygame.display.flip()
# DISPLAY.blit(colourImage, [700, 466])
# pygame.time.delay(delay)
# pygame.display.flip()

def greyscale():
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
>>>>>>> origin/master

BLACK = (0, 0, 0)
WHITE= (255, 255, 255) # red, green, blue in 8-bits
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

<<<<<<< HEAD
colourImage = pygame.image.load('images\BillNyePlus.jpg')

DISPLAY.blit(colourImage, (0, 0))
pygame.display.flip()

pxarray = pygame.PixelArray(DISPLAY)
del pxarray

def Greyscale():
    DISPLAY.blit(colourImage, (0, 0))
    pygame.display.flip()
    pxarray = pygame.PixelArray(DISPLAY)
=======
            pxarray[x, y] = (GREY, GREY, GREY)

pxarray = pygame.PixelArray(DISPLAY)

def blueColour():
>>>>>>> origin/master
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
<<<<<<< HEAD

            GREY = (RED + GREEN + BLUE)/3

            pxarray[x, y] = (GREY, GREY, GREY)
    del pxarray

def redColour():
    DISPLAY.blit(colourImage, (0, 0))
    pygame.display.flip()
    pxarray = pygame.PixelArray(DISPLAY)
=======
            pxarray[x, y] = (255 - RED, 255 - GREEN, BLUE)

def redColour():
>>>>>>> origin/master
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (RED, 255 - GREEN, 255- BLUE)

def greenColour():
<<<<<<< HEAD
    DISPLAY.blit(colourImage, (0, 0))
    pygame.display.flip()
    pxarray = pygame.PixelArray(DISPLAY)
=======
>>>>>>> origin/master
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (255 - RED, GREEN, 255- BLUE)
<<<<<<< HEAD

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
=======
>>>>>>> origin/master

def invertColour():
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (255 - RED, 255 - GREEN, 255 - BLUE)
<<<<<<< HEAD
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
=======
>>>>>>> origin/master

while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   if event.type == pygame.KEYDOWN:
<<<<<<< HEAD
       if event.key == pygame.K_1:
           Greyscale()
=======
       if event.key == pygame.K_r:
           blueColour()
           invertColour()
>>>>>>> origin/master
           pygame.display.flip()
           pygame.image.save(DISPLAY, 'images\BillNyeGrey.jpg')
   if event.type == pygame.KEYDOWN:
<<<<<<< HEAD
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
=======
       if event.key == pygame.K_t:
>>>>>>> origin/master
           blueColour()
           invertColour()
           pygame.display.flip()
           pygame.image.save(DISPLAY, 'images\BillNyeBlue.jpg')
   if event.type == pygame.KEYDOWN:
<<<<<<< HEAD
       if event.key == pygame.K_5:
           BlackWhite()
           pygame.display.flip()
           pygame.image.save(DISPLAY, 'images\BillNyeBlackWhite.jpg')

pygame.display.update()
=======
       if event.key == pygame.K_y:
            greenColour()
            invertColour()
            pygame.display.flip()
pygame.display.update()
clock.tick(60)
>>>>>>> origin/master
