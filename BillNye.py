import pygame, sys, PIL
from pygame.locals import *
from pygame.image import save
from PIL import Image
pygame.init()

DISPLAY = pygame.display.set_mode((1400, 932), 0, 32)
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

def blite():
    image = Image.open('images\BillNye.jpg')
    gray = image.convert('L')
    bw = gray.point(lambda x: 0 if x < 128 else 255, '1')
    bw.save('images\BillNyeBW.png')
    bwimage = pygame.image.load('images\BillNyeBW.png')
    DISPLAY.blit(bwimage, [0, 0])
    pygame.time.delay(delay)
    pygame.display.flip()
    DISPLAY.blit(bwimage, [700, 0])
    pygame.time.delay(delay)
    pygame.display.flip()
    DISPLAY.blit(bwimage, [0, 466])
    pygame.time.delay(delay)
    pygame.display.flip()
    DISPLAY.blit(bwimage, [700, 466])
    pygame.time.delay(delay)
    pygame.display.flip()

def greyscale():
    for x in range(colourImage.get_width()):
        for y in range(colourImage.get_height()):
            c = list(colourImage.get_at((x,y))[:3])
            deg = (c[0]*red +c[1]*green + c[2]*blue) / (red + green + blue)

            colourImage.fill( [deg]*3, ((x,y), (1,1)))




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
           blite()
   if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_t:
            greyscale()

pygame.display.update()
clock.tick(60)