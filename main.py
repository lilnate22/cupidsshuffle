#Nate Fonseka
#Cupid Shuffle
#Released under Creative Commons 2.0

import pygame
import player
import food
import girl
import enemy
import os,sys
import time

class Game_Window(object):
        def __init__(self):
                pygame.init()
                pygame.mixer.init()
                self.screen = pygame.display.set_mode((700,700),0,32)
                self.clock = pygame.time.Clock()
                self.player = player.Player(700,700)
                self.Food = food.Food()
                self.Girl = girl.girl()
                self.Enemy = enemy.enemy()                
                self.font = pygame.font.SysFont('freesansbold.ttf',40)
                pygame.display.set_caption('Cupid Shuffle')
                self.go = pygame.mixer.Sound(os.path.join(os.getcwd(),'gameover.aiff'))

        def game_over(self):
                # play the game over sound
                
                
                self.go.play()
                
                running = True
                gtime = 0
                while running :
                        gtime += self.clock.tick()
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()
                                if event.type == pygame.KEYDOWN and gtime > 1500:
                                        running = False
                        self.screen.fill((50,140,210))
                        isurf = pygame.image.load(os.path.join(os.getcwd(), 'gameover.png'))
                        irect = isurf.get_rect(center=(350,350))
                        self.screen.blit(isurf,irect)
                        t2 = 'Hearts Broken: ' + str(self.player.point)
                        text2 = self.font.render(t2,True,(255,0,0))
                        self.screen.blit(text2,(250,50))
                        
                        pygame.display.update()
                self.player.is_dead = False
                self.clock.tick()
                self.player.restart()
                self.Food.restart()
                self.Girl.restart()
                self.Enemy.restart()
                #stop the music for a little
               

        def run(self):
                pygame.mixer.music.load('bgmusic.mp3')
                while True:
                        pygame.mixer.music.play(-1, 0.0)
                        self.runGame()
                        pygame.mixer.music.stop()
                        self.game_over()
                
        def runGame(self):
                self.go.stop()
                self.startTime = time.time()                
                while True:     
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        exit()
                        self.screen.fill((0,0,0))

                        dt = self.clock.tick()
                        self.player.update(dt,self.screen)
                        
                        self.Girl.spawn(dt,self.screen,self.player)

                        #we want to spawn enemies and food after X seconds
                        timeDiff =  int(time.time()- self.startTime)
                        
                        if timeDiff > 20:
                                self.Food.spawn(dt,self.screen,self.player)

                        #when the game has progressed far enough, then the enemy despawn will be spread out much more
                        if(timeDiff) > 30 and timeDiff < 59:
                                self.Enemy.spawn(dt,self.screen,self.player)
                                self.Enemy.despawnTick = 30;
                                
                        if timeDiff > 60 and timeDiff < 119:
                                self.Enemy.despawnTick = 45;
                                
                        if timeDiff > 120 and timeDiff < 240 :
                                self.Enemy.despawnTick = 60;
                                
                        if timeDiff > 240:
                                self.Enemy.despawnTick = 120;

                        if self.player.is_dead :
                                return False
                                

                        point = self.font.render("Hearts Broken %s " % (str(self.player.point)),True,(250,250,250))
                        self.screen.blit(point,(0,0))
                        ctime = self.font.render("Time: %s" %(str(timeDiff)),True,(250,250,250))
                        self.screen.blit(ctime,(0,30))
                        pygame.display.update()


if __name__ == '__main__':
        app = Game_Window()
        app.run()
