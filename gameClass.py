
import pygame
import background
import sys
import ships
import scope
import torpedo

def main():
    pygame.init()
    game = Game()
    game.runGame()


"""
Game Class
"""

class Game:
    def __init__(self):
        self.width = 1000
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.screen.fill((200,200,200)) # Values can be changed as needed. Example values
        self.bg = background.Background(self.screen, 0, 375)
        self.ship1 = ships.Ship(self.screen, 0, 340)
        self.ship2 = ships.Ship(self.screen, -200, 340)
        self.ship3 = ships.Ship(self.screen, -400, 340) 
        self.scope = scope.Scope(self.screen)
        self.linev = scope.Scope(self.screen)
        self.lineh = scope.Scope(self.screen)
        self.P1 = (500, 700)
        self.dx = 0
        self.dy = 0
        self.torpedo = None
        

    def moveShips(self):
        if self.ship1.rect.left < self.screen.get_width():
            self.ship1.rect.move_ip(1,0)
        if self.ship2.rect.left < self.screen.get_width():
            self.ship2.rect.move_ip(1,0)
        if self.ship3.rect.left < self.screen.get_width():
            self.ship3.rect.move_ip(1, 0)

    def screenWrap(self):
        if self.ship1.rect.left == self.screen.get_width():
            self.ship1 = ships.Ship(self.screen, 0, 340)
            self.ship1.draw()
        if self.ship2.rect.left == self.screen.get_width():
            self.ship2 = ships.Ship(self.screen, -200, 340)
            self.ship2.draw()
        if self.ship3.rect.left == self.screen.get_width():
            self.ship3 = ships.Ship(self.screen, -400, 340)
            self.ship3.draw()       


    
    def getCoordinates(self):
            xCood = (self.scope.startV[0] + self.scope.endV[0]) / 2 
            yCood = (self.scope.startV[1] + self.scope.endV[1]) / 2
            return xCood, yCood

    def calculateSlope(self):
        self.dx = self.getCoordinates()[0] - 500
        self.dy = self.getCoordinates()[1] - 700
        return self.dx, self.dy


    def runGame(self):
        pygame.key.set_repeat(500, 30) # Values can be changed as needed. Example values

        while 1:
            for event in pygame.event.get(): # Handles figuring out even 
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            self.screen.fill((200,200,200)) # Values can be changed as needed. Example values
            self.bg.drawSea()
            self.bg.drawSky()
            self.ship1.draw()
            self.ship2.draw()
            self.ship3.draw()
            self.scope.move()
            self.moveShips()
            self.screenWrap()
            
            key = pygame.key.get_pressed()
            # Catching the ZeroDivisionError using an exception
            
            try:
                if key[pygame.K_SPACE]:
                    print(self.calculateSlope())
                    self.torpedo = torpedo.Torpedo(self.screen, self.dx, self.dy)
            except ZeroDivisionError:
                self.torpedo = torpedo.Torpedo(self.screen, self.dx, self.dy)
                self.torpedo.move()
                pass
            if not self.torpedo == None:
                self.torpedo.move()
                if (self.collision()):
                    print(self.collisionShip1())
                    print(self.collisionShip2())
                    print(self.collisionShip3())
                if self.torpedo.rect.top < 372:
                    print("="*15)
                    del(self.torpedo)
                    self.torpedo = None


    def collision(self):
        if pygame.sprite.collide_rect(self.torpedo, self.ship1) or pygame.sprite.collide_rect(self.torpedo, self.ship2) or pygame.sprite.collide_rect(self.torpedo, self.ship3):
            return True

    def collisionShip1 (self):
        if pygame.sprite.collide_rect(self.torpedo, self.ship1):
            del(self.ship1)
            self.ship1 = ships.Ship(self.screen, -200, 340)
            
        
    def collisionShip2 (self):
        if pygame.sprite.collide_rect(self.torpedo, self.ship2):
            del (self.ship2)
            self.ship2 = ships.Ship(self.screen, -400, 340)
            
    def collisionShip3 (self):
        if pygame.sprite.collide_rect(self.torpedo, self.ship3):
            del (self.ship3)
            self.ship3 = ships.Ship(self.screen, -600, 340)
            
            
        
main()