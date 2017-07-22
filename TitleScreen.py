import gameClass
import pygame

def main():
    pygame.init()
    pygame.font.init()
    titleScreem = TitleScreen()
    titleScreen.runTitleScreen()


"""
Game Class
"""

class titleScreen:
    def __init__(self):
        #self.score = 0
        #self.scoreText = pygame.font.Font("Minecraft.ttf", 30)
        self.width = 1000
        self.height = 700
        #self.screen = pygame.display.set_mode((self.width, self.height))
        #self.background = pygame.Surface(self.screen.get_size())
        #self.background = self.background.convert()
        #self.screen.fill((200,200,200)) # Values can be changed as needed. Example values
        #self.bg = background.Background(self.screen, 0, 375)

        while 1:
            for event in pygame.event.get(): # Handles figuring out even 
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            self.screen.fill((200,200,200)) # Values can be changed as needed. Example values
            #self.bg.drawSea()
            #self.bg.drawSky()
    main()