import pygame
import random
import os,time



class enemy_piece(object):
	def __init__(self,pos,color = (0,50,221)):
		self.m_x = pos[0]
		self.m_y = pos[1]
                self.spawn_time = time.time()
		self.x = self.m_x * 10
		self.y = self.m_y * 10
		self.color = color

	def blit(self,screen):
		rect = pygame.Rect(self.x,self.y,10,10)
		pygame.draw.rect(screen,self.color,rect)

class enemy(object):
	def __init__(self):
		self.enemys = list()
                self.despawnTick = 10  #default despawn tick is 10 secs
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
			for p in self.enemys :
				if p.m_x == x and p.m_y == y :
					running = True
		return x,y

	def restart(self):
		self.enemys = []
		self.time = 10000

	def spawn(self,dt,screen,boy):
		self.time += dt
		if self.time >= self.time_tick or len(self.enemys) <= 0:
			self.time = 0
			x,y = self.random_pos(boy)
			f_piece = enemy_piece((x,y))
			self.enemys.append(f_piece)
		for f_piece in self.enemys :
			if f_piece.m_x == boy.x and f_piece.m_y == boy.y :
				boy.is_dead = True # we have hit an enemy...not sure if they are dads or bfs...w.e the game is over
				self.enemys.remove(f_piece)

			#we will inverse the set, and check spawn time. if it is greater than X
			currentTime = time.time()
			if(currentTime - f_piece.spawn_time) > self.despawnTick:
                                self.enemys.remove(f_piece)
			f_piece.blit(screen)
