

# Pong - Python Edition
# @author Peter Glenn
# @version 6.3.2019

# Game constants
FRAMERATE = 60
SCREEN_X = 600
SCREEN_Y = 400

# Random
import random

# Setting up pygame
import pygame
pygame.init()
size = (SCREEN_X, SCREEN_Y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
pygame.key.set_repeat(1)
GAME_FONT = pygame.font.Font('SevenSegment.ttf', 100)
BALL_IMAGE = pygame.image.load("ball.png")
ICON_IMAGE = pygame.image.load("icon.png")

POP_SOUND = pygame.mixer.Sound("pop.wav")
SCORE_SOUND = pygame.mixer.Sound("ding.wav")

pygame.display.set_icon(ICON_IMAGE)

# Defining colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
DARK_GREY = (128, 128, 128)

# Returns -1 or 1
def plus_or_minus():
	rand = random.randint(1, 3)
	if rand == 1:
		rand = 1
	else:
		rand = -1
	return rand

# Player locations and scores
player_one_location = SCREEN_Y / 2 - 15
player_two_location = SCREEN_Y / 2 - 15
player_one_score = 0
player_two_score = 0

# Ball location and velocity
ball_x = SCREEN_X / 2
ball_y = SCREEN_Y / 2
vel_x = 3 * plus_or_minus()
vel_y = 3 * plus_or_minus()

# Reset Ball Location and Velocity
def resetBallLoc():
	global SCREEN_X, SCREEN_Y, ball_x, ball_y, vel_x, vel_y

	ball_x = SCREEN_X / 2
	ball_y = random.randint(10, SCREEN_Y - 10)
	vel_x = 3 * plus_or_minus()
	vel_y = 3 * plus_or_minus()

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

	# Check one pixel at a time, with a max absolute velocity of 1000
	counter_x = min(abs(vel_x), 1000)
	counter_y = min(abs(vel_y), 1000)

	while counter_x > 0 or counter_y > 0:

		# Vertical Bounce
		if (ball_y - 10 <= 0 and vel_y < 0) or (ball_y + 10 >= SCREEN_Y and vel_y > 0):
			vel_y = -vel_y * 1.05
			POP_SOUND.play()

		# Left player bounce
		if vel_x < 0 and ball_x - 10 >= 15 and ball_x - 10 <= 30 and ball_y + 10 >= player_one_location and ball_y - 10 <= player_one_location + 50:
			if vel_x < 0:
				vel_x = -vel_x * 1.1
				POP_SOUND.play()

		# Right player bounce
		if vel_x > 0 and ball_x + 10 <= SCREEN_X - 15 and ball_x + 10 >= SCREEN_X - 30 and ball_y + 10 >= player_two_location and ball_y - 10 <= player_two_location + 50:
			if vel_x > 0:
				vel_x = -vel_x * 1.1
				POP_SOUND.play()

		# Update ball position
		if counter_x > 0:
			ball_x += abs(vel_x) / vel_x
		if counter_y > 0:
			ball_y += abs(vel_y) / vel_y

		# Update Loop Counters
		counter_x -= 1
		counter_y -= 1

	# Check for points

	# Player one scores
	if ball_x - 10 > SCREEN_X:
		resetBallLoc()
		player_one_score += 1
		SCORE_SOUND.play()
	# Player two scores
	if ball_x + 10 < 0:
		resetBallLoc()
		player_two_score += 1
		SCORE_SOUND.play()

	# Draw Screen 
	screen.fill(BLACK)

	# Write Score Text
	text_surface_player_one = GAME_FONT.render(str(player_one_score), False, DARK_GREY)
	screen.blit(text_surface_player_one, (50, 10))
	text_surface_player_two = GAME_FONT.render(str(player_two_score), False, DARK_GREY)
	screen.blit(text_surface_player_two, (SCREEN_X - GAME_FONT.size(str(player_two_score))[0] - 50, 10))

	# Draw Player 1
	pygame.draw.rect(screen, GREEN, [15, player_one_location, 15, 50], 0)

	# Draw Player 2
	pygame.draw.rect(screen, GREEN, [SCREEN_X - 30, player_two_location, 15, 50], 0)

	# Draw Screen Divider
	pygame.draw.rect(screen, DARK_GREY, [SCREEN_X / 2 - 1, 0, 2, SCREEN_Y], 0)

	# Draw Ball
	screen.blit(BALL_IMAGE, [int(ball_x) - 10, int(ball_y) - 10])

	# Update display
	pygame.display.flip()

	# Frames per second limit
	clock.tick(FRAMERATE)

# Quit game
pygame.quit()


