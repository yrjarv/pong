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
    def __init__(self, position: tuple[float], window,
                 dimensions: tuple[float, float] = (20, 100),
                 color: tuple = (255, 255, 255)) -> None:
        """
        :param position: Contains the x- and y-values for the\
        rectangle to start at, starting at the top left corner of the window
        :param window: A Pygame window to draw the paddles in
        :param dimensions: Contains respectively the width and\
        height of the paddle
        :param color: The RGB value of the paddle's color, default is\
        white
        """
        self.position = list(position)
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

    def collision_wall(self, added_distance: float, index: int) -> bool:
        """
        Checks if the paddle collides with the screen
        :param added_distance: The distance to add to the paddle position.\
        To prevent it from moving into the wall because of checking before\
        movement.
        :param index: 0 or 1, depending on whether the collision is in the x\
        or y direction
        :return: True if the paddle collides with the screen, False otherwise
        """
        new_position = self.position[index] + added_distance
        max_position = (
            self.window.get_width() if index == 0 else self.window.get_height()
        )
        return (new_position <= 0 or
                new_position+self.dimensions[index] >= max_position)

    def move(self, distance: float, index: int = 1) -> None:
        """
        Moves the paddle a given amount y direction as long as that doesn't\
        make it collide witht the walls
        :param distance: How much the paddle should move
        :param index: 0 or 1, depending on whether the distance should be\
        added to the x or coordinates
        """
        if not self.collision_wall(distance, index):
            self.position[index] += distance
        self.draw()


class Ball:
    """
    Represents a ball in the game. Ball objects collide with Paddle objects
    """
    def __init__(self, position: tuple[float], window, radius: int = 10,
                 color: tuple = (255, 255, 255)) -> None:
        """
        :param position: Contains the x- and y-values for the\
        rectangle to start at, starting at the top left corner of the window
        :param window: A Pygame window to draw the ball in
        :param int radius: The radius of the ball
        :param tuple color: The RGB value of the ball's color, default is\
        white
        """
        self.position = list(position)
        self.window = window
        self.radius = radius
        self.color = color

        self.draw()

    def draw(self) -> None:
        """
        Draws the ball on self.window
        """
        pygame.draw.circle(self.window, self.color, self.position, self.radius)

    def collision_paddle(self, paddles: list[Paddle]) -> bool:
        """
        Checks if the ball collides with any of the paddles
        :param paddles: A list of Paddle objects
        :return: True if the ball collides with any of the paddles, False\
        otherwise
        """
        for paddle in paddles:
            collisions = [False, False]
            for i in range(2):
                collisions[i] = (
                    self.position[i] > paddle.position[i] and
                    self.position[i] < (paddle.position[i]
                                        + paddle.dimensions[i])
                )
            if collisions[0] and collisions[1]:
                return True
        return False

    def collision_wall(self, index: int = 1) -> bool:
        """
        Checks if the ball collides with the screen
        :param index: 0 or 1, depending on whether you want to check if it\
        collides while moving on the x-axis (i.e. with the sides) or the y-axis
        :return: True if the ball collides with the top or bottom of the\
        screen, False otherwise
        """
        dimension = self.window.get_height()
        if index == 0:
            dimension = self.window.get_width()
        return (
            self.position[index] <= 20 # top/left
            or self.position[index] >= dimension-20 # bottom/right
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
