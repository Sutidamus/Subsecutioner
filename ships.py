import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, screen, xCood, yCood):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.xCood = xCood
        self.yCood = yCood
        self.color = (99, 93, 93)
        self.image = pygame.image.load("libertyShip.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.xCood, self.yCood)
        #print(self.rect.y)
    
    def __del__(self):
        print ("Ship Destroyed")

    def draw(self):
        self.screen.blit(self.image,(self.rect.x, self.rect.y))

