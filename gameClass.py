
import pygame
import background
import sys
import ships
import Scope

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
        self.bg = background.Background(self.screen, 0, self.height/2)
        self.ship1 = ships.Ship(self.screen, 100, 340)
        self.ship2 = ships.Ship(self.screen, 250, 340)
        self.ship3 = ships.Ship(self.screen, 400, 340)
        self.scope = Scope.Scope(self.screen)
        self.linev = Scope.Scope(self.screen)
        self.lineh = Scope.Scope(self.screen)

    def moveShips(self):
        if self.ship1.rect.left < self.screen.get_width():
            self.ship1.rect.move_ip(3,0)
        if self.ship2.rect.left < self.screen.get_width():
            self.ship2.rect.move_ip(3,0)
        if self.ship3.rect.left < self.screen.get_width():
            self.ship3.rect.move_ip(3, 0)

    def screenWrap(self):
        if self.ship1.rect.left == self.screen.get_width():
            self.ship1 = ships.Ship(self.screen, 100, 340)
            self.ship1.draw()
        if self.ship2.rect.left == self.screen.get_width():
            self.ship2 = ships.Ship(self.screen, 250, 340)
            self.ship2.draw()
        if self.ship3.rect.left == self.screen.get_width():
            self.ship3 = ships.Ship(self.screen, 400, 340)
            self.ship3.draw()       

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
            print(self.scope.getCoordinates())

main()