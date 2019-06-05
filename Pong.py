

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
pygame.font.init()
GAME_FONT = pygame.font.SysFont('Helvetica', 50)

# Player locations and scores
player_one_location = SCREEN_Y / 2 - 15
player_two_location = SCREEN_Y / 2 - 15
player_one_score = 0
player_two_score = 0

# Ball location and velocity
ball_x = SCREEN_X / 2
ball_y = SCREEN_Y / 2
vel_x = -4
vel_y = -4

# Defining colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
DARK_GREY = (128, 128, 128)

# Reset Ball Location and Velocity
def resetBallLoc(newX, newY):
	global ball_x, ball_y, vel_x, vel_y
	ball_x = newX
	ball_y = newY
	vel_x = -vel_x
	vel_y = -vel_y

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
	if ball_x - 8 > 15 and ball_x - 8 < 30 and ball_y - 8 > player_one_location and ball_y + 8 < player_one_location + 50:
		if vel_x < 0:
			vel_x = -vel_x 

	# Right player bounce
	if ball_x + 8 < SCREEN_X - 15 and ball_x + 8 > SCREEN_X - 30 and ball_y - 8 > player_two_location and ball_y + 8 < player_two_location + 50:
		if vel_x > 0:
			vel_x = -vel_x 

	# Update ball position
	ball_x += vel_x
	ball_y += vel_y

	# Check for points

	# Player one scores
	if ball_x - 8 > SCREEN_X:
		resetBallLoc(SCREEN_X - 30 - 8, player_two_location + 50 / 2)
		player_one_score += 1
	# Player two scores
	if ball_x + 8 < 0:
		resetBallLoc(30 + 8, player_one_location + 50 / 2)
		player_two_score += 1

	# Draw Screen 
	screen.fill(BLACK)
	# Write Score Text
	text_surface_player_one = GAME_FONT.render(str(player_one_score), False, DARK_GREY)
	screen.blit(text_surface_player_one, (20, 10))
	text_surface_player_two = GAME_FONT.render(str(player_two_score), False, DARK_GREY)
	screen.blit(text_surface_player_two, (SCREEN_X - GAME_FONT.size(str(player_two_score))[0] - 20, 10))
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


