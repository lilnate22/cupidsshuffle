#Nate Fonseka
#Cupid Shuffle
#Released under Creative Commons 2.0

import pygame
import player
import food
import girl
import os

class Game_Window(object):
        def __init__(self):
                pygame.init()

                self.screen = pygame.display.set_mode((700,700),0,32)
                self.clock = pygame.time.Clock()
                self.player = player.Player(700,700)
                self.Food = food.Food()
                self.Girl = girl.girl()
                
                self.font = pygame.font.SysFont('freesansbold.ttf',40)

        def game_over(self):
                running = True
                time = 0
                while running :
                        time += self.clock.tick()
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        exit()
                                if event.type == pygame.KEYDOWN and time > 1500:
                                        running = False
                        self.screen.fill((255,255,255))
                        text = self.font.render('GAME OVER ',True,(255,0,0))
                        self.screen.blit(text,(200-text.get_width()/2,200-text.get_height()))
                        t2 = 'Points for Hearts Broken: ' + str(self.player.point)
                        text2 = self.font.render(t2,True,(255,0,0))
                        self.screen.blit(text2,(200-text2.get_width()/2,200+text2.get_height()))
                        
                        pygame.display.update()
                self.player.is_dead = False
                self.clock.tick()
                self.player.restart()
                self.Food.restart()
                self.Girl.restart()
                

        def run(self):
                #the music to play during gameplay
                pygame.mixer.music.load('bgmusic.mp3')
                pygame.mixer.music.play()
                while True :
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        exit()
                        self.screen.fill((0,0,0))

                        dt = self.clock.tick()
                        self.player.update(dt,self.screen)
                        self.Food.spawn(dt,self.screen,self.player)
                        self.Girl.spawn(dt,self.screen,self.player)
                        

                        if self.player.is_dead :
                                self.game_over()

                        point = self.font.render(str(self.player.point),True,(0,0,0))
                        self.screen.blit(point,(0,0))
                        pygame.display.update()


if __name__ == '__main__':
        app = Game_Window()
        app.run()
