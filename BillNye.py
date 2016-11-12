import pygame, sys
from pygame.locals import *

pygame.init()

#Displays screen
WIDTH = 1400
HEIGHT = 932
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Bill Nye')
clock = pygame.time.Clock()

#Sets up colours
BLACK = (0, 0, 0)
WHITE= (255, 255, 255) # red, green, blue in 8-bits
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
Delay = 200
colourImage = pygame.image.load('images\BillNyePlus.jpg')
colourImage = pygame.transform.scale(colourImage, (WIDTH, HEIGHT))

DISPLAY.blit(colourImage, (0, 0))
pygame.display.flip()

pxarray = pygame.PixelArray(DISPLAY)
del pxarray

#Makes picture greyscale by removing red, green and blue
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

#Makes picture red by removing blue and green
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

#Makes picture green by removing blue and red
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

#Makes picture blue by removing red and green
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

#Inverts colour by removing 255 from all RGB values
def invertColour():
    pxarray = pygame.PixelArray(DISPLAY)
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (255 - RED, 255 - GREEN, 255 - BLUE)
    del pxarray

#Makes image black and white by calculating the values of the pixels
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

#Puts 4 images on the screen of the effects we created
def PieceDeResistance():
    RedImage = pygame.image.load('images\BillNyeRed.jpg')
    RedImage = pygame.transform.scale(RedImage, (700, 466))
    GreenImage = pygame.image.load('images\BillNyeGreen.jpg')
    GreenImage = pygame.transform.scale(GreenImage, (700, 466))
    BlueImage = pygame.image.load('images\BillNyeBlue.jpg')
    BlueImage = pygame.transform.scale(BlueImage, (700, 466))
    BWImage = pygame.image.load('images\BillNyeBlackWhite.jpg')
    BWImage = pygame.transform.scale(BWImage, (700, 466))
    DISPLAY.blit(BWImage, (0, 0))
    pygame.display.flip()
    pygame.time.delay(Delay)
    DISPLAY.blit(RedImage, (700, 0))
    pygame.display.flip()
    pygame.time.delay(Delay)
    DISPLAY.blit(GreenImage, (0, 466))
    pygame.display.flip()
    pygame.time.delay(Delay)
    DISPLAY.blit(BlueImage, (700, 466))
    pygame.display.flip()
    pygame.time.delay(Delay)
    pygame.image.save(DISPLAY, 'images\PieceDeResistance.jpg')

#Sets up key presses to make images do effects
while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
           Greyscale()
           pygame.display.flip()
           pygame.image.save(DISPLAY, 'images\BillNyeGrey.jpg')
   if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
           redColour()
           invertColour()
           pygame.display.flip()
           pygame.image.save(DISPLAY, 'images\BillNyeRed.jpg')
   if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
           greenColour()
           invertColour()
           pygame.display.flip()
           pygame.image.save(DISPLAY, 'images\BillNyeGreen.jpg')
   if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
           blueColour()
           invertColour()
           pygame.display.flip()
           pygame.image.save(DISPLAY, 'images\BillNyeBlue.jpg')
   if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
           BlackWhite()
           pygame.display.flip()
           pygame.image.save(DISPLAY, 'images\BillNyeBlackWhite.jpg')
   if event.type == pygame.KEYDOWN and event.key == pygame.K_9:
       try:
        PieceDeResistance()
       except:
           print 'Images have not been generated yet, please use keys 1-5 before trying this again.'

pygame.display.update()
clock.tick(60)
