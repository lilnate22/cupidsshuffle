import pygame
import random
import os

# DIR = os.path.realpath('food.py')    #out-dated

class girl_piece(object):
	def __init__(self,pos,color = (250,230,221)):
		self.m_x = pos[0]
		self.m_y = pos[1]
		self.x = self.m_x * 10
		self.y = self.m_y * 10
		self.color = color

	def blit(self,screen):
		rect = pygame.Rect(self.x,self.y,10,10)
		pygame.draw.rect(screen,self.color,rect)

class girl(object):
	def __init__(self):
		self.girls = list()

		self.time = 10000
		self.time_tick = 10000

	def random_pos(self,boy):
		running = True 
		while running:
			x,y = random.randint(1,69),random.randint(1,69)
			running = False
			for t in boy.followers :
				if t.m_x == x and t.m_y == y :
					running = True
			if x == boy.x and y == boy.y :
				running = True
			for p in self.girls :
				if p.m_x == x and p.m_y == y :
					running = True
		return x,y

	def restart(self):
		self.girls = []
		self.time = 10000

	def spawn(self,dt,screen,boy):
		self.time += dt
		if self.time >= self.time_tick or len(self.girls) <= 0:
			self.time = 0
			x,y = self.random_pos(boy)
			f_piece = girl_piece((x,y))
			self.girls.append(f_piece)

		for f_piece in self.girls :
			if f_piece.m_x == boy.x and f_piece.m_y == boy.y :
				boy.increase_length(1,5) # we kissed a girl, make her "chase" us
				self.girls.remove(f_piece)
			f_piece.blit(screen)
