"""
Player
"""

import pygame

class Player(pygame.sprite.Sprite):
    number = 0

    def __init__(self, width=5, height=75, velocity=2, color=(255, 255, 255), name=""):
        super(Player, self).__init__()
        Player.number += 1
        self.number = Player.number
        self.name = name
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(0, 0, width, height)
        self.velocity = velocity
        self.score = 0

    def __str__(self):
        if self.name:
            return self.name
        return f"Player {self.number}"

    def set_initial_position(self, win):
        """
        sets an initial position of the paddle
        """
        if self.number == 1:
            x, y = win.midleft
            self.rect.x, self.rect.y = x+self.width, y-self.height//2
        else:
            x, y = win.midright
            self.rect.x, self.rect.y = x-2*self.width, y-self.height//2

    def change_position(self, direction):
        """
        moves the paddle
        """
        if direction == "left":
            self.rect.move_ip(-self.velocity, 0)
        if direction == "right":
            self.rect.move_ip(self.velocity, 0)
        if direction == "up":
            self.rect.move_ip(0, -self.velocity)
        if direction == "down":
            self.rect.move_ip(0, self.velocity)

    def attack(self, ball):
        """
        springs the ball
        """
        _, yb = ball.rect.midleft
        _, yp = self.rect.center

        multiplier = 1

        if ball.vec[1] > 0:
            if yb < yp:
                multiplier = -1
        else:
            if yb > yp:
                multiplier = -1
        
        ball.change_direction([-1, multiplier])
        ball.bounce()

    def validate_position(self, win_size):
        """
        checks if the paddle isn't outside the game area
        """
        x, y = self.rect.left, self.rect.top

        if x < 0:
            self.rect.left = 0
        if x > win_size[0] - self.rect.width:
            self.rect.left = win_size[0] - self.rect.width
        if y < 0: 
            self.rect.top = 0
        if y > win_size[1] - self.rect.height:
            self.rect.top = win_size[1] - self.rect.height


        if self.number == 1:
            if x > win_size[0]//2:
                self.rect.left = win_size[0]//2-self.width
        else:
            if x < win_size[0]//2:
                self.rect.left = win_size[0]//2+self.width
