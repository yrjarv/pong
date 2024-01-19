"""
Main program for the game Pong
"""
# pylint: disable=E1101
import random
import pygame
import shapes

# Constants
PADDLE_SPEED = 0.75
WINDOW = (800, 600)
TPS = 200
BACKGROUNDCOLOR = (0, 0, 0)
GAMECOLOR = (255, 255, 255)

# Starting values
player_scores = [0, 0]

# Functions to randomize ball behaviour
def random_start_ball_speed() -> tuple[float, float]:
    """
    Generates a tuple with two random numbers, representing the vector of\
    the ball's speed.
    :returns tuple[float, float]: The vector of the ball's speed
    """
    return (
        random.choice([-1, 1]) * random.uniform(0.3, 0.75) * 0.5,
        random.choice([-1, 1]) * random.uniform(0.1, 0.3)
    )

def random_paddle_collision_ball_speed(previous_ball_speed: tuple[float, float]
                                       ) -> tuple[float, float]:
    """
    Generates a tuple with two numbers that are the result of random\
    multiplication of the previous ball speed. The new ball speed has a 2/3\
    chance of being in the same direction as the previous, leading to more\
    unpredictable and non-repetetive gameplay.
    :param tuple[float, float] previous_ball_speed: The previous ball speed
    :returns tuple[float, float]: The new ball speed
    """
    x_multiplier = random.uniform(0.95, 1.25)
    return (
        previous_ball_speed[0] * -1 * x_multiplier,
        previous_ball_speed[1] * random.choice((-1, 1, 1)) * x_multiplier * 0.8
    )

# Initialize pygame, set up window and tick speed
pygame.init()
pygame.time.Clock().tick(TPS)
window = pygame.display.set_mode(WINDOW)
window.fill(BACKGROUNDCOLOR)
font = pygame.font.SysFont('Arial', 48)

# Initialise all elements
paddles = [
    shapes.Paddle([20, 250], window, color=GAMECOLOR),
    shapes.Paddle([760, 250], window, color=GAMECOLOR)
]
ball = shapes.Ball([400, 300], window)
ball_speed = random_start_ball_speed()
ball.position = [window.get_width()/2, window.get_height()/2]

# Game loop
while True:
    # Break loop if user closes pygame window
    if pygame.event.get(pygame.QUIT):
        break

    # Get key input
    keys = pygame.key.get_pressed()
    # Moving according to input
    if keys[pygame.K_w]:
        paddles[0].move(-PADDLE_SPEED)
    if keys[pygame.K_s]:
        paddles[0].move(PADDLE_SPEED)
    if keys[pygame.K_UP]:
        paddles[1].move(-PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        paddles[1].move(PADDLE_SPEED)

    # Movement and multiplication/randomisation of speed
    if ball.collision_wall():
        ball_speed = (ball_speed[0], ball_speed[1]*random.uniform(-1.2, -0.95))
    if ball.collision_paddle(paddles):
        ball_speed = random_paddle_collision_ball_speed(ball_speed)
    ball.move(ball_speed)

    # Checking winners, changing scores and resetting the ball
    if not (0 < ball.position[0] < window.get_width()
            and -10 < ball.position[1] < window.get_height()+10):
        if ball.position[0] <= 0:
            player_scores[1] += 1
        elif ball.position[0] >= window.get_width():
            player_scores[0] += 1
        ball.position = [window.get_width()/2, window.get_height()/2]
        ball_speed = random_start_ball_speed()

    # Draw all objects and update score text
    for paddle in paddles:
        paddle.draw()
    ball.draw()
    text = font.render(f'{player_scores[0]} : {player_scores[1]}', True,
                       GAMECOLOR)
    text_rect = text.get_rect(center=(window.get_width()/2, 50))
    window.blit(text, text_rect)
    pygame.display.update()
    window.fill(BACKGROUNDCOLOR)

    # Quit if esc is pressed, done after the rendering to ensure that all
    # objects are still drawn
    if keys[pygame.K_ESCAPE]:
        break

# Game done
while not pygame.event.get(pygame.QUIT):
    continue
pygame.quit() # Quits only when pygame window is closed
