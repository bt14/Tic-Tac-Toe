from game import *
from button import *
from pop_up_window import * 
import pygame
pygame.init()

win = pygame.display.set_mode((552,625))
pygame.display.set_caption("Tic Tac Toe")

font1 = pygame.font.SysFont('cambria', 16)	
font2 = pygame.font.SysFont('couriernew', 14)

player1 = Player('X', 0, True)
player2 = Player('O', 0, False)

tiles = [Tile(58,52,115,115), Tile(218,52,115,115), Tile(378,52,115,115), 
	Tile(58,213,115,115), Tile(218,213,115,115), Tile(378,213,115,113), 
	Tile(50,374,115,115), Tile(218,374,115,115), Tile(378,374,115,115)]

board = Board(725,725, tiles)

game = Game(board, player1, player2)

def redrawScreen():
	board.draw(win)

	# text that says who's turn it is
	playerLabel = font2.render(game.currentPlayerStr, True, (0,0,0))
	win.blit(playerLabel, (25, 545))

	for tile in board.tiles:
		tile.draw(win)

	# will be visible only when game is over 
	if popUp.visible:
		popUp.draw(win)

	for button in buttons:
		if button.visible:
			button.draw(win)

	if newGameMainButt.visible:
		gameOverLbl = font2.render('Game over', True, (255,0,0))
		win.blit(gameOverLbl, (235, 545))
	
	pygame.display.update()

def changePlayers():
	if game.player1.isTurn:
		game.player1.isTurn = False
		game.player2.isTurn = True
		game.currentPlayerStr = 'Player ' + player2.piece + '\'s turn'
	else: 
		game.player2.isTurn = False
		game.player1.isTurn = True
		game.currentPlayerStr = 'Player ' + player1.piece + '\'s turn'

def checkForWins():

	tiles = board.tiles

	if not game.done:
		if ((tiles[0].status and tiles[0].status == tiles[1].status and tiles[1].status == tiles[2].status) or 
			(tiles[0].status and tiles[0].status == tiles[3].status and tiles[3].status == tiles[6].status)):
			game.winner = tiles[0].status

		elif ((tiles[3].status and tiles[3].status == tiles[4].status and tiles[4].status == tiles[5].status) or
			(tiles[1].status and tiles[1].status == tiles[4].status and tiles[4].status == tiles[7].status) or
			(tiles[0].status and tiles[0].status == tiles[4].status and tiles[4].status == tiles[8].status) or
			(tiles[6].status and tiles[6].status == tiles[4].status and tiles[4].status == tiles[2].status)):
			game.winner = tiles[4].status

		elif ((tiles[6].status and tiles[6].status == tiles[7].status and tiles[7].status == tiles[8].status) or
			(tiles[2].status and tiles[2].status == tiles[5].status and tiles[5].status == tiles[8].status)):
			game.winner = tiles[8].status
		board.isFull()

	# the cases in which the game is over
	if game.winner:
		game.done = True
		popUp.visible = True
		popUp.text = 'player ' + game.winner + ' won!'
	elif board.full:
		game.done = True
		popUp.visible = True
		popUp.text = 'nobody won :('

# closes pop up window and resets the game
def newGame():
	game.newGame(win)
	popUp.close()

def exitGame():
	game.running = False

# closes pop up window without resetting the game
def closeWindow():
	game.winner = None
	board.full = False
	popUp.close()

	resetButt.visible = False
	newGameMainButt.visible = True
	# redrawScreen()

def resetGame():
	resetButt.visible = True
	newGameMainButt.visible = False
	game.newGame(win)
	
buttons = []

exitGameButt = Button(80, 300, 120, 35, 'Exit Game', font1, (0,0,0), (211,211,211), (166,166,166), exitGame, False)
newGameButt = Button(220, 300, 120, 35, 'New Game', font1, (0,0,0), (211,211,211), (166,166,166), newGame, False)	
closeWindowButt = Button(360, 300, 120, 35, 'Close', font1, (0,0,0), (211,211,211), (166,166,166), closeWindow, False)
popUpButtons = [newGameButt, exitGameButt, closeWindowButt] 
buttons.extend(popUpButtons)
popUp = PopUpWindow(60, 175, 440, 210, '', font1, (0,0,0), (230,230,230), popUpButtons)

resetButt = Button(400, 545, 120, 35, 'Reset Game', font1, (0,0,0), (211,211,211), (166,166,166), resetGame, True)
newGameMainButt = Button(resetButt.x, resetButt.y, resetButt.width, resetButt.height, 'New Game', font1, (0,0,0), (211,211,211), (166,166,166), resetGame, False)
buttons.extend([resetButt, newGameMainButt])

while game.running:

	pygame.time.delay(100)

	# update each button with the current mouse pos
	pos = pygame.mouse.get_pos()
	for button in buttons:
		button.updateHover(pos)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game.running = False

		buttonClicked = False	# True if any button is clicked this round
		for button in buttons:
			if button.get_event(event):
				buttonClicked = True

		# prevents tiles under buttons to be clicked at same time
		if not buttonClicked:
			for tile in board.tiles:
				# tile has been clicked
				if tile.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP:
					# can only place piece if the tile is empty and the game hasnt ended yet
					if tile.status == None and not game.done:	
						if game.player1.isTurn:
							tile.status = game.player1.piece
						else:
							tile.status = game.player2.piece
						changePlayers()
				
	checkForWins()  
	redrawScreen()

pygame.quit()
