import pygame
import math
import time


class Torpedo(pygame.sprite.Sprite):
    def __init__(self, screen, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.dx = dx
        self.dy = dy
        self.image = pygame.image.load("arrow.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        try:
            self.image = pygame.transform.rotate(self.image, math.degrees(math.atan(self.dx/self.dy)))
        except ZeroDivisionError:
            pass
            
        self.originalRect = self.image.get_rect()
        self.originalRect.center = (500, 700)
        self.count = 0

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        
        #delay = 0.6
        #oldTime = time.time()
        #if oldTime + delay > time.time():
        #time.sleep(0.6)
        self.rect = self.originalRect.move(self.dx/200.0 * self.count, self.dy/200.0 * self.count)
        self.draw()
        self.count += 1
       
        

