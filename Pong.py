

# Pong!!

# Setting up pygame
import pygame
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("test name")
clock = pygame.time.Clock()

# Defining colors
BLACK = (0, 0, 0)

# Main Game Loop
running = True
x = 0
while running:

	# Test for closed game window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Game logic
	x += 1
	print("test", x)

	# Draw screen
	screen.fill(BLACK)
	pygame.display.flip()

	# Frames per second limit
	clock.tick(60)

# Quit game
pygame.quit()


