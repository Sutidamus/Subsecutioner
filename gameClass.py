import pygame
import background
import sys
import ships
import scope
import torpedo
import random
import explosion
import time

def main():
    pygame.init()
    pygame.font.init()
    game = Game()
    game.runGame()


"""
Game Class
"""

class Game:
    def __init__(self):
        self.score = 0
        self.scoreText = pygame.font.Font("Minecraft.ttf", 30)
        self.width = 1000
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.screen.fill((200,200,200)) # Values can be changed as needed. Example values
        self.bg = background.Background(self.screen, 0, 375)
        self.ship1Y = random.randint(340, 375)
        self.ship2Y = random.randint(350, 385)
        self.ship3Y = random.randint(360, 395)
        self.ship1 = ships.Ship(self.screen, 0, self.ship1Y)
        self.ship2 = ships.Ship(self.screen, -200, self.ship2Y)
        self.ship3 = ships.Ship(self.screen, -400, self.ship3Y) 
        self.scope = scope.Scope(self.screen)
        self.linev = scope.Scope(self.screen)
        self.lineh = scope.Scope(self.screen)
        self.P1 = (500, 700)
        self.dx = 0
        self.dy = 0
        self.torpedo = None
        self.ship1Speed = 1
        self.ship2Speed = 1
        self.ship3Speed = 1
        self.explosionLocX = None
        self.explosionLocY = None
        self.explosion = None

    def moveShips(self):
        if self.ship1.rect.left < self.screen.get_width():
            self.ship1.rect.move_ip(self.ship1Speed,0)
        if self.ship2.rect.left < self.screen.get_width():
            self.ship2.rect.move_ip(self.ship2Speed,0)
        if self.ship3.rect.left < self.screen.get_width():
            self.ship3.rect.move_ip(self.ship2Speed, 0)

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
                if self.collision() or self.torpedo.rect.top < 330:
                    self.collisionShip1()
                    self.collisionShip2()
                    self.collisionShip3()
                    del(self.torpedo)
                    time.sleep(.2)
                    self.torpedo = None
                #if self.torpedo.rect.top < 420:
                    #print("="*15)
                    #del(self.torpedo)
                    #self.torpedo = None
            self.updateScore()


    def collision(self):
        if pygame.sprite.collide_rect(self.torpedo, self.ship1) or pygame.sprite.collide_rect(self.torpedo, self.ship2) or pygame.sprite.collide_rect(self.torpedo, self.ship3):
            self.increaseScore()
            return True

    def collisionShip1 (self):
        if pygame.sprite.collide_rect(self.torpedo, self.ship1):
            print("Explosion 1 found")
            self.explosionLocX = self.ship1.rect.x
            self.explosionLocY = self.ship1.rect.y
            self.explosion = explosion.Explosion(self.screen, self.explosionLocX, self.explosionLocY)
            del(self.ship1)
            self.ship1 = ships.Ship(self.screen, -200, 340)
            self.explosion.animate()   
                   
    def collisionShip2 (self):
        if pygame.sprite.collide_rect(self.torpedo, self.ship2):
            print("Explosion 2 found")
            self.explosionLocX = self.ship2.rect.x
            self.explosionLocY = self.ship2.rect.y
            self.explosion = explosion.Explosion(self.screen, self.explosionLocX, self.explosionLocY)
            del(self.ship2)
            self.ship2 = ships.Ship(self.screen, -400, 340)
            self.explosion.animate()
            
            
            
            
    def collisionShip3 (self):
        if pygame.sprite.collide_rect(self.torpedo, self.ship3):
            print("explosion 3 found")
            self.explosionLocX = self.ship3.rect.x
            self.explosionLocY = self.ship3.rect.y
            self.explosion = explosion.Explosion(self.screen, self.explosionLocX, self.explosionLocY)
            del(self.ship3)
            self.ship3 = ships.Ship(self.screen, -600, 340)
            self.explosion.animate()
           
            
    def increaseScore(self):
        self.score += 100
    def updateScore(self):
        self.scoreDis = self.scoreText.render("Current Score: " + str(self.score), 20, (255,255,255))
        self.screen.blit(self.scoreDis, (35, 35))
        
