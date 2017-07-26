import pygame
import sys
import gameClass
import helpScreen
import story

"""
Code will pop up a black screen
"""

def main():
    pygame.init()
    pygame.mixer.music.load("menu_bgm.wav")
    pygame.mixer.music.play(-1, 0.0)
    title = Title()
    title.runTitle()
    

"""
Title class
"""
class Title:
    def __init__(self):
        print("there")
        self.width = 1000 # Values can be changed as needed. Example values
        self.height = 700 # Values can be changed as needed. Example values
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = background("Wallpaper1.jpg")
        self.playButton = pygame.rect.Rect(436, 210, 200, 60)
        self.helpButton = pygame.rect.Rect(436, 300, 200, 60)
        self.storyButton = pygame.rect.Rect(436, 390, 200, 60)
        self.sample = pygame.font.Font("1942.ttf", 34)
        self.subsecutionerSample = pygame.font.Font("Typewriter.ttf", 60)
        self.playWords = self.sample.render("Subsecute", 1, pygame.Color("black"))
        self.helpWords = self.sample.render("Help", 1, pygame.Color("black"))
        self.storyWords = self.sample.render("Story", 1, pygame.Color("black"))
        self.subsecutioner = self.subsecutionerSample.render("THE SUBSECUTIONER", 1, pygame.Color("black"))

    def runTitle(self):
        pygame.key.set_repeat(500, 30) # Values can be changed as needed. Example values
        while 1:
            for event in pygame.event.get(): # Handles figuring out even 
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.checkForPlay()
                    self.checkForHelp()
                    self.checkForStory()

            pygame.display.update()
            
            self.screen.blit(self.background.image, (0, 0))
            self.screen.blit(self.playWords, (438, 222))
            self.screen.blit(self.helpWords, (485, 310))
            self.screen.blit(self.storyWords, (480, 400))
            self.screen.blit(self.subsecutioner, (200, 50))
            pygame.draw.rect(self.screen, pygame.Color("black"), self.playButton, 3)
            pygame.draw.rect(self.screen, pygame.Color("black"), self.helpButton, 3)
            pygame.draw.rect(self.screen, pygame.Color("black"), self.storyButton, 3)

    def checkForPlay(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 436 and p1x < 636 and p1y > 210 and p1y < 270:
            pygame.mixer.music.stop()
            #pygame.mixer.music.load("sea_music.wav")
            #pygame.mixer.music.play(1, 0.0)
            game = gameClass.Game()
            game.runGame()

    def checkForHelp(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 436 and p1x < 636 and p1y > 300 and p1y < 360:
            game = helpScreen.SubseHelp()
            game.runHelp()

    def checkForStory(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 436 and p1x < 636 and p1y > 390 and p1y < 450:
            game = story.Story()
            game.runStory()


class background:
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Wallpaper1.jpg")
        self.rect = self.image.get_rect()

main()