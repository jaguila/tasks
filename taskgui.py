import pygame, sys, eztext
from pygame.locals import *


car = pygame.image.load('boba.jpg')

class App:
	def __init__(self):
		self._running = True
		self._display_surf = None
		self.size = self.weight, self.height = 640, 400
		clock = pygame.time.Clock()

# initialize all pygame modules		
	def on_init(self):
		pygame.init()
		self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self._running = True

# check if quit _running		
# user inputs
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False
#compute changes in game world(npc move)			
	def on_loop(self):
		pass
	def on_render(self):
#		self._display_surf.blit(car, (50, 100))
		pygame.display.flip()
		for i in range(100):
			self._display_surf.fill((0, 0, 0))
			self._display_surf.blit(car, (i,0))
		pass

# quits all pygame modules		
	def on_cleanup(self):
		pygame.quit()
		
# initialize pygame > main loop to check events > compute render until _running is True >quit when _running is false		
	def on_execute(self):
		if self.on_init() == False:
			self._running = False
		
		while( self._running ):
			clocktic(30)
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		self.on_cleanup()

if __name__ == "__main__" :
	theApp = App()
	theApp.on_execute()