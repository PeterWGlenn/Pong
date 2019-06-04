

# Pong - Python Edition
# @author Peter Glenn
# @version 6.3.2019

# Game constants
FRAMERATE = 60
SCREEN_X = 600
SCREEN_Y = 400

# Setting up pygame
import pygame
pygame.init()
size = (SCREEN_X, SCREEN_Y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
pygame.key.set_repeat(1)

# Player locations
player_one_location = SCREEN_Y / 2 - 15
player_two_location = SCREEN_Y / 2 - 15

# Ball location and velocity
ball_x = SCREEN_X / 2
ball_y = SCREEN_Y / 2
vel_x = -5
vel_y = -5

# Defining colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Main Game Loop
running = True
while running:

	# Event Listeners
	for event in pygame.event.get():
		# Closed window
		if event.type == pygame.QUIT:
			running = False

		# Key Press
		if event.type == pygame.KEYDOWN:

			keys = pygame.key.get_pressed()

			# Player one controls
			if keys[pygame.K_w] and player_one_location - 5 > 0:
				player_one_location -= 5
			if keys[pygame.K_s] and player_one_location + 5 < SCREEN_Y - 50:
				player_one_location += 5

			# Player two controls
			if keys[pygame.K_UP] and player_two_location - 5 > 0:
				player_two_location -= 5
			if keys[pygame.K_DOWN] and player_two_location + 5 < SCREEN_Y - 50:
				player_two_location += 5


	### Game logic ###

	# Vertical Bounce
	if ball_y - 8 < 0 or ball_y + 8 > SCREEN_Y:
		vel_y = -vel_y

	# Left player bounce
	if ball_x - 8 > 15 and ball_x - 8 < 30:
		vel_x = -vel_x 

	# Right player bounce
	if ball_x + 8 < SCREEN_X - 15 and ball_x + 8 > SCREEN_X - 30:
		vel_x = -vel_x 

	# Update ball position
	ball_x += vel_x
	ball_y += vel_y

	# Draw Screen 
	screen.fill(BLACK)
	# Draw Player 1
	pygame.draw.rect(screen, GREEN, [15, player_one_location, 15, 50], 0)
	# Draw Player 2
	pygame.draw.rect(screen, GREEN, [SCREEN_X - 30, player_two_location, 15, 50], 0)
	# Draw Ball
	pygame.draw.circle(screen, GREEN, [int(ball_x), int(ball_y)], 8, 0)

	# Update display
	pygame.display.flip()

	# Frames per second limit
	clock.tick(FRAMERATE)

# Quit game
pygame.quit()


