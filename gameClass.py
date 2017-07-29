import pygame
import background
import sys
import ships
import scope
import torpedo
import random
import explosion
import time
import gameover

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
        pygame.init()
        self.score = 0
        self.scoreText = pygame.font.Font("Minecraft.ttf", 30)
        self.timeText = pygame.font.Font("Minecraft.ttf", 30)
        self.width = 1000
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.screen.fill((200,200,200)) # Values can be changed as needed. Example values
        self.bg = background.Background(self.screen, 0, 375)
        self.ship1Y = random.randint(340, 375)
        self.ship2Y = random.randint(375, 385)
        self.ship3Y = random.randint(385, 395)
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
        self.ship1Speed = random.randint(1,3)
        self.ship2Speed = random.randint(1,3)
        self.ship3Speed = random.randint(1,3)
        self.explosionLocX = None
        self.explosionLocY = None
        self.explosion = None
        self.LENGTHOFGAME = 90
        self.time = 90
        self.boVoiceCounter = 0
        self.explodeSound = pygame.mixer.Sound("explode.wav")
        self.torpedoSound = pygame.mixer.Sound("torpedoMove.wav")
        self.voiceSink = pygame.mixer.Sound("ShipDestroyed1.wav")
        #self.voiceShoot = pygame.mixer.Sound("")
        self.voicePowerPlus = pygame.mixer.Sound("HavePower.wav")
        self.voicePowerGone = pygame.mixer.Sound("NoPower.wav")
        #self.voiceTorp = pygame.mixer.Sound("Torpedo1.wav")
        self.cooldown = 300
        self.voiceCounter = 0
        self.voiceTorpedo = pygame.mixer.Sound("firingTorpedo.wav")
        self.channel1 = pygame.mixer.Channel(0)
        self.channel2 = pygame.mixer.Channel(1)
        self.channel3 = pygame.mixer.Channel(2)
        self.channel4 = pygame.mixer.Channel(3)
        self.channel5 = pygame.mixer.Channel(4)

    def moveShips(self):
        if self.ship1.rect.left < self.screen.get_width():
            self.ship1.rect.move_ip(self.ship1Speed,0)
        if self.ship2.rect.left < self.screen.get_width():
            self.ship2.rect.move_ip(self.ship2Speed,0)
        if self.ship3.rect.left < self.screen.get_width():
            self.ship3.rect.move_ip(self.ship3Speed, 0)

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

        startGameTime = time.time()
        self.last = pygame.time.get_ticks()
        rand_blackoutSt = random.randint(5, 8)
        rand_blackoutEnd = random.randint(9, 12)
        blackout2st = random.randint(25, 28)
        blackout2End = random.randint(29, 33)
        blackVocCounter = 0
        blackOut3 = random.randint(50, 52)
        blackout3st = 51
        blackout3End = random.randint(54, 56)
        #print(blackout3)
        while 1:
            for event in pygame.event.get(): # Handles figuring out even 
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            #seconds = pygame.time.get_ticks()//1000
            self.screen.fill((200,200,200)) # Values can be changed as needed. Example values
            self.time = 90
            self.bg.drawSea()
            self.bg.drawSky()
            self.ship1.draw()
            self.ship2.draw()
            self.ship3.draw()
            secondsPassed = time.time() - startGameTime
            #1st and 2nd Blackout
            if time.time() - startGameTime >= rand_blackoutSt and time.time() - startGameTime <= rand_blackoutEnd or time.time() - startGameTime >= blackout2st and time.time() - startGameTime <= blackout2End:
                if self.voiceCounter == 0:
                    self.channel3.play(self.voicePowerGone, 0)
                if int(time.time()) - int(startGameTime) == int(rand_blackoutEnd) and self.boVoiceCounter == 0:
                    self.channel5.play(self.voicePowerPlus, 0)
                    self.boVoiceCounter += 1
                    print("blackout over")
                startTime = int(time.time())
                endTime = startTime + 10
                while not startTime == endTime:
                    self.screen.fill((0,0,0))
                    startTime += 1
                    self.voiceCounter += 1
            #3rd blackout
            if time.time() - startGameTime >= blackOut3 and time.time() - startGameTime <= blackout3End and blackOut3 == 51:
                if self.voiceCounter == 0:
                    self.channel3.play(self.voicePowerGone, 0)
                if int(time.time()) - int(startGameTime) == int(rand_blackoutEnd) and self.boVoiceCounter == 0:
                    self.channel5.play(self.voicePowerPlus, 0)
                    self.boVoiceCounter += 1
                    print("blackout over")
                startTime = int(time.time())
                endTime = startTime + 10
                while not startTime == endTime:
                    self.screen.fill((0,0,0))
                    startTime += 1
                    self.voiceCounter += 1
            print(pygame.time.get_ticks())
            #if time.time()*1000%1000 ==0:
                #self.time -= 1
            self.scope.move()
            self.moveShips()
            self.screenWrap()
                   

            if time.time() - startGameTime >= self.LENGTHOFGAME and self.torpedo == None:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("menu_bgm.wav")
                pygame.mixer.music.play(-1, 0.0)
                go = gameover.GameOver(self.score)
                g = go.runGameOver()
                if g:
                    return
                else:
                    pygame.init()
                    # re-setup the class game to play the  game
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
                    self.ship1Speed = random.randint(1,3)
                    self.ship2Speed = random.randint(1,3)
                    self.ship3Speed = random.randint(1,3)
                    self.explosionLocX = None
                    self.explosionLocY = None
                    self.explosion = None
                    startGameTime = time.time()


            
            key = pygame.key.get_pressed()
            # Catching the ZeroDivisionError using an exception
            self.now = pygame.time.get_ticks()
            try:
                if key[pygame.K_SPACE]:
                    print(self.calculateSlope())
                    #self.torpedoSound.play()
                    if time.time() - startGameTime <= self.LENGTHOFGAME:
                        self.torpedo = torpedo.Torpedo(self.screen, self.dx, self.dy)
                        self.channel1.play(self.torpedoSound, 0)
                        self.channel4.play(self.voiceTorpedo, 0)
                        #self.channel2.play(self.voiceTorp, 0)
                        self.torpedoSound.set_volume(1.0)
            except ZeroDivisionError:
                if time.time() - startGameTime <= self.LENGTHOFGAME:
                    self.torpedo = torpedo.Torpedo(self.screen, self.dx, self.dy)
                    self.torpedo.move()
                    self.channel1.play(self.torpedoSound, 0)
                    #self.channel2.play(self.voiceTorp, 0)
                    self.torpedoSound.set_volume(1.0)
                    pass
            if not self.torpedo == None:
                oldVolume = self.torpedoSound.get_volume()
                self.torpedoSound.set_volume(oldVolume - .005)
                self.torpedo.move()
                if self.collision() or self.torpedo.rect.top < 440:
                    self.collisionShip1()
                    self.collisionShip2()
                    self.collisionShip3()
                    del(self.torpedo)
                    self.torpedoSound.stop()
                    time.sleep(.03)
                    self.torpedo = None
                #if self.torpedo.rect.top < 420:
                    #print("="*15)
                    #del(self.torpedo)
                    #self.torpedo = None
            self.updateScore()
            self.time = self.time - secondsPassed
            self.time = int(self.time)
            #if time.time() - startGameTime <= self.LENGTHOFGAME:
            if time.time() - startGameTime >= self.LENGTHOFGAME:
                self.screen.blit(self.textDis,(830, 35))
            else:
                self.updateTime()
            #if seconds % 30 == 0:


    def collision(self):
        if pygame.sprite.collide_rect(self.torpedo, self.ship1) or pygame.sprite.collide_rect(self.torpedo, self.ship2) or pygame.sprite.collide_rect(self.torpedo, self.ship3):
            self.channel3.play(self.voiceSink, 0)
            return True

    def collisionShip1 (self):
        if pygame.sprite.collide_rect(self.torpedo, self.ship1):
            print("Explosion 1 found")
            self.explosionLocX = self.ship1.rect.x
            self.explosionLocY = self.ship1.rect.y
            self.explodeSound.play()
            self.explosion = explosion.Explosion(self.screen, self.explosionLocX, self.explosionLocY)
            del(self.ship1)
            self.ship1 = ships.Ship(self.screen, -200, 340)
            for i in range(3):
                self.explosion.animate(i)
            self.score += self.ship1Speed * 100 
                
                   
    def collisionShip2 (self):
        if pygame.sprite.collide_rect(self.torpedo, self.ship2):
            print("Explosion 2 found")
            self.explosionLocX = self.ship2.rect.x
            self.explosionLocY = self.ship2.rect.y
            self.explodeSound.play()
            self.explosion = explosion.Explosion(self.screen, self.explosionLocX, self.explosionLocY)
            del(self.ship2)
            self.ship2 = ships.Ship(self.screen, -400, 340)
            for i in range(3):
                self.explosion.animate(i)
            self.score += self.ship2Speed * 100
                
            
            
            
    def collisionShip3 (self):
        if pygame.sprite.collide_rect(self.torpedo, self.ship3):
            print("explosion 3 found")
            self.explosionLocX = self.ship3.rect.x
            self.explosionLocY = self.ship3.rect.y
            self.explodeSound.play()
            self.explosion = explosion.Explosion(self.screen, self.explosionLocX, self.explosionLocY)
            del(self.ship3)
            self.ship3 = ships.Ship(self.screen, -600, 340)
            for i in range(3):
                self.explosion.animate(i)
            self.score += self.ship3Speed * 100
           
            
    #def increaseScore(self):
        #self.score += 100
    def updateScore(self):
        self.scoreDis = self.scoreText.render("Current Score: " + str(self.score), 20, (255,255,255))
        self.screen.blit(self.scoreDis, (35, 35))
    def changeTime(self):
        self.time -= 1
    def updateTime(self):
        self.textDis = self.timeText.render("Time: " + str(self.time),20, (255,255,255))
        self.screen.blit(self.textDis,(830, 35))