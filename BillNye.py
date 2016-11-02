import pygame, sys
from pygame.locals import *
from pygame.image import save
pygame.init()

HEIGHT = 1400
WIDTH = 932
DISPLAY = pygame.display.set_mode((HEIGHT, WIDTH), 0, 32)
pygame.display.set_caption('images\Bill Nye')
clock = pygame.time.Clock()
colourImage = pygame.image.load('images\BillNye.jpg')
delay = 200
red = False
green = True
blue = False

def drawimage():
    DISPLAY.blit(colourImage, [0, 0])
    pygame.time.delay(delay)
    pygame.display.flip()
    DISPLAY.blit(colourImage, [700, 0])
    pygame.time.delay(delay)
    pygame.display.flip()
    DISPLAY.blit(colourImage, [0, 466])
    pygame.time.delay(delay)
    pygame.display.flip()
    DISPLAY.blit(colourImage, [700, 466])
    pygame.time.delay(delay)
    pygame.display.flip()

# def blite():
#     image = Image.open('images\BillNye.jpg')
#     gray = image.convert('L')
#     bw = gray.point(lambda x: 0 if x < 128 else 255, '1')
#     bw.save('images\BillNyeBW.png')
#     bwimage = pygame.image.load('images\BillNyeBW.png')
#     DISPLAY.blit(bwimage, [0, 0])
#     pygame.time.delay(delay)
#     pygame.display.flip()
#     DISPLAY.blit(bwimage, [700, 0])
#     pygame.time.delay(delay)
#     pygame.display.flip()
#     DISPLAY.blit(bwimage, [0, 466])
#     pygame.time.delay(delay)
#     pygame.display.flip()
#     DISPLAY.blit(bwimage, [700, 466])
#     pygame.time.delay(delay)
#     pygame.display.flip()

def greyscale():
    for x in range(colourImage.get_width()):
        for y in range(colourImage.get_height()):
            c = list(colourImage.get_at((x,y))[:3])
            deg = (c[0]*red +c[1]*green + c[2]*blue) / (red + green + blue)

            colourImage.fill( [deg]*3, ((x,y), (1,1)))


def blueColour():
    pxarray = pygame.PixelArray(DISPLAY)
    for y in xrange(HEIGHT):
        for x in xrange(WIDTH):
            RED = DISPLAY.get_at((x, y)).r
            GREEN = DISPLAY.get_at((x, y)).g
            BLUE = DISPLAY.get_at((x, y)).b
            pxarray[x, y] = (255 - RED, 255 - GREEN, BLUE)
            pygame.display.flip()
            del pxarray

while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_d:
           drawimage()
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_g:
           blueColour()
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_t:
            greyscale()

pygame.display.update()
clock.tick(60)