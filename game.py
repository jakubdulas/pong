import pygame
import sys
import time
from Player import Player
from Ball import Ball
from settings import *

def move_players(player1, player2, keys):
    """
    takes players as arguments and pressed keys. The funcion changes a position of players. 
    """
    if keys[pygame.K_w]:
        player1.change_position('up')
    if keys[pygame.K_s]:
        player1.change_position('down')
    if keys[pygame.K_a]:
        player1.change_position('left')
    if keys[pygame.K_d]:
        player1.change_position('right')

    if keys[pygame.K_UP]:
        player2.change_position('up')
    if keys[pygame.K_DOWN]:
        player2.change_position('down')
    if keys[pygame.K_LEFT]:
        player2.change_position('left')
    if keys[pygame.K_RIGHT]:
        player2.change_position('right')


def show_score(scr, player1, player2, font):
    """
    displays score on the top of the display
    """
    text = font.render(f"{player1} ({player1.score}-{player2.score}) {player2}", False, (255, 255, 255))
    scr.blit(text, [win.midtop[0]-text.get_width()//2, win.midtop[1]])
 

def announce_winner(scr, font, player, ball):
    """
    displays text with winner
    """
    ball.stop()
    text = font.render(f"{player} wins!", False, (255, 215, 0))
    scr.blit(text, [win.centerx-text.get_width()//2, win.centery-text.get_height()//2])

def exit_game():
    """
    exits game after 3 seconds
    """
    time.sleep(3)
    sys.exit()

def draw_line(scr):
    """
    draws a line splitting a game area into 2 halfs
    """
    i = 0
    while i < scr.get_height():
        rect = pygame.Rect(scr.get_width()//2-2, i, 4, 15)
        i += 20
        pygame.draw.rect(scr, RED, rect)

if __name__ == '__main__':
    pygame.init()
    pygame.key.set_repeat(10, 10)

    scr = pygame.display.set_mode(WINDOW_SIZE)
    win = scr.get_rect()

    # Setting fonts
    font24 = pygame.font.SysFont('Comic Sans MS', 24)
    font64 = pygame.font.SysFont('Comic Sans MS', 64)

    # Adding players and setting initial positions
    player1 = Player(**PLAYER1_SETTINGS)
    player1.set_initial_position(win)
    player2 = Player(**PLAYER2_SETTINGS)
    player2.set_initial_position(win)

    # Grouping players
    players = pygame.sprite.Group()
    players.add(player1)
    players.add(player2)

    # Creating Ball object
    ball = Ball(player1, player2, **BALL_SETTINGS)
    ball.set_position(win.midtop)

    fps = pygame.time.Clock()
    
    stop_game = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            keys = pygame.key.get_pressed()
            move_players(player1, player2, keys)
            player1.validate_position(win.size)
            player2.validate_position(win.size)

        # Drawing line
        scr.fill(BLACK)
        draw_line(scr)

        # Balls hits a border
        ball.border_collision(win)

        # Ball and paddle collision
        player_collided = pygame.sprite.spritecollideany(ball, players)
        if player_collided is not None:
            player_collided.attack(ball)
        
        # Choosing the winner
        if player1.score == MAX_SCORE:
            announce_winner(scr, font64, player1, ball)
            stop_game = True
        
        if player2.score == MAX_SCORE:
            announce_winner(scr, font64, player2, ball)
            stop_game = True

        # Drawing elements
        ball.draw(scr)
        show_score(scr, player1, player2, font24)
        pygame.draw.rect(scr, player1.color, player1.rect)
        pygame.draw.rect(scr, player2.color, player2.rect)
        pygame.display.flip()

        if stop_game:
            exit_game()
        
        fps.tick(60)