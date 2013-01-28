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
                self.display = pygame.display.set_mode((WIN_H,WIN_W),0,32)
                self.font = pygame.font.SysFont('freesansbold.ttf',40)
                #self.display.fill((0,0,0))
        
if __name__ == '__main__':
    newgame = Game()
