import pygame
import time
import tictactoe as ttt
WHITE = (255,255,255)
BLACK = (0,0,0)
(WIDTH, HEIGHT) = (440, 440)
W = WIDTH//6
H = HEIGHT//6
thickness = 3
X = pygame.transform.scale(pygame.image.load('X.png'), (WIDTH//5, WIDTH//5))
O = pygame.transform.scale(pygame.image.load('O.png'), (WIDTH//5, WIDTH//5))
positions = [
	[(W,H),(3*W,H),(5*W,H)],
	[(W,3*H),(3*W,3*H),(5*W,3*H)],
	[(W,5*H),(3*W,5*H),(5*W,5*H)]
]
board = [ ['_' for c in range(3)] for r in range(3) ]

def mark(player,r,c):
	if player=='X':
		img = X
	else:
		img = O
	imgRect = img.get_rect()
	imgRect.center = positions[r][c]
	screen.blit(img, imgRect)

def DesText(s,x=220,y=500):
	pygame.draw.rect(screen,WHITE,(125,470,500,40))
	font = pygame.font.SysFont('segoeuisemilight', 25)
	text = font.render('%s'%(s), True, BLACK)
	textRect = text.get_rect()
	textRect.center = (x, y)
	screen.blit(text, textRect)


pygame.init()
screen = pygame.display.set_mode((440, 550))
pygame.display.set_caption('Beat It')
screen.fill(WHITE)
pygame.draw.rect(screen,BLACK,(0,0,WIDTH,HEIGHT),thickness)
pygame.draw.lines(screen,BLACK,False,[(WIDTH//3,0),(WIDTH//3,HEIGHT)],thickness)
pygame.draw.lines(screen,BLACK,False,[(2*(WIDTH//3),0),(2*(WIDTH//3),HEIGHT)],thickness)
pygame.draw.lines(screen,BLACK,False,[(0,HEIGHT//3),(WIDTH,HEIGHT//3)],thickness)
pygame.draw.lines(screen,BLACK,False,[(0,2*(HEIGHT//3)),(WIDTH,2*(HEIGHT//3))],thickness)
pygame.display.update()

running = True
begin = True
gameOver = False
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False	
			break
		if begin:
			DesText('Want to Start? y/n')
			pygame.display.update()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:
					choice = 'n'
				elif event.key == pygame.K_y:
					choice = 'y'
				ttt.init(choice)
				if choice == 'y' or choice == 'Y':
					HUMAN = 'X'
					AI = 'O'
					currentPlayer = HUMAN
				else:
					HUMAN = 'O'
					AI = 'X'
					currentPlayer = AI
				begin = False
		else:
			if gameOver == False:
				if currentPlayer == AI:
					DesText('AI turn')
				else:
					DesText('Your turn')
				if currentPlayer == AI:
					(r1,c1) = ttt.findOptimalMove(board)
					if (r1,c1) != (None,None):
						board[r1][c1] = AI
						mark(AI,r1,c1)
						currentPlayer = HUMAN
				elif currentPlayer == HUMAN:
					if pygame.mouse.get_pressed()[0]==1:
						x,y = pygame.mouse.get_pos()
						if x<=WIDTH and y<=HEIGHT:
							r,c = y//(HEIGHT//3),x//(HEIGHT//3)
							if board[r][c] == '_':
								board[r][c] = HUMAN
								mark(HUMAN,r,c)
								currentPlayer = AI
				pygame.display.update()
				if ttt.terminal(board):
					gameOver = True
					winner = ttt.checkWinner(board)
					if winner!=None:
						if winner == AI:
							DesText('AI wins!')
						else:
							DesText('You win!')
					else:
						DesText('Tie!')
					pygame.display.update()
pygame.quit()
