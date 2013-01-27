#Author: Nate Fonseka
#Release : GNU GPL v3

#class objects...this is what the users will click
import pygame
import sys,random
import string


#should do inheritance...but too lazy
class baseClass:
	self.name = "Base"
	self.likes = set([]);
	self.images =['base']
	self.selectedImage = 'base'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	

class cat:
	self.name = "cat"
	self.likes = set(['fishbone','yarn','milk','mouse']);
	self.images =['cat1','cat2']
	self.selectedImage = 'cat1'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	

class dog:
	self.name = "dog"
	self.likes = set(['bone','ball','male']);
	self.images =['dog1','dog2']
	self.selectedImage = 'dog1'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
	
class bear:
	self.name = "bear"
	self.likes = set(['fishbone','honey']);
	self.images =['bear1','bear2']
	self.selectedImage = 'bear1'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
	

class boy:
	self.name = "boy"
	self.likes = set(['ball','bat','dog','girl']);
	self.images =['boy1','boy2']
	self.selectedImage = 'boy1'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
	

class girl:
	self.name = "girl"
	self.likes = set(['flower','boy','princess','unicorn']);
	self.images =['girl1','girl2']
	self.selectedImage = 'girl1'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	

class yarn:
	self.name = "yarn"
	self.likes = set(['granny','cat']);
	self.images =['yarn']
	self.selectedImage = 'yarn'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class honey:
	self.name = "honey"
	self.likes = set(['flower','bear']);
	self.images =['honey1','honey2']
	self.selectedImage = 'honey1'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
	
class flower:
	self.name = "flower"
	self.likes = set(['girl','honey']);
	self.images =['flower']
	self.selectedImage = 'flower'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class knight:
	self.name = "knight"
	self.likes = set(['princess','sword');
	self.images =['knight']
	self.selectedImage = 'knight'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class princess:
	self.name = "princess"
	self.likes = set(['knight','girl']);
	self.images =['princess']
	self.selectedImage = 'princess'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 

class sword:
	self.name = "sword"
	self.likes = set(['knight']);
	self.images =['sword']
	self.selectedImage = 'sword'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 

		
class zombie:
	self.name = "zombie"
	self.likes = set(['brain']);
	self.images =['zombie']
	self.selectedImage = 'zombie'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 

		
class bird:
	self.name = "bird"
	self.likes = set(['cat','flower']);
	self.images =['bird']
	self.selectedImage = 'bird'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class granny:
	self.name = "granny"
	self.likes = set(['yarn']);
	self.images =['granny']
	self.selectedImage = 'granny'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class ball:
	self.name = "ball"
	self.likes = set(['bat','boy']);
	self.images =['ball']
	self.selectedImage = 'ball'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class bat:
	self.name = "bat"
	self.likes = set(['ball','boy','zombie']);
	self.images =['bat1']
	self.selectedImage = 'bat1'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class bone:
	self.name = "bone"
	self.likes = set(['dog']);
	self.images =['bone1','bone2']
	self.selectedImage = 'bone1'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class brain:
	self.name = "brain"
	self.likes = set(['zombie']);
	self.images =['brain']
	self.selectedImage = 'brain'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class mouse:
	self.name = "mouse"
	self.likes = set(['cat','cheese']);
	self.images =['mouse']
	self.selectedImage = 'mouse'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 

class unicorn:
	self.name = "unicorn"
	self.likes = set(['girl']);
	self.images =['unicorn']
	self.selectedImage = 'unicorn'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class cheese:
	self.name = "cheese"
	self.likes = set(['mouse']);
	self.images =['cheese']
	self.selectedImage = 'cheese'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 

class milk:
	self.name = "milk"
	self.likes = set(['cat']);
	self.images =['milk']
	self.selectedImage = 'milk'
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
