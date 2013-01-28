#Nate Fonseka
#Cupid Shuffle
#Released under Creative Commons 2.0

import pygame
import player
import food
import girl
import enemy
import os
import time

class Game_Window(object):
        def __init__(self):
                pygame.init()
                self.screen = pygame.display.set_mode((700,700),0,32)
                self.clock = pygame.time.Clock()
                self.player = player.Player(700,700)
                self.Food = food.Food()
                self.Girl = girl.girl()
                self.Enemy = enemy.enemy()                
                self.font = pygame.font.SysFont('freesansbold.ttf',40)
                pygame.display.set_caption('Cupid Shuffle')

        def game_over(self):
                running = True
                gtime = 0
                while running :
                        gtime += self.clock.tick()
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        exit()
                                if event.type == pygame.KEYDOWN and gtime > 1500:
                                        running = False
                        self.screen.fill((255,255,255))
                        text = self.font.render('GAME OVER ',True,(255,0,0))
                        self.screen.blit(text,(200-text.get_width()/2,200-text.get_height()))
                        t2 = 'Hearts Broken: ' + str(self.player.point)
                        text2 = self.font.render(t2,True,(255,0,0))
                        self.screen.blit(text2,(200-text2.get_width()/2,200+text2.get_height()))
                        
                        pygame.display.update()
                self.player.is_dead = False
                self.clock.tick()
                self.player.restart()
                self.Food.restart()
                self.Girl.restart()
                self.Enemy.restart()

        def run(self):
                #the music to play during gameplay
                pygame.mixer.music.load('bgmusic.mp3')
                pygame.mixer.music.play()
                
                
                self.startTime = time.time()
                while True :
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        exit()
                        self.screen.fill((0,0,0))

                        dt = self.clock.tick()
                        self.player.update(dt,self.screen)
                        
                        self.Girl.spawn(dt,self.screen,self.player)

                        #we want to spawn enemies and food after X seconds
                        timeDiff =  int(time.time()- self.startTime)
                        
                        if timeDiff > 10:
                                self.Enemy.spawn(dt,self.screen,self.player)
                                self.Food.spawn(dt,self.screen,self.player)

                        #when the game has progressed far enough, then the enemy despawn will be spread out much more
                        if(timeDiff) > 30:
                                self.Enemy.despawnTick = 30;
                        if timeDiff > 60:
                                self.Enemy.despawnTick = 45;
                        if timeDiff > 120:
                                self.Enemy.despawnTick = 60;
                        if timeDiff > 240:
                                self.Enemy.despawnTick = 120;

                        if self.player.is_dead :
                                pygame.mixer.music.stop()
                                self.game_over()

                        point = self.font.render("Hearts Broken %s " % (str(self.player.point)),True,(250,250,250))
                        self.screen.blit(point,(0,0))
                        ctime = self.font.render("Time: %s" %(str(timeDiff)),True,(250,250,250))
                        self.screen.blit(ctime,(0,30))
                        pygame.display.update()


if __name__ == '__main__':
        app = Game_Window()
        app.run()
