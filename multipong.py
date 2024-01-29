"""
Pong with several balls and one paddle at the bottom of the screen
"""
# pylint: disable=no-member
import random
import pygame
import shapes

WINDOW_DIMENSIONS = (1000, 500)
PADDLE_DIMENSIONS = (200, 20)
PADDLE_SPEED = 2
BALL_SPEED = 0.1
BACKGROUND_COLOR = (0, 0, 0)

game_over = False # pylint: disable=invalid-name

pygame.init()
window = pygame.display.set_mode(WINDOW_DIMENSIONS)
font = pygame.font.SysFont('Arial', 64)

def random_ball() -> shapes.Ball:
    """
    Creates and returns a new randomly generated ball
    :returns: A shapes.Ball object with a random position and color
    """
    return shapes.Ball(
        (random.randint(20, WINDOW_DIMENSIONS[0]-20),
         random.randint(20, WINDOW_DIMENSIONS[1]-20)),
        window,
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )
def random_ball_speed() -> list[float, float]:
    """
    Generates a random ball speed and direction
    :returns: A list of two speeds, the x and y speeds of the ball, that are\
    randomly multiplied by either 1 or -1
    """
    return [
        random.choice((-BALL_SPEED, BALL_SPEED)),
        random.choice((-BALL_SPEED, BALL_SPEED))
    ]

paddle = shapes.Paddle(
    ((WINDOW_DIMENSIONS[0]-PADDLE_DIMENSIONS[0])/2, WINDOW_DIMENSIONS[1]-30),
    window,
    PADDLE_DIMENSIONS
)
balls = [random_ball()]
ball_speeds = [random_ball_speed()]

while not pygame.event.get(pygame.QUIT) and not game_over:
    window.fill(BACKGROUND_COLOR)

    # Get input, move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        paddle.move(PADDLE_SPEED, index=0)
    if keys[pygame.K_LEFT]:
        paddle.move(-PADDLE_SPEED, index=0)

    # Check all balls and draw them
    for i, ball in enumerate(balls):
        if ball.collision_wall(index=0):
            ball_speeds[i][0] *= -1
        if ball.collision_wall(index=1):
            ball_speeds[i][1] *= -1
            if ball.position[1] > WINDOW_DIMENSIONS[1]/2:
                game_over = True # pylint: disable=invalid-name
                break

        if ball.collision_paddle([paddle]):
            # Change the ball speed
            ball_speeds[i][0] *= random.choice((-1, 1))
            ball_speeds[i][1] *= -1

            # Add a new ball
            balls.append(random_ball())
            ball_speeds.append(random_ball_speed())

        ball.move(ball_speeds[i])
        ball.draw()

    # Draw paddle and score, update game
    paddle.draw()

    score = font.render(str(len(balls)), True, (255, 0, 0))
    score_rect = score.get_rect()
    window.blit(score, score_rect)

    pygame.display.update()

print(f'Score: {len(balls)}')
pygame.quit()
