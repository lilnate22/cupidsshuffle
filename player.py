import pygame

class Player_part(object):
	def __init__(self,pos,color = (10,255,25)):
		self.m_x = pos[0]
		self.m_y = pos[1]
		self.x = self.m_x * 10
		self.y = self.m_y * 10
		self.color = color

	def blit(self,screen):
		rect = pygame.Rect(self.x,self.y,10,10)
		pygame.draw.rect(screen,self.color,rect)

class Player(object) :
	def __init__(self,width,height):
		self.x = 38
		self.y = 0

		self.length = 10

		self.followers = []
		self.time_tick = 40
		self.speed = 20
		self.time = 0
		self.last_key = None
		self.h_x = -1
		self.h_y = 0

		self.head_color = (0,0,255)
		self.head = Player_part((self.x,self.y),self.head_color)
		self.point = 0
		self.is_dead = False

	def restart(self):
		self.x = 38
		self.y = 0
		self.is_dead = False
		self.length = 10
		self.followers = []
		self.speed = 1
		self.time = 0
		self.h_x = -1
		self.h_y = 0

	def update(self,dt,screen):
		self.update_position(dt)
		self.blit(screen)
		self.check_dead()

	def check_dead(self):
		for t in self.followers :
			if t.m_x == self.x and t.m_y == self.y :
				self.is_dead = True
                if self.x < 0 or self.x > 69 or self.y < 0 or self.y > 69 :
                        self.is_dead = True

	def increase_length(self,value,point):
		self.length += value
		self.point += point

	def update_position(self,dt):
		self.time += dt
		key_pressed = pygame.key.get_pressed()
		if key_pressed[pygame.K_UP] and self.h_y != +1 :
			self.h_x = 0 
			self.h_y = -1
		elif key_pressed[pygame.K_DOWN] and self.h_y != -1 :
			self.h_x = 0
			self.h_y = +1
		elif key_pressed[pygame.K_LEFT] and self.h_x != +1:
			self.h_x = -1
			self.h_y = 0
		elif key_pressed[pygame.K_RIGHT] and self.h_x != -1:
			self.h_x = +1
			self.h_y = 0
		elif key_pressed[pygame.K_a]:
			print "length: %s followers:%s" %(str(self.length),str(len(self.followers)))
		if self.time >= self.time_tick :
			self.followers.insert(0,Player_part((self.x,self.y)))
			self.x += self.h_x
			self.y += self.h_y
			self.head.x,self.head.y = self.x*10,self.y*10
			if len(self.followers) > self.length :
				self.followers.pop(len(self.followers) -1)
			self.time = 0

	def blit(self,screen):
		for t in self.followers :
			t.blit(screen)
		self.head.blit(screen)
