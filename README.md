# Pong

This is a simple pong game, made using Python and Pygame. Two players control one paddle each, the left one using W and S keys and the right one with arrow keys. The paddles move up and down, and the ball bounces off the paddles and the top and bottom walls. After a bounce, the speed in x and y directions is randomly multiplied, to prevent every round from being identical.

I have also made a multipong game, where you bounce more and more balls as the game progresses and lose when one ball hits the bottom edge of the sreen.

## Installation and use

To install, download all the files or [clone the repository](https://letmegooglethat.com/?q=Clone+repo+to+local+machine+github).

Then, install pygame using `pip install pygame` or `pip install -r requirements.txt`. When you run the `main.py` file, the regular pong game should open. If you run `multipong.py`, a game where you have to bounce more and more balls will open.

## Modifications
At the top of `main.py` and `multipong.py` files there are quite a few different constants you can change, in order to change the game. If you e.g. want a faster speed on the paddles, just change the constant related to that.
