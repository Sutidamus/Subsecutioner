import pygame
import sys
import math
import time
import gameClass

"""
Code will pop up a black screen
"""

def main():
    pygame.init()
    title = Title()
    title.runTitle()
    

"""
Title class
"""
class Title:
    def __init__(self):
        self.width = 1000 # Values can be changed as needed. Example values
        self.height = 700 # Values can be changed as needed. Example values
        self.screen = pygame.display.set_mode((self.width, self.height))
        # Need to set background so shapes are drawn with full color
        #self.background = pygame.Surface(self.screen.get_size())
        #self.background = self.background.convert()
        self.screen.fill((220,220,220)) # Values can be changed as needed. Example values
        self.background = background("Wallpaper1.jpg")
        self.playButton = pygame.rect.Rect(425, 300, 200, 60)
        #self.subsecute = subsecute(self.screen, 425, 300)
        #pos = []
        self.sample = pygame.font.SysFont("timesnewroman", 40)
        self.words = self.sample.render("Subsecute", 1, pygame.Color("black"))

    def runTitle(self):
        pygame.key.set_repeat(500, 30) # Values can be changed as needed. Example values
        while 1:
            for event in pygame.event.get(): # Handles figuring out even 
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.checkForPlay()

            #self.subsecute.clicked()
            pygame.display.update()
            
            #self.screen.fill((220, 220, 220))
            self.screen.blit(self.background.image, (0, 0))
            self.screen.blit(self.words, (435, 310))
            pygame.draw.rect(self.screen, pygame.Color("black"), self.playButton, 4)

    def checkForPlay(self):
        p1x, p1y = pygame.mouse.get_pos()
        print(p1x)
        if p1x > 425 and p1x < 625 and p1y > 300 and p1y < 360:
            game = gameClass.Game()
            game.runGame()

class background:
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Wallpaper1.jpg")
        self.rect = self.image.get_rect()

main()