<h1>Pong</h1>
<hr>
This is a simple pong game, made using Python and Pygame. Two players control one paddle each, the left one using W and S keys and the right one with arrow keys. The paddles move up and down, and the ball bounces off the paddles and the top and bottom walls. After a bounce, the speed in x and y directions is randomly multiplied, to prevent every round from being identical.
<br><br>
I have also made a multipong game, where you bounce more and more balls as the game progresses and lose when one ball hits the bottom edge of the sreen.
<h2>Installation and use</h2>
To install, download all the files or <a href='https://letmegooglethat.com/?q=Clone+repo+to+local+machine+github'>clone the repository</a>.<br>
Then, install pygame using <code>pip install pygame</code> or <code>pip install -r requirements.txt</code>. When you run the <code>main.py</code> file, the regular pong game should open. If you run <code>multipong.py</code>, a game where you have to bounce more and more balls will open.
<h2>Modifications</h2>
At the top of <code>main.py</code> and <code>multipong.py</code> files there are quite a few different constants you can change, in order to change the game. If you e.g. want a faster speed on the paddles, just change the constant related to that.