import pygame
import random
import sys
from pygame.locals import *


width = 1000
height = 700
# tao khung hien thi game
display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Xenzia")


GREEN = (0, 255, 0)
YELLOW = (255, 140, 0)
WHITE = (255, 255, 255)

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
            pygame.draw.circle(display_surf, GREEN, tuple(center), self.radius)

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

    def draw_arena(self):
        display_surf.fill([0, 0, 0])
        pygame.draw.rect(display_surf, WHITE, (0, 0, width, height), self.line_thickness)
        self.snake.draw()
        self.food.draw()

    def update(self, _fps, direction):
        if self.snake.hit_food(self.food):
            self.snake.eat(self.food)
            _fps += 1
        self.snake.move(direction)
        pygame.display.update()
        fps_clock.tick(_fps)
        return _fps


def main():
    pygame.init()

    fps = 5
    direction = "right"
    player = Snake([[width/2, height/2]], 10)
    food = Food(random.randrange(10, width - 9), random.randrange(10, height - 9), 10)
    game = Game(10, player, food)
    die = False

    while True:
        if player.hit_wall() or player.hit_snake():
            die = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                die = True
            elif event.type == KEYDOWN and event.key == K_a and direction != "right":
                direction = "left"
            elif event.type == KEYDOWN and event.key == K_d and direction != "left":
                direction = "right"
            elif event.type == KEYDOWN and event.key == K_w and direction != "backward":
                direction = "forward"
            elif event.type == KEYDOWN and event.key == K_s and direction != "forward":
                direction = "backward"
        if die:
            pygame.quit()
            sys.exit()
        game.draw_arena()
        fps = game.update(fps, direction)


if __name__ == '__main__':
    main()
