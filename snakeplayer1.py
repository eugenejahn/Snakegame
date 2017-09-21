
import pygame, sys, random
import random
from pygame.locals import *

windowwidth = 600
windoeheight = 600
FPS = 15


green  = (  0,204,  0)
white = (255,255,255)
black = (  0,  0,  0)
BLUE     = (  0,   0, 255)
RED      = (255,   0,   0)

bordercolor = BLUE
bgcolor = white
food    = black
snakecolor   = green
snakecolor2 = RED

up = 'up'
down = 'down'
left = 'left'
right = 'right'
ending = 'ending'

foodscore = 0
foodscore2 = 0

win = ""
wincolor = white
lose =""
losecolor = white

gap =10
randomlist = []
for i in range (10,540,10):
	for b in range (10,510,10):
		randomlist.append([i,b])
x = 35
y = 45

x2 = 355
y2 = 455

snake = [[x,y],[x,y+10],[x,y+20],[x,y+30],[x,y+40],[x,y+50],[x,y+60]]

foodPositon  = [450,300]

def main():
	global FPSCLOCK, DISPLAYSURF ,move,move2,snake,snake2,win,wincolor,lose,losecolor,foodscore,foodscore2
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((windowwidth,windoeheight))
	FPSCLOCK = pygame.time.Clock()
	move = right
	move2 = right
	foodscore = 0

	while True :
		DISPLAYSURF.fill(bgcolor)
		drawFood()
		drawborder()
		score()
		
		for event in pygame.event.get(): # event handling loop
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			if event.type ==KEYUP:
				if event.key ==K_SPACE :
					move = right
					move2= right
					x = 35
					y = 45
					x2 = 355
					y2 = 455
					
					snake = [[x,y],[x,y+10],[x,y+20],[x,y+30],[x,y+40],[x,y+50],[x,y+60]]
					foodscore = 0
					
					win = ""
					wincolor = white
					lose =""
					losecolor = white
			if event.type == KEYUP and move != ending:
				if event.key == K_UP and move != down:
					length = len(snake)
					for i in range(1,length):
						for j in range(0,2):
							snake[length-i][j] = snake[length-i-1][j]
					snake[0][1] = snake[0][1] - gap
					move = up
				if event.key == K_DOWN and move != up:
					length = len(snake)
					for i in range(1,length):
						for j in range(0,2):
							snake[length-i][j] = snake[length-i-1][j]
					snake[0][1] = snake[0][1] + gap
					move = down
				if event.key == K_RIGHT and move != left:
					length = len(snake)
					for i in range(1,length):
						for j in range(0,2):
							for j in range(0,2):
								snake[length-i][j] = snake[length-i-1][j]
					snake[0][0] = snake[0][0] + gap
					move = right
				if event.key == K_LEFT and move != right:
					length = len(snake)
					for i in range(1,length):
						for j in range(0,2):
							snake[length-i][j] = snake[length-i-1][j]
					snake[0][0] = snake[0][0] - gap
					move = left
		border()
		dead()
		end()
		eat()
		drawSnake()
		if move == up:
			length = len(snake)
			for i in range(1,length):
				for j in range(0,2):
					snake[length-i][j] = snake[length-i-1][j]
			snake[0][1] = snake[0][1] - gap
		if move == down:
			length = len(snake)
			for i in range(1,length):
				for j in range(0,2):
					snake[length-i][j] = snake[length-i-1][j]
			snake[0][1] = snake[0][1] + gap
		if move == left:
			length = len(snake)
			for i in range(1,length):
				for j in range(0,2):
					for j in range(0,2):
						snake[length-i][j] = snake[length-i-1][j]
			snake[0][0] = snake[0][0] - gap
		if move == right:
			global snake,snake2
			length = len(snake)
			for i in range(1,length):
				for j in range(0,2):
					snake[length-i][j] = snake[length-i-1][j]
			snake[0][0] = snake[0][0] + gap

		border()
		dead()
		end()
		eat()
		drawSnake()

		
		

		pygame.display.update()
		FPSCLOCK.tick(FPS)
def drawFood():
	half = 10
	left,top = foodPositon[0],foodPositon[1]
	pygame.draw.circle(DISPLAYSURF, food, (left + half, top + half), half - 5)
def drawSnake():
	length = len(snake)
	BOXSIZE = 40
	half = 30
	quarter = 10

	for x in range(0,length ):
		left,top = snake[x][0],snake[x][1]
		pygame.draw.rect(DISPLAYSURF, snakecolor, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
		#pygame.draw.line(DISPLAYSURF, snakecolor, (left, top + 1), (left + 1, top))
		#pygame.draw.line(DISPLAYSURF, snakecolor, (left + 1, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + 1))
def eat():
	global foodPositon,foodscore
	if snake[0][0]+5 == foodPositon[0] and snake[0][1]+5 == foodPositon[1]:
		snake.append([snake[0][0]-10,snake[0][1]])
		foodPositon = randomlist[random.randint(0, len(randomlist)-1)]
		print foodPositon
		foodscore = foodscore +100
	
def dead():
	global lose,losecolor,move,move2
	length = len(snake)
	for i in range (1,length):
		if snake[0] == snake[i]:
			lose = "Green Suicde"
			losecolor = green
			move = ending
			move2 =None


def border():
	if snake[0][0] <= -1:
		snake[0][0] = 535
	if snake[0][0] >= 536:
		snake[0][0] = 5
	if snake[0][1] <= -1:
		snake[0][1] = 505
	if snake[0][1] >= 506:
		snake[0][1] = 5

	
def drawborder():
	pygame.draw.line(DISPLAYSURF, bordercolor, [1,1], [1,526], 5)
	pygame.draw.line(DISPLAYSURF, bordercolor, [1,526], [558,526], 5)
	pygame.draw.line(DISPLAYSURF, bordercolor, [558,526], [558,1], 5)
	pygame.draw.line(DISPLAYSURF, bordercolor, [1,1], [558,1], 5)
def score():
	font = pygame.font.Font(None, 50)
	text1 = font.render("Score:"+str(foodscore), 1, green)
	text1pos = text1.get_rect()
	text1pos.centerx = DISPLAYSURF.get_rect().centerx
	text1pos.centery = DISPLAYSURF.get_rect().centery
	DISPLAYSURF.blit(text1, (300,550))
def end():
	font = pygame.font.Font(None, 100)
	text1 = font.render(lose, 1, losecolor)
	text1pos = text1.get_rect()
	text1pos.centerx = DISPLAYSURF.get_rect().centerx
	text1pos.centery = DISPLAYSURF.get_rect().centery
	DISPLAYSURF.blit(text1, text1pos)
def winlose():
	font = pygame.font.Font(None, 100)
	text1 = font.render(win, 1, wincolor)
	text1pos = text1.get_rect()
	text1pos.centerx = DISPLAYSURF.get_rect().centerx
	text1pos.centery = DISPLAYSURF.get_rect().centery
	DISPLAYSURF.blit(text1, text1pos)

			
		

		


if __name__ == '__main__':
    main()


	