import pygame
import math
import time


class Torpedo(pygame.sprite.Sprite):
    def __init__(self, screen, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.dx = dx
        self.dy = dy
        self.imagePos = 0
        self.imageList = ["torpedo1.png", "torpedo2.png", "torpedo3.png"]
        self.image = pygame.image.load(self.imageList[0])

        self.originalRect = self.image.get_rect()
        self.originalRect.center = (500, 700)
        self.rect = self.originalRect
        self.count = 0

    def draw(self):

                
        
        print("Image pos: " + str(self.imagePos))
        self.image = pygame.image.load(self.imageList[self.imagePos])
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.originalRect = self.image.get_rect()
        self.originalRect.center = (500, 700)
        
        
        try:
            self.image = pygame.transform.rotate(self.image, math.degrees(math.atan(self.dx/self.dy)))
        except ZeroDivisionError:
            pass

        

        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        
        

        print(self.rect.x, self.rect.y)
    def move(self):
        
        self.rect.x = 500
        self.rect.y = 700
        self.rect = self.originalRect.move(self.dx/200.0 * self.count, self.dy/200.0 * self.count)
        self.draw()
        self.count += 1
        self.imagePos +=1
        if self.imagePos == 3:
            self.imagePos = 0
        
       