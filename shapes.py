"""
Contains the shapes used in Pong
"""
import pygame
pygame.init() # pylint: disable=no-member

class Paddle:
    """
    Represents a paddle for the player to move in the game. Ball objects\
    collide with Paddle objects
    """
    def __init__(self, position: list[float], window,
                 dimensions: tuple[float, float] = (20, 100),
                 color: tuple = (255, 255, 255)) -> None:
        """
        :param list[float] position: Contains the x- and y-values for the\
        rectangle to start at, starting at the top left corner of the window
        :param window: A Pygame window to draw the paddles in
        :param tuple[float] dimensions: Contains respectively the width and\
        height of the paddle
        :param tuple color: The RGB value of the paddle's color, default is\
        white
        """
        self.position = position
        self.window = window
        self.dimensions = dimensions
        self.color = color

        self.draw()


    def draw(self) -> None:
        """
        Draws the rectangle on self.window
        """
        pygame.draw.rect(self.window, self.color,
                            (self.position[0], self.position[1],
                             self.dimensions[0], self.dimensions[1])
                        )

    def collision_wall(self, added_distance: float) -> bool:
        """
        Checks if the paddle collides with the top or bottom of the screen
        :return: True if the paddle collides with the top or bottom of the\
        screen, False otherwise
        """
        new_y = self.position[1] + added_distance
        return (new_y <= 0 or
                new_y+self.dimensions[1] >= self.window.get_height())

    def move(self, distance: float) -> None:
        """
        Moves the paddle a given amount y direction as long as that doesn't\
        make it collide witht the walls
        :param float distance: How much the paddle should move
        """
        if not self.collision_wall(distance):
            self.position[1] += distance
        self.draw()


class Ball:
    """
    Represents a ball in the game. Ball objects collide with Paddle objects
    """
    def __init__(self, position: list[float], window, radius: int = 10,
                 color: tuple = (255, 255, 255)) -> None:
        """
        :param list[float] position: Contains the x- and y-values for the\
        rectangle to start at, starting at the top left corner of the window
        :param window: A Pygame window to draw the ball in
        :param int radius: The radius of the ball
        :param tuple color: The RGB value of the ball's color, default is\
        white
        """
        self.window = window
        self.radius = radius
        self.position = position
        self.color = color

        self.draw()

    def draw(self) -> None:
        """
        Draws the ball on self.window
        """
        pygame.draw.circle(self.window, self.color, self.position, self.radius)

    def collision_paddle(self, paddles: list) -> bool:
        """
        Checks if the ball collides with any of the paddles
        :param list paddles: A list of Paddle objects
        :return: True if the ball collides with any of the paddles, False\
        otherwise
        """
        return (
            (
                self.position[0] < paddles[0].position[0]+paddles[0].dimensions[0]
                and paddles[0].position[1] < self.position[1]
                < paddles[0].position[1]+paddles[0].dimensions[1]
            )
            or
            (
                self.position[0] > paddles[1].position[0]
                and paddles[1].position[1] < self.position[1]
                < paddles[1].position[1]+paddles[1].dimensions[1]
            )

        )

    def collision_wall(self) -> bool:
        """
        Checks if the ball collides with the top or bottom of the screen
        :return: True if the ball collides with the top or bottom of the\
        screen, False otherwise
        """
        return (
            self.position[1] <= 10 # top
            or self.position[1] >= self.window.get_height()-10 # bottom
        )

    def move(self, distance: tuple[float, float]) -> None:
        """
        Moves the ball
        :param tuple[float, float] distance: How much the ball should move in\
        x and y directions
        """
        self.position[0] += distance[0]
        self.position[1] += distance[1]
        self.draw()
