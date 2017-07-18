import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, screen, xCood, yCood):
        self.screen = screen
        self.xCood = xCood
        self.yCood = yCood
        self.color = (99, 93, 93)
        self.rect = pygame.draw.rect(self.screen, self.color, (self.xCood, self.yCood, 100, 40))

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

