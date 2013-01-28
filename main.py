#Cupid Shuffle
#Author: Nate Fonseka
#Released under GNU GPL v3
#Github: lilnate22/cupidsshuffle
import pygame, sys,random, time
from pygame.locals import *
import pygame.gfxdraw
import os

WIN_H = 700
WIN_W = 700

class Game:
        def __init__(self):
                pygame.init()
                self.screen = pygame.display.set_mode((700,700),0,32)
                self.font = pygame.font.SysFont('freesansbold.ttf',40)
                #self.display.fill((0,0,0))
                self.clock = pygame.time.Clock()
                
        def end(self):
                running = True
                time = 0 # we will need this if the game freezes up
                while running:
                        time = time + self.clock.tick()

                        #we need the quit event from pygame
                        for event in pygame.event.get():
                                
                                if event.type == pygame.QUIT:
                                        sys.exit()
                                elif event.type == pygame.KEYDOWN and time > 1500:  #timed with the keypress...dont know what is going on
                                        running = False
                        self.screen.fill((255,130,120))
                        
        
if __name__ == '__main__':
    newgame = Game()
