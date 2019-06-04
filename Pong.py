

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
pygame.display.set_caption("test name")
clock = pygame.time.Clock()

# Player locations
player_one_location = SCREEN_Y / 2 - 15
player_two_location = SCREEN_Y / 2 - 15

# Defining colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Main Game Loop
running = True
while running:

	# Test for closed game window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

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


