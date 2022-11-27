"""
Ball
"""
import pygame
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self, player1, player2, size=20, velocity=4,
                 color=(255, 255, 255), change_color=True, change_size=True,
                 change_velocity=True):
        super(Ball, self).__init__()
        self.rect = pygame.Rect(0, 0, size, size)
        self.velocity = velocity
        self.color = color
        self.player1 = player1
        self.player2 = player2
        self.bounces = 0
        self.size = size
        self.change_color = change_color
        self.change_size = change_size
        self.change_velocity = change_velocity
        self.initial_velocity = velocity
        choose_side = random.choice([-1, 1])
        self.vec = [choose_side*self.velocity, -self.velocity]

    def draw(self, win):
        """
        updates and draws a ball
        """
        multiplierx = multipliery = 1
        if self.vec[0] < 0:
            multiplierx = -1
        if self.vec[1] < 0:
            multipliery = -1

        self.vec = [multiplierx*self.velocity, multipliery*self.velocity]
        self.rect.move_ip(self.vec)
        pygame.draw.rect(win, self.color, self.rect)

    def set_position(self, position):
        """
        sets initial position
        """
        self.rect.x, self.rect.y = position

    def change_direction(self, direction):
        """
        changes direction vector
        """
        x, y = direction
        self.vec = [x*self.vec[0], y*self.vec[1]]

        displacement = [self.vec[0]*self.player1.velocity,
                        self.vec[1]*self.player1.velocity]
        self.rect.move_ip(displacement)

    def border_collision(self, win):
        """
        changes vector if a ball hits a wall and
        place the ball if a player score a point
        """
        if self.rect.top < win.top or self.rect.bottom > win.bottom:
            self.vec[1] *= -1

        if self.rect.left < win.left:
            self.player2.score += 1
            self.player1.set_initial_position(win)
            self.player2.set_initial_position(win)
            self.reset(win, -1)

        if self.rect.right > win.right:
            self.player1.score += 1
            self.player1.set_initial_position(win)
            self.player2.set_initial_position(win)
            self.reset(win, 1)

    def stop(self):
        """
        stops the ball
        """
        self.vec = [0, 0]
        self.color = (0, 0, 0)

    def bounce(self):
        """
        count bounce and changes appearance of the ball
        """
        self.bounces += 1
        difficulty_level = self.bounces//3
        if self.bounces % 3 == 0:
            self._change_color()
            self._change_size()
            self._change_velocity(difficulty_level)

    def reset(self, win, mulitplier):
        """
        resets ball settings
        """
        self.rect.x, self.rect.y = win.midtop
        self.bounces = 0
        self.color = (255, 255, 255)
        self.velocity = self.initial_velocity
        self.vec[0] = mulitplier
        self.rect.width = self.size
        self.rect.height = self.size

    def _change_velocity(self, difficulty_level):
        """
        increases the velocity of the ball
        """
        if self.change_velocity:
            self.velocity += difficulty_level

    def _change_size(self):
        """
        sets a random ball size in a range of [size/2, size]
        """
        if self.change_size:
            size = random.randint(self.size//2, self.size)
            self.rect.width = size
            self.rect.height = size

    def _change_color(self):
        """
        sets a color of the ball to random
        """
        if self.change_color:
            rgb = random.randint(0xAAAAAA, 0xFFFFFF)
            self.color = pygame.color.Color(rgb)
