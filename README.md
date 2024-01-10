<h1>Pong</h1>
<hr>
This is a simple pong game, made using Python and Pygame. Two players control one paddle each, the left one using W and S keys and the right one with arrow keys. The paddles move up and down, and the ball bounces off the paddles and the top and bottom walls. After a bounce, the speed in x and y directions is randomly multiplied, to prevent every round from being identical.
<h2>Installation and use</h2>
To install, download all the files or <a href='https://letmegooglethat.com/?q=Clone+repo+to+local+machine+github'>clone the repository</a>.<br>
Then, install pygame using `pip install pygame` or `pip install -r requirements.txt`. When you run `main.py`, the game should open.
<h2>Modifications</h2>
At the top of `main.py` there are quite a few different constants you can change, in order to change the game. The randomized movement is also controlled by the two functions at lines 20 and 31, which can be changed to suit your needs.
