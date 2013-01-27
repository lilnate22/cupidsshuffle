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
	
	