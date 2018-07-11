"""
Playground for testing models
Author: dentou
"""

import pygame
import sys
from Car import Car

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Playground')



# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Set speed parameters
ACCELERATION = 100
BRAKE = 100
TURNSPEED = 30

# Setup car
x0 = 300
y0 = 300
CARWIDTH = 20
CARHEIGHT = 40
car = Car(position = (x0, y0), size = (CARWIDTH, CARHEIGHT))

# Choose whether to set car when going out of window
CARRESET = True

# Set up movement variables.
moveUp = False
moveDown = False
moveLeft = False
moveRight = False

MOVESPEED = 4

FPS = 60

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			# Change the keyboard variables.
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				moveRight = False
				moveLeft = True
			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				moveLeft = False
				moveRight = True
			if event.key == pygame.K_UP or event.key == pygame.K_w:
				moveDown = False
				moveUp = True
			if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				moveUp = False
				moveDown = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				moveLeft = False
			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				moveRight = False
			if event.key == pygame.K_UP or event.key == pygame.K_w:
				moveUp = False
			if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				moveDown = False


	# Move the car
	if moveUp:
		car.accelerate(ACCELERATION)
	if moveDown:
		car.accelerate(-ACCELERATION)
	if car.is_moving():
		if moveLeft:
			car.turn(TURNSPEED/FPS) # 30 degrees per second
		elif moveRight:
			car.turn(-TURNSPEED/FPS)
		if (not moveUp) and (not moveDown) and car.is_moving():
			car.brake(BRAKE)

	car.update(1/FPS)

	# If car goes out of window, reset
	if CARRESET:
		if ((car.model.top_left.x < 0) or (car.model.top_right.x < 0) or (car.model.bottom_left.x < 0) or (car.model.bottom_right.x < 0) or 
			(car.model.top_left.x > WINDOWWIDTH) or (car.model.top_right.x > WINDOWWIDTH) or (car.model.bottom_left.x > WINDOWWIDTH) or 
			(car.model.bottom_right.x > WINDOWWIDTH) or 
			(car.model.top_left.y < 0) or (car.model.top_right.y < 0) or (car.model.bottom_left.y < 0) or (car.model.bottom_right.y < 0) or 
			(car.model.top_left.y > WINDOWHEIGHT) or (car.model.top_right.y > WINDOWHEIGHT) or (car.model.bottom_left.y > WINDOWHEIGHT) or 
			(car.model.bottom_right.y > WINDOWHEIGHT)):
			car.reset(position = (x0, y0), size = (CARWIDTH, CARHEIGHT))



	# Draw the white background onto the surface.
	windowSurface.fill(WHITE)

	# Draw the player onto the surface.
	#pygame.draw.rect(windowSurface, BLACK, player)

	# Draw car
	car.draw(windowSurface, BLACK)

	# Draw the window onto the screen.
	pygame.display.update()
	mainClock.tick(FPS)

