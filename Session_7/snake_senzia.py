import pygame
import os
import random
import sys
from pygame.locals import *


width = 1067
height = 600
# tao khung hien thi game
display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Xenzia")
icon_surf = pygame.image.load(os.path.join('snake_icon.jpg'))
pygame.display.set_icon(icon_surf)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

fps_clock = pygame.time.Clock()


class Food:

    def __init__(self, x, y, radius):
        self.r = radius
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(display_surf, YELLOW, (self.x, self.y), self.r)


class Snake:

    def __init__(self, elements_position, radius):
        self.elements_position = elements_position
        self.radius = radius
        self.extension = [0, 0]

    def draw(self):
        for element in self.elements_position:
            center = map(int, element)
            pygame.draw.circle(display_surf, RED, tuple(center), self.radius)

    def move(self, direction):
        if direction == "forward":
            self.elements_position.append([self.elements_position[-1][0], self.elements_position[-1][1] - 2*self.radius])
        elif direction == "backward":
            self.elements_position.append([self.elements_position[-1][0], self.elements_position[-1][1] + 2*self.radius])
        elif direction == "left":
            self.elements_position.append([self.elements_position[-1][0] - 2*self.radius, self.elements_position[-1][1]])
        if direction == "right":
            self.elements_position.append([self.elements_position[-1][0] + 2*self.radius, self.elements_position[-1][1]])
        self.extension = self.elements_position[0]
        self.elements_position.pop(0)

    def eat(self, food):
        self.elements_position.insert(0, self.extension)
        food.x = random.randrange(10, width - 9)
        food.y = random.randrange(10, height - 9)

    def hit_food(self, food):
        if float(food.x) + float(self.radius + food.r) >= self.elements_position[-1][0] >= float(food.x) - float(self.radius + food.r) \
                and float(food.y) + float(self.radius + food.r) >= self.elements_position[-1][1] >= float(food.y) - float(self.radius + food.r):
            return True
        else:
            return False

    def hit_wall(self):
        if int(self.elements_position[-1][0]) <= 0 or int(self.elements_position[-1][0]) >= width \
                or int(self.elements_position[-1][1]) <= 0 or int(self.elements_position[-1][1]) >= height:
            return True
        else:
            return False

    def hit_snake(self):
        hit = False
        for element in range(len(self.elements_position) - 1):
            if self.elements_position[-1] == self.elements_position[element]:
                hit = True
                break
        if hit:
            return True
        else:
            return False


class Game:

    def __init__(self, line_thickness, snake, food):
        self.line_thickness = line_thickness
        self.snake = snake
        self.food = food

    def display_image(self, img):
        img = pygame.transform.scale(img, (width, height))
        display_surf.blit(img, (0, 0))

    def load_sound(self, music, loop, channel):
        pygame.mixer.Channel(channel).play(music, loop)

    def draw_arena(self, grass):
        display_surf.fill(BLACK)
        self.display_image(grass)
        pygame.draw.rect(display_surf, WHITE, (0, 0, width, height), self.line_thickness)
        self.food.draw()
        self.snake.draw()

    def update(self, _fps, direction, sound):
        if self.snake.hit_food(self.food):
            self.snake.eat(self.food)
            self.load_sound(sound, 0, 0)
            _fps += 1
        self.snake.move(direction)
        pygame.display.update()
        fps_clock.tick(_fps)
        return _fps


def main():
    pygame.init()

    # load image and sound
    background = pygame.image.load(os.path.join('grass.jpg')).convert()
    game_over_img = pygame.image.load(os.path.join('game_over.png')).convert()
    start = pygame.image.load(os.path.join('snake.jpg')).convert()
    eat_sound = pygame.mixer.Sound(os.path.join('eat.wav'))
    game_over_sound = pygame.mixer.Sound(os.path.join('gameover.wav'))
    start_screen = True
    music = os.path.join('electronic_loop.mp3')
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
        fps = 5
        direction = "right"
        player = Snake([[width/2, height/2]], 10)
        food = Food(random.randrange(10, width - 9), random.randrange(10, height - 9), 10)
        game = Game(10, player, food)
        die = False
        play = True

        # display game screen
        while play:
            if player.hit_wall() or player.hit_snake():
                die = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_a and direction != "right":
                    direction = "left"
                elif event.type == KEYDOWN and event.key == K_d and direction != "left":
                    direction = "right"
                elif event.type == KEYDOWN and event.key == K_w and direction != "backward":
                    direction = "forward"
                elif event.type == KEYDOWN and event.key == K_s and direction != "forward":
                    direction = "backward"
            game.draw_arena(background)
            fps = game.update(fps, direction, eat_sound)
            if die:
                game.load_sound(game_over_sound, 0, 0)
                display_surf.fill(BLACK)
                play_again = True
                while play_again:
                    game.display_image(game_over_img)
                    play_again_display = pygame.font.Font(None, 50).render("Play again?(y/n)", True, WHITE)
                    display_surf.blit(play_again_display, ((width - play_again_display.get_width()) // 2, (height - play_again_display.get_height()) // 2 + 200))
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
