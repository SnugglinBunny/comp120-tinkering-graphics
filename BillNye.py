import pygame, sys
from pygame.locals import *
from pygame.image import save
pygame.init()

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

            GREY = (RED + GREEN + BLUE)/3

            pxarray[x, y] = (GREY, GREY, GREY)

pxarray = pygame.PixelArray(DISPLAY)

def blueColour():
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (255 - RED, 255 - GREEN, BLUE)

def redColour():
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (RED, 255 - GREEN, 255- BLUE)

def greenColour():
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (255 - RED, GREEN, 255- BLUE)

def invertColour():
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (255 - RED, 255 - GREEN, 255 - BLUE)

while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_r:
           blueColour()
           invertColour()
           pygame.display.flip()
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_t:
           blueColour()
           invertColour()
           pygame.display.flip()
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_y:
            greenColour()
            invertColour()
            pygame.display.flip()
pygame.display.update()
clock.tick(60)