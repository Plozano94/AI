import numpy as np
import time
import pygame

#Parameters
rows=80
columns=80
refresh_time=0.1
width=600
height=600
cycles=1000
background_colour = (200,0,0)
empty_color=(0,0,0)
active_color=(255,255,255)


#class
class GameOfLife:
	numero_filas=rows
	numero_columnas=columns
	grid=np.array([])
	def start(self,):
		#self.grid=np.zeros(shape=(self.numero_filas,self.numero_columnas))
		self.grid=np.random.random_integers(0,1,(self.numero_filas,self.numero_columnas))
		return

	def refresh(self,):
		grid2=np.random.random_integers(0,0,(self.numero_filas,self.numero_columnas))
		for i in range(0,self.numero_filas-1):
			for j in range(0,self.numero_columnas-1):
				grid2[i][j]=self.checkSquare(i,j)
		self.grid=grid2
		return

	def checkSquare(self, x,y):
		cont=0
		if self.grid[x][y]:
			for i in range(-1,2):
				if self.grid[x+i][y-1]:
					cont+=1
			for i in [-1,1]:
				if self.grid[x+i][y]:
					cont+=1
			for i in range(-1,2):
				if self.grid[x+i][y+1]:
					cont+=1
			if cont>3 or cont<2:
				return 0
			else:
				return 1
		if not self.grid[x][y]:
			for i in range(-1,2):
				if self.grid[x+i][y-1]:
					cont+=1
			for i in [-1,1]:
				if self.grid[x+i][y]:
					cont+=1
			for i in range(-1,2):
				if self.grid[x+i][y+1]:
					cont+=1
			if cont==3:
				return 1
			else:
				return 0

#setting up de application
game=GameOfLife()
game.start()

pygame.init()
block_size=width/rows
window = pygame.display.set_mode((width,height))
window.fill(background_colour)


for a in range(cycles):
	game.refresh()
	window.fill(background_colour)
	for i in range(0,game.numero_filas):
			for j in range(0,game.numero_columnas):
				if not game.grid[i][j]:
					rect = pygame.Rect(j*(block_size+1), i*(block_size+1), block_size, block_size)
					pygame.draw.rect(window, empty_color, rect)
				if game.grid[i][j]:
					rect = pygame.Rect(j*(block_size+1),i*(block_size+1), block_size+1, block_size+1)
					pygame.draw.rect(window, active_color, rect)


	print str(game.grid)
	pygame.display.update()
	time.sleep(refresh_time)
