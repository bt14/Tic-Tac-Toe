import pygame
from button import *

bd = pygame.transform.scale(pygame.image.load('pics\\board.png'), (552,540)) 

# picX = pygame.transform.scale(pygame.image.load('pics\\X.png'), (110,114))
# picO = pygame.transform.scale(pygame.image.load('pics\\O.png'), (114,110))

class Game():
	
	def __init__(self, board, player1, player2):
		self.board = board
		self.player1 = player1
		self.player2 = player2
		self.currentPlayerStr = 'Player ' + player1.piece + '\'s turn'  #player1 always goes first
		self.done = False
		self.winner = None
		self.running = True

	def newGame(self, win):
		self.currentPlayerStr = 'Player ' + self.player1.piece + '\'s turn'
		self.done = False
		self.winner = None
		self.player1.isTurn = True
		self.player2.isTurn = False
		self.board.clear(win)

class Board:

	def __init__(self, height, width, tiles):
		self.height = height
		self.width = width
		self.tiles = tiles	#array of tiles	
		self.full = False	

	# draws board and background
	def draw(self, win):
		win.fill((247,247,247))
		win.blit(bd, (0,0))

	def clear(self, win):
		for tile in self.tiles:
			tile.empty(win)

	def isFull(self):
		for tile in self.tiles:
			if not tile.status:
				self.full = False
				return
		self.full = True
		return

class Tile():

	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.rect = pygame.Rect(x, y, width, height)
		self.status = None	# None if empty, or 'X' or 'O'

	def draw(self, win):
		# blits the status (ie the player's piece onto the tile)
		font = pygame.font.SysFont('couriernew', 40, True)
		label = font.render(self.status, True, (0,0,0))
		label_rect = label.get_rect(center=self.rect.center)
		win.blit(label, label_rect)
			# maybe change to pictures instead of labels later

	def empty(self, win):
		self.status = None	
		self.draw(win)
		pygame.display.update()
	
class Player:

	def __init__(self, piece, score, isTurn):
		self.piece = piece
		self.score = score
		self.isTurn = isTurn

	