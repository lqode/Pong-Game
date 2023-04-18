# Pong: The Famous Arcade Game

## Description
There are 2 players: Left and Right. Each player has a paddle and the aim is to not miss the ball. 
The scoreboard keeps track of scores of  both players. If a player misses the ball with its paddle, 
the other player gets a point. 

The following events are tracked:
- When ball hits the top or bottom wall, it just bounces towards the same player.
- When a player hits the ball with the paddle, the ball goes towards the other player.
- When a player misses the ball, a point is awarded to the other player.

**Keywords**: Classes, Inheritance, OOP, Python.

## Requirements
Used Python 3.8 for development

### Usage
Run `main.py` to play the Pong game.

### Paddle left
width = 20, height =100, x_pos = 350, y_pos = 0

up, down - move by 20 pixels

### Paddle left
width = 20, height =100, x_pos = -350, y_pos = 0

up, down - move by 20 pixels

### Ball
width = 20, height =20, x_pos = 0, y_pos = 0
