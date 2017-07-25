import pygame
import sys

"""
Code will pop up a black screen
"""

def main():
    pygame.init()
    story = Story()
    story.runStory()



"""
Game class
"""
class Story:
    def __init__(self):
        print("here")
        self.width = 1000 # Values can be changed as needed. Example values
        self.height = 700 # Values can be changed as needed. Example values
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = background("Story.jpg")
        self.sample = pygame.font.Font("1942.ttf", 40)
        self.back = pygame.rect.Rect(20, 20, 180, 60)
        self.backWords = self.sample.render("Back", 1, pygame.Color("black"))

    def runStory(self):
        pygame.key.set_repeat(500, 30) # Values can be changed as needed. Example values
        while 1:
            for event in pygame.event.get(): # Handles figuring out even 
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.checkBack():
                        return

            pygame.display.update()
            self.screen.blit(self.background.image, (0, 0))
            pygame.draw.rect(self.screen, pygame.Color("black"), self.back, 3)
            self.screen.blit(self.backWords, (55, 30))

    def checkBack(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 20 and p1x < 200 and p1y >20 and p1y < 80:
            return True
            print("hi")



class background:
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Story.jpg")
        self.rect = self.image.get_rect()

# main()