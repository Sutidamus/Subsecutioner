import pygame

class Torpedo(pygame.sprite.Sprite):
    def __init__(self, screen, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.dx = dx
        self.dy = dy
        self.image = pygame.image.load("download.jpeg")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (500, 700)

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
