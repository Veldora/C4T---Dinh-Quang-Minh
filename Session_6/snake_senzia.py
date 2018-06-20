import pygame
import random
from pygame.locals import *


width = 1000
height = 700
# tao khung hien thi game
display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Xenzia")


GREEN = (0, 255, 0)
YELLOW = (255, 140, 0)
WHITE = (255, 255, 255)

fps = 10   # so frame tren giay
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
            pygame.draw.circle(display_surf, GREEN, tuple(element), self.radius)

    def move(self, direction):
        if direction == "forward":
            self.elements_position.append(self.elements_position[-1][0], self.elements_position[-1][1] - 2*self.radius)
        elif direction == "backward":
            self.elements_position.append(self.elements_position[-1][0], self.elements_position[-1][1] + 2*self.radius)
        elif direction == "left":
            self.elements_position.append(self.elements_position[-1][0] - 2*self.radius, self.elements_position[-1][1])
        if direction == "right":
            self.elements_position.append(self.elements_position[-1][0] + 2*self.radius, self.elements_position[-1][1])
        self.extension = self.elements_position[0]
        self.elements_position.pop(0)

    def eat(self, food):
        self.elements_position.insert(0, self.extension)
        food.x = random.randrange(10, width - 9)
        food.y = random.randrange(10, height - 9)

    def hit_food(self, food):
        if self.elements_position[-1] == [food.x, food.y]:
            return True
        else:
            return False

    def hit_wall(self):
        if self.elements_position[-1][0] == 0 or self.elements_position[-1][0] == width \
                or self.elements_position[-1][1] == 0 or self.elements_position[-1][1] == height:
            return True
        else:
            return False

    def hit_snake(self):
        hit = False
        for element in self.elements_position:
            if self.elements_position[-1] == element:
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
        for i in range(len(self.snake.elements_position)):
            self.snake.elements_position[i][0] = int(self.snake.elements_position[i][0])
            self.snake.elements_position[i][1] = int(self.snake.elements_position[i][1])
        if self.snake.hit_food(self.food):
            self.snake.eat(self.food)
            _fps += 5
        self.snake.move(direction)
        pygame.display.update()
        fps_clock.tick(_fps)


def main():
    pygame.init()

    direction = "right"
    player = Snake([width/2, height/2], 10)
    food = Food(random.randrange(10, width - 9), random.randrange(10, height - 9), 10)
    game = Game(10, player, food)

    for i in range(len(player.elements_position)):
        player.elements_position[i][0] = int(player.elements_position[i][0])
        player.elements_position[i][1] = int(player.elements_position[i][1])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or player.hit_wall() or player.hit_snake():
                pygame.quit()
            elif event.type == KEYDOWN and event.key == K_a:
                direction = "left"
            elif event.type == KEYDOWN and event.key == K_d:
                direction = "right"
            elif event.type == KEYDOWN and event.key == K_w:
                direction = "forward"
            elif event.type == KEYDOWN and event.key == K_s:
                direction = "backward"
        game.update(fps, direction)


if __name__ == '__main__':
    main()
