#Author: Nate Fonseka
#Release : GNU GPL v3

#class objects...this is what the users will click
import pygame
import sys,random
import string


#should do inheritance...but too lazy
class baseClass:
	def __init__ ():
		self.name = "Base"
		self.likes = set([]);
		self.images =['base']
		self.selectedImage = 'base'
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	

class cat:
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "cat"
		self.likes = set(['fishbone','yarn','milk','mouse']);
		self.images =['cat1','cat2']
		self.selectedImage = 'cat1'
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	

class dog:
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "dog"
		self.likes = set(['bone','ball','male']);
		self.images =['dog1','dog2']
		self.selectedImage = 'dog1'	
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
	
class bear:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "bear"
		self.likes = set(['fishbone','honey']);
		self.images =['bear1','bear2']
		self.selectedImage = 'bear1'
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
	

class boy:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "boy"
		self.likes = set(['ball','bat','dog','girl']);
		self.images =['boy1','boy2']
		self.selectedImage = 'boy1'
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
	

class girl:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "girl"
		self.likes = set(['flower','boy','princess','unicorn']);
		self.images =['girl1','girl2']
		self.selectedImage = 'girl1'
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	

class yarn:
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "yarn"
		self.likes = set(['granny','cat']);
		self.images =['yarn']
		self.selectedImage = 'yarn'
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class honey:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "honey"
		self.likes = set(['flower','bear']);
		self.images =['honey1','honey2']
		self.selectedImage = 'honey1'
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
	
class flower:
	
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "flower"
		self.likes = set(['girl','honey']);
		self.images =['flower']
		self.selectedImage = 'flower'
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class knight:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "knight"
		self.likes = set(['princess','sword']);
		self.images =['knight']
		self.selectedImage = 'knight'
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class princess:
	
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "princess"
		self.likes = set(['knight','girl']);
		self.images =['princess']
		self.selectedImage = 'princess'
		
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 

class sword:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "sword"
		self.likes = set(['knight']);
		self.images =['sword']
		self.selectedImage = 'sword'
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 

		
class zombie:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "zombie"
		self.likes = set(['brain']);
		self.images =['zombie']
		self.selectedImage = 'zombie'
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 

		
class bird:
	
	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "bird"
		self.likes = set(['cat','flower']);
		self.images =['bird']
		self.selectedImage = 'bird'
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class granny:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "granny"
		self.likes = set(['yarn']);
		self.images =['granny']
		self.selectedImage = 'granny'
		
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class ball:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "ball"
		self.likes = set(['bat','boy']);
		self.images =['ball']
		self.selectedImage = 'ball'
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class bat:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "bat"
		self.likes = set(['ball','boy','zombie']);
		self.images =['bat1']
		self.selectedImage = 'bat1'
	
	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class bone:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "bone"
		self.likes = set(['dog']);
		self.images =['bone1','bone2']
		self.selectedImage = 'bone1'	
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class brain:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "brain"
		self.likes = set(['zombie']);
		self.images =['brain']
		self.selectedImage = 'brain'	
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class mouse:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "mouse"
		self.likes = set(['cat','cheese']);
		self.images =['mouse']
		self.selectedImage = 'mouse'	
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 

class unicorn:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "unicorn"
		self.likes = set(['girl']);
		self.images =['unicorn']
		self.selectedImage = 'unicorn'	
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
class cheese:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "cheese"
		self.likes = set(['mouse']);
		self.images =['cheese']
		self.selectedImage = 'cheese'	
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 

class milk:

	def __init__ ():
		random.seed(42)
		indx = random.randint(0,1)
		self.selectedImage = self.images[indx]
		self.name = "milk"
		self.likes = set(['cat']);
		self.images =['milk']
		self.selectedImage = 'milk'
		
	def check_likes(arg1):
		if arg1 in self.likes:
			return True;
		return False; 
	
