import pygame
import sys
import random
import os.path
from pygame.locals import *


width = 1067
height = 600
# tao khung hien thi game
display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")
icon_surf = pygame.image.load(os.path.join('background.gif'))
pygame.display.set_icon(icon_surf)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

fps = 200   # so frame tren giay
fps_clock = pygame.time.Clock()


class Paddle:

    def __init__(self, w, h, x, y):
        self.w = w
        self.h = h
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(display_surf, RED, (self.x, self.y, self.w, self.h))

    def move(self, pos):
        self.y = pos[1] - self.h/2
        if self.y < 0:
            self.y = 0
        elif self.y > height - self.h:
            self.y = height - self.h


class AutoPaddle(Paddle):

    def __init__(self, x, y, w, h):
        super().__init__(w, h, x, y)

    def auto_move(self, ball):
        self.y = ball.y - self.h/2
        if self.y < 0:
            self.y = 0
        elif self.y > height - self.h:
            self.y = height - self.h


class Ball:

    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.dir_x = 1  # 1 right and -1 left
        self.dir_y = 1  # -1 up and 1 down

    def draw(self):
        pygame.draw.rect(display_surf, GREEN, (self.x, self.y, self.w, self.h))

    def move(self):
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed

    def bound(self, axis):
        if axis == 'x':
            self.dir_y = - self.dir_y
        if axis == 'y':
            self.dir_x = - self.dir_x

    def hit_ceiling(self):
        if self.y <= 0 or self.y >= (height - self.h):
            return True
        else:
            return False

    def hit_paddle(self, paddle):
        if (paddle.y - self.h) <= self.y <= (paddle.y + paddle.h) and self.x <= (paddle.x + paddle.w):
            return True
        else:
            return False

    def hit_auto_paddle(self, autopaddle):
        if (autopaddle.y - self.h) <= self.y <= (autopaddle.y + autopaddle.h) and self.x + self.w >= autopaddle.x:
            return True
        else:
            return False


class Scoreboard:

    def __init__(self, x, y, font, size, score):
        self.x = x
        self.y = y
        self.font = font
        self.size = size
        self.score = score

    def display(self):
        font = pygame.font.Font(self.font, self.size)
        display_score = font.render("Score: " + str(self.score), True, WHITE)
        display_surf.blit(display_score, (self.x, self.y))


class Game:

    def __init__(self, line_thickness, speed, ball, paddle, autopaddle, scoreboard):
        self.line_thickness = line_thickness
        self.speed = speed
        self.ball = ball
        self.paddle = paddle
        self.autopaddle = autopaddle
        self.scoreboard = scoreboard

    def display_image(self, img):
        img = pygame.transform.scale(img, (width, height))
        display_surf.blit(img, (0, 0))

    def load_sound(self, music, loop, channel):
        pygame.mixer.Channel(channel).play(music, loop)

    def draw_arena(self, background):
        display_surf.fill(BLACK)
        self.display_image(background)
        pygame.draw.line(display_surf, WHITE, (width / 2, 0), (width / 2, height), 3)
        self.paddle.draw()
        self.autopaddle.draw()
        self.ball.draw()
        self.scoreboard.display()

    def update(self, pos, sound):
        if self.ball.hit_ceiling():
            self.ball.bound('x')
            self.load_sound(sound, 0, 0)
        if self.ball.hit_paddle(self.paddle):
            self.ball.bound('y')
            self.scoreboard.score += 10
            if self.scoreboard.score % 20 == 0:
                self.ball.speed += 1
            self.load_sound(sound, 0, 0)
        if self.ball.hit_auto_paddle(self.autopaddle):
            self.ball.bound('y')
            self.load_sound(sound, 0, 0)
        self.ball.move()
        self.autopaddle.auto_move(self.ball)
        self.paddle.move(pos)
        pygame.display.update()
        fps_clock.tick(fps)


def main():
    global mouse_pos
    pygame.init()
    high_score = 0

    # load image and sound
    background = pygame.image.load(os.path.join('wallhaven.jpg')).convert()
    game_over_img = pygame.image.load(os.path.join('game_over.png')).convert()
    start = pygame.image.load(os.path.join('ping.png')).convert()
    ball_img = pygame.image.load(os.path.join('ball.png')).convert()
    hit_wall_sound = pygame.mixer.Sound(os.path.join('hit_wall.wav'))
    game_over_sound = pygame.mixer.Sound(os.path.join('gameover.wav'))
    start_screen = True
    music = os.path.join('techno_house_loop.mp3')
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)

    # display start screen
    while start_screen:
        start = pygame.transform.scale(start, (width, height))
        display_surf.blit(start, (0, 0))
        start_screen_display = pygame.font.Font(None, 40).render("Press any key to start!!!", True, WHITE)
        display_surf.blit(start_screen_display, (width/2 + 150, height - 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                start_screen = False
        pygame.display.update()

    while True:
        paddle = Paddle(30, 200, 0, 100)
        autopadle = AutoPaddle(width - 30, 100, 30, 200)
        ball = Ball(random.randrange(50, width - 50), random.randrange(50, height - 50), 20, 20, 5)
        scoreboard = Scoreboard(width / 4, 10 + 30 / 2, None, 30, 0)
        game = Game(10, 20, ball, paddle, autopadle, scoreboard)
        play = True
        die = False
        mouse_pos = [0, 100]

        # display game screen
        while play:
            if ball.x <= 0 and ball.hit_paddle(paddle) is False:
                die = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()

            game.draw_arena(background)
            game.update(mouse_pos, hit_wall_sound)
            if die:
                if scoreboard.score > high_score:
                    high_score = scoreboard.score
                game.load_sound(game_over_sound, 0, 0)
                display_surf.fill(BLACK)
                for i in range(150):
                    game.display_image(game_over_img)
                    pygame.display.update()
                display_surf.fill(BLACK)
                play_again = True
                while play_again:
                    game.display_image(ball_img)
                    game_over = pygame.font.Font(None, 120).render("Your score: " + str(scoreboard.score), True, BLACK)
                    high_score_display = pygame.font.Font(None, 50).render("High score: " + str(high_score), True, BLACK)
                    play_again_display = pygame.font.Font(None, 50).render("Play again?(y/n)", True, BLACK)
                    display_surf.blit(game_over, ((width - game_over.get_width()) // 2, (height - game_over.get_height()) // 2 - 100))
                    display_surf.blit(high_score_display, ((width - high_score_display.get_width()) // 2, (height - game_over.get_height()) // 2))
                    display_surf.blit(play_again_display, ((width - play_again_display.get_width()) // 2, (height - game_over.get_height()) // 2 + 200))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_n):
                            pygame.quit()
                            sys.exit()
                        elif event.type == KEYDOWN and event.key == K_y:
                            play_again = False
                            play = False
                    pygame.display.update()


if __name__ == '__main__':
    main()
