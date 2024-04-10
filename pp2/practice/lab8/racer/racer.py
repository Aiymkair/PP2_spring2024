import pygame, sys
from pygame.locals import *
import random
import math


pygame.init()
screen = pygame.display.set_mode((400, 600))

pygame.display.set_caption("Racer")
FPS = pygame.time.Clock()
zat1 = pygame.Rect((20,50), (50,100))
zat2 = pygame.Rect((10,10), (100,100))
print(zat1.colliderect(zat2))


class Zlo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("zlo.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
        def move(self):
            self.rect.move_ip(0,10)
            if (self.rect.bottom > 600):
                self.rect.top = 0
                self.rect.center = (random.randint(30, 370), 0)
 
        def draw(self, surface):
            surface.blit(self.image, self.rect) 
 

class Igrok(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =pygame.image.load("igrok.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160.520)

    def update(self):
        pressed_keys =pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    
    def draw(self,surface):
        surface.bilt(self.image, self.rect)

I1 = Igrok()
Z1 = Zlo()


done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    I1.update()
    Z1.move()
    screen.fill(WHITE)
    I1.draw(screen)
    Z1.draw(screen)
         
    pygame.display.update()
    frame_per_sec.tick(FPS)
    pygame.display.flip()