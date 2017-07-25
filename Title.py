import pygame
import sys
import gameClass
import helpScreen

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
        self.background = background("Wallpaper1.jpg")
        self.playButton = pygame.rect.Rect(425, 270, 200, 60)
        self.helpButton = pygame.rect.Rect(425, 360, 200, 60)
        self.sample = pygame.font.Font("True Lies.ttf", 40)
        self.playWords = self.sample.render("Subsecute", 1, pygame.Color("black"))
        self.helpWords = self.sample.render("Subsehelp", 1, pygame.Color("black"))

    def runTitle(self):
        pygame.key.set_repeat(500, 30) # Values can be changed as needed. Example values
        while 1:
            for event in pygame.event.get(): # Handles figuring out even 
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.checkForPlay()
                    self.checkForHelp()

            pygame.display.update()
            
            self.screen.blit(self.background.image, (0, 0))
            self.screen.blit(self.playWords, (427, 280))
            self.screen.blit(self.helpWords, (425, 370))
            pygame.draw.rect(self.screen, pygame.Color("black"), self.playButton, 4)
            pygame.draw.rect(self.screen, pygame.Color("black"), self.helpButton, 4)
    def checkForPlay(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 425 and p1x < 625 and p1y > 270 and p1y < 330:
            game = gameClass.Game()
            game.runGame()

    def checkForHelp(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 425 and p1x < 625 and p1y > 360 and p1y < 420:
            game = helpScreen.SubseHelp()
            game.runHelp()


class background:
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Wallpaper1.jpg")
        self.rect = self.image.get_rect()

main()