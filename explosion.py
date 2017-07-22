import pygame

class Explosion:
    def __init__(self, screen, xCood, yCood):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.imagePos = 0
        self.xCood = xCood
        self.yCood = yCood
        self.imageList = ["explosion1.png", "explosion2.png", "explosion3.png"]
        self.image = pygame.image.load(self.imageList[0])
        self.rect = self.image.get_rect()

    def __del__(self):
        print("explosion gone")

    def draw(self):
        pass
        
        
    def animate(self):
        if self.imagePos == 3:
            self.imagePos = 0
        #if pygame.time.get_ticks() % 12 == 0:
            #self.imagePos +=1
        self.image = pygame.image.load(self.imageList[self.imagePos])
        self.screen.blit(self.image, (self.xCood ,self.yCood))
        print("i drew that...")
        #print(str(self.imagePos) + "==============")
        self.imagePos+= 1