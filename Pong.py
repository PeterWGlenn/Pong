

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


	# Game logic


	# Draw Screen 
	screen.fill(BLACK)
	# Draw Player 1
	pygame.draw.rect(screen, GREEN, [15, player_one_location, 15, 50], 0)
	# Draw Player 2
	pygame.draw.rect(screen, GREEN, [SCREEN_X - 30, player_two_location, 15, 50], 0)

	# Update display
	pygame.display.flip()

	# Frames per second limit
	clock.tick(FRAMERATE)

# Quit game
pygame.quit()


