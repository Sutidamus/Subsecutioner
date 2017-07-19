import pygame
import math


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
            
        self.rect = self.image.get_rect()
        self.rect.center = (500, 700)

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y - 50))

