import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, screen, xCood, yCood):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        #self.width = self.screen.get_width()
        #self.height = self.screen.get_height()
        self.xCood = xCood
        self.yCood = yCood
        self.color = (50,50,230)
        self.skyColor = (30, 170, 220)
        self.image = pygame.image.load("atlanticOcean.png")
        self.skyImage = pygame.image.load("sky.png")
        self.oceanRect = self.image.get_rect()
        #self.image = pygame.transform.scale(self.image, (100,100))
        #self.ocean = pygame.draw.rect(self.screen, self.color, (self.xCood, self.yCood, self.screen.get_width(), 400) )
        self.sky = pygame.draw.rect(self.screen, self.color,(0, 0, self.screen.get_width(), 375))
    
    def drawSea(self):
        self.image = pygame.transform.scale(self.image, (1000,600))
        self.screen.blit(self.image, (0, 100))
    def drawSky(self):
        pygame.draw.rect(self.screen, self.skyColor, self.sky)
        #self.skyImage = pygame.transform.scale(self.skyImage, (1000,400))
        #self.screen.blit(self.skyImage,(0,0))


    
