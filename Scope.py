import pygame

class Scope(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.color = pygame.Color(255, 0, 0)
        self.width = 3
        self.startV = (500,420)
        self.endV = (500, 280)
        self.startH = (430, 350)
        self.endH = (570, 350)
        self.rect = pygame.draw.circle(self.screen, self.color, (500, 350), 70, self.width)
        # self.rect = pygame.Rect(500, 300, 70, self.width)
        self.linev = pygame.draw.line(self.screen, self.color, self.startV, self.endV, self.width)
        self.lineh = pygame.draw.line(self.screen, self.color, self.startH, self.endH, self.width)
        
    
    def draw(self):
        pygame.draw.ellipse(self.screen, self.color, self.rect, self.width)
        pygame.draw.line(self.screen, self.color, self.startV, self.endV, self.width)
        pygame.draw.line(self.screen, self.color, self.startH, self.endH, self.width)

    def move(self):
        #key = pygame.key.get_pressed()
        self.startH = (self.startH[0]+1, self.startH[1] + 1)
        self.startV = (self.startV[0] + 1, self.startV[1]+1)
        self.endH = (self.endH[0] + 1, self.endH[1] + 1)
        self.endV = (self.endV[0] +1 , self.endV[1] +1)
        self.rect.move_ip(1, 1)
        #self.linev.move_ip(1,1)
        #self.lineh.move_ip(1,1)
        self.draw()
        

    