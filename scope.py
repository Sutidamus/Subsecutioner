import pygame

class Scope(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.color = pygame.Color(255, 0, 0)
        self.scopeWidth = 3
        self.startV = (500,420)
        self.endV = (500, 280)
        self.startH = (430, 350)
        self.endH = (570, 350)
        self.circleStartX = 500
        self.circleStartY = 350
        self.screenHeight = 700
        self.screenWidth = 1000
        self.rect = pygame.draw.circle(self.screen, self.color, (self.circleStartX, self.circleStartY), 70, self.scopeWidth)
        # self.rect = pygame.Rect(500, 300, 70, self.width)
        self.linev = pygame.draw.line(self.screen, self.color, self.startV, self.endV, self.scopeWidth)
        self.lineh = pygame.draw.line(self.screen, self.color, self.startH, self.endH, self.scopeWidth)
        
    
    def draw(self):
        pygame.draw.ellipse(self.screen, self.color, self.rect, self.scopeWidth)
        pygame.draw.line(self.screen, self.color, self.startV, self.endV, self.scopeWidth)
        pygame.draw.line(self.screen, self.color, self.startH, self.endH, self.scopeWidth)

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.top > self.screenHeight / 5:
           #print(self.startH[1])
            self.rect.move_ip(0,-10)
            self.startH = (self.startH[0], self.startH[1] - 10)
            self.endH = (self.endH[0], self.endH[1] - 10)
            self.startV = (self.startV[0], self.startV[1] - 10)
            self.endV = (self.endV[0], self.endV[1] - 10)

        if key[pygame.K_DOWN] and self.rect.top < self.screenHeight - 2/5 *self.screenHeight:
           #print(self.startH[1])
            self.rect.move_ip(0,10)
            self.startH = (self.startH[0], self.startH[1] + 10)
            self.endH = (self.endH[0], self.endH[1] + 10)
            self.startV = (self.startV[0], self.startV[1] + 10)
            self.endV = (self.endV[0], self.endV[1] + 10)

        if key[pygame.K_LEFT] and self.rect.left > 0:
           #print(self.startH[1])
            self.rect.move_ip(-10,0)
            self.startH = (self.startH[0] - 10, self.startH[1])
            self.endH = (self.endH[0] - 10, self.endH[1])
            self.startV = (self.startV[0] - 10, self.startV[1])
            self.endV = (self.endV[0] - 10, self.endV[1])

        if key[pygame.K_RIGHT] and self.rect.right < self.screenWidth:
           #print(self.startH[1])
            self.rect.move_ip(10,0)
            self.startH = (self.startH[0] + 10, self.startH[1])
            self.endH = (self.endH[0] + 10, self.endH[1])
            self.startV = (self.startV[0] + 10, self.startV[1])
            self.endV = (self.endV[0] + 10, self.endV[1])
        
        #self.linev.move_ip(1,1)
        #self.lineh.move_ip(1,1)
        self.draw()
        

    