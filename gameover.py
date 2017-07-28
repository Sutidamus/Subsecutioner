import pygame
import sys

"""
Code will pop up a black screen
"""

def main():
    pygame.init()
    pygame.mixer.music.load("menu_bgm.wav")
    pygame.mixer.music.play(1, 0.0)
    gameOver = GameOver()
    gameOver.runGameOver()



"""
Game class
"""
class GameOver:
    def __init__(self, score):
        print("here")
        self.width = 1000 # Values can be changed as needed. Example values
        self.height = 700 # Values can be changed as needed. Example values
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = background("Wallpaper1.jpg")
        self.sample = pygame.font.Font("1942.ttf", 40)
        self.gameOverSample = pygame.font.Font("Typewriter.ttf", 80)
        self.score = str(score)
        self.scoreText = pygame.font.Font("Minecraft.ttf", 65)
        self.playAgain = pygame.rect.Rect(360, 240, 260, 60)
        self.quit = pygame.rect.Rect(433, 330, 105, 60)
        self.gameOverWords = self.gameOverSample.render("Game Over", 1, pygame.Color("black"))
        self.playAgainWords = self.sample.render("Play again", 1, pygame.Color("black"))
        self.quitWords = self.sample.render("Quit", 1, pygame.Color("black"))


    def runGameOver(self):
        pygame.key.set_repeat(500, 30) # Values can be changed as needed. Example values
        while 1:
            for event in pygame.event.get(): # Handles figuring out even 
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = self.checkQuit()
                    if x == True:
                        return True
                    if self.checkPlayAgain() == True:
                        pygame.mixer.music.load("uboat_bgm.wav")
                        pygame.mixer.music.play(1, 0.0)
                        return False


            pygame.display.update()
            self.screen.blit(self.background.image, (0, 0))
            pygame.draw.rect(self.screen, pygame.Color("black"), self.playAgain, 3)
            pygame.draw.rect(self.screen, pygame.Color("black"), self.quit, 3)
            self.screen.blit(self.playAgainWords, (360, 245))
            self.scoreDis = self.scoreText.render("Final Score: " +self.score ,1, pygame.Color("white"))
            self.screen.blit(self.scoreDis, (235, 500))
            self.screen.blit(self.gameOverWords, (250, 100))
            self.screen.blit(self.quitWords, (435, 335))

    def checkPlayAgain(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 360 and p1x < 620 and p1y > 240 and p1y < 300:
            return True
        return False
            

    def checkQuit(self):
        p1x, p1y = pygame.mouse.get_pos()
        if p1x > 433 and p1x < 538 and p1y > 330 and p1y < 390:
            return True
        return False



class background:
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Wallpaper1.jpg")
        self.rect = self.image.get_rect()

# main()