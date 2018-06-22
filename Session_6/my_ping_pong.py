import pygame
import sys
from pygame.locals import *


width = 1000
height = 700
# tao khung hien thi game
display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")


WHITE = (255, 255, 255)

fps = 200   # so frame tren giay
fps_clock = pygame.time.Clock()


class Paddle:

    def __init__(self, w, h, x, y):
        self.w = w
        self.h = h
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(display_surf, WHITE, (self.x, self.y, self.w, self.h))

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
        pygame.draw.rect(display_surf, WHITE, (self.x, self.y, self.w, self.h))

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

    def draw_arena(self):
        display_surf.fill([0, 0, 0])
        pygame.draw.line(display_surf, WHITE, (width / 2, 0), (width / 2, height), 3)
        self.paddle.draw()
        self.autopaddle.draw()
        self.ball.draw()
        self.scoreboard.display()

    def update(self, pos):
        if self.ball.hit_ceiling():
            self.ball.bound('x')
        if self.ball.hit_paddle(self.paddle):
            self.ball.bound('y')
            self.scoreboard.score += 10
            if self.scoreboard.score % 20 == 0:
                self.ball.speed += 1
        if self.ball.hit_auto_paddle(self.autopaddle):
            self.ball.bound('y')
        self.ball.move()
        self.autopaddle.auto_move(self.ball)
        self.paddle.move(pos)
        pygame.display.update()
        fps_clock.tick(fps)


def main():
    global mouse_pos
    pygame.init()

    paddle = Paddle(30, 300, 0, 100)
    autopadle = AutoPaddle(width - 30, 100, 30, 300)
    ball = Ball(50, 50, 20, 20, 2)
    scoreboard = Scoreboard(width/4, 10 + 30/2, None, 30, 0)
    game = Game(10, 20, ball, paddle, autopadle, scoreboard)
    die = False
    mouse_pos = [0, 100]

    while True:
        if ball.x <= 0 and ball.hit_paddle(paddle) is False:
            die = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                die = True
            elif event.type == MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
        if die:
            pygame.quit()
            sys.exit()
        game.draw_arena()
        game.update(mouse_pos)


if __name__ == '__main__':
    main()
