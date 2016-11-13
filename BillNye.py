import pygame, sys                                                  #imports all useful modules
from pygame.locals import *

pygame.init()                                                       #Initiates Pygame

WIDTH = 1400
HEIGHT = 932
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)           #Sets Height and Width and creates window.
pygame.display.set_caption('Bill Nye')                              #Sets caption in the windows top bar.
clock = pygame.time.Clock()                                         #Sets up clock for fps cap later on.

BLACK = (0, 0, 0)                                                   #Creates global variables for later use.
WHITE= (255, 255, 255) # red, green, blue in 8-bits
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
Delay = 200                                                         #This is equivelent to 200 milliseconds.
colourImage = pygame.image.load('images\BillNyePlus.jpg')           #Load in the image from disk.
colourImage = pygame.transform.scale(colourImage, (WIDTH, HEIGHT))  #Scales image to fit the window.

DISPLAY.blit(colourImage, (0, 0))                                   #Generates image on screen.
pygame.display.flip()                                               #Updates entire surface.


def Greyscale():                                                    #Creates Greyscale Function.
    DISPLAY.blit(colourImage, (0, 0))                               #Displays the normal image.
    pygame.display.flip()                                           #Updates Surface.
    pxarray = pygame.PixelArray(DISPLAY)                            #Creates pixel array for the window.
    for y in xrange(HEIGHT):                                        #Goes through every pixel on the y axis.
        for x in xrange(WIDTH):                                     #Loops through each pixel in the array.
            RED = DISPLAY.get_at((x, y)).r                          #Each pixel is split into three colour values RGB.
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b

            GREY = (RED + GREEN + BLUE)/3                           #Colour values are added making a shade of grey.

            pxarray[x, y] = (GREY, GREY, GREY)                      #Pixel is then assigned the new grey colour.
    del pxarray                                                     #Deletes the pixel array unlocking the screen.


def redColour():
    DISPLAY.blit(colourImage, (0, 0))
    pygame.display.flip()
    pxarray = pygame.PixelArray(DISPLAY)
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b                         #Reduces the Green and Blue values
            pxarray[x, y] = (RED, 255 - GREEN, 255- BLUE)           #Making Red the dominant Colour.

def greenColour():
    DISPLAY.blit(colourImage, (0, 0))
    pygame.display.flip()
    pxarray = pygame.PixelArray(DISPLAY)
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b                         #Reduces the Red and Blue values
            pxarray[x, y] = (255 - RED, GREEN, 255- BLUE)           #Making Green the dominant Colour.

def blueColour():
    DISPLAY.blit(colourImage, (0, 0))
    pygame.display.flip()
    pxarray = pygame.PixelArray(DISPLAY)
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b                         #Reduces the Red and Green values
            pxarray[x, y] = (255 - RED, 255 - GREEN, BLUE)          #Making Blue the dominant Colour.

def invertColour():
    pxarray = pygame.PixelArray(DISPLAY)
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b                         #Inverts colours by removing the current value
            pxarray[x, y] = (255 - RED, 255 - GREEN, 255 - BLUE)    #From the maximum possible value 255.
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

            GREY = (RED + GREEN + BLUE)                             #Add all three colour values.
            if GREY < 400:                                          #If the three colours are over 400 pixel = Black
                pxarray[x, y] = (0, 0, 0)
            else:
                pxarray[x, y] = (255, 255, 255)                     #If not pixel = white.

    del pxarray

def PieceDeResistance():
    RedImage = pygame.image.load('images\BillNyeRed.jpg')           #Loads each generated image.
    RedImage = pygame.transform.scale(RedImage, (700, 466))         #Scales them down.
    GreenImage = pygame.image.load('images\BillNyeGreen.jpg')
    GreenImage = pygame.transform.scale(GreenImage, (700, 466))
    BlueImage = pygame.image.load('images\BillNyeBlue.jpg')
    BlueImage = pygame.transform.scale(BlueImage, (700, 466))
    BWImage = pygame.image.load('images\BillNyeBlackWhite.jpg')
    BWImage = pygame.transform.scale(BWImage, (700, 466))
    DISPLAY.blit(BWImage, (0, 0))                                   #Display each on the screen.
    pygame.display.flip()                                           #Flip updates screen.
    pygame.time.delay(Delay)                                        #Wait delay time before next image.
    DISPLAY.blit(RedImage, (700, 0))
    pygame.display.flip()
    pygame.time.delay(Delay)
    DISPLAY.blit(GreenImage, (0, 466))
    pygame.display.flip()
    pygame.time.delay(Delay)
    DISPLAY.blit(BlueImage, (700, 466))
    pygame.display.flip()
    pygame.time.delay(Delay)
    pygame.image.save(DISPLAY, 'images\PieceDeResistance.jpg')      #Save final image to disk.

while True:
   for event in pygame.event.get():
       if event.type == QUIT:                                       #Stops game exiting unless escape is pressed.
           pygame.quit()
           sys.exit()
   if event.type == pygame.KEYDOWN and event.key == pygame.K_1:     #If key 1 is pressed do:
           Greyscale()                                              #Displays image from effect and saves it to disk.
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
   if event.type == pygame.KEYDOWN and event.key == pygame.K_9:     #Prints final image.
       try:
        PieceDeResistance()                                         #If it fails for any reason
       except:                                                      #Print error message.
           print 'Images have not been generated yet, please use keys 1-5 before trying this again.'

pygame.display.update()
clock.tick(60)                                                      #Regulates fps to 60.
