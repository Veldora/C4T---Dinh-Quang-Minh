import pygame
import os
import sys
import random
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

width = 1067
height = 600
# tao khung hien thi game
display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Shooter")

fps = 5  # so frame tren giay
fps_clock = pygame.time.Clock()


class Chicken:

    def __init__(self, x, y, radius):
        self.x = int(x)
        self.y = int(y)
        self.radius = int(radius)

    def draw(self):
        pygame.draw.circle(display_surf, WHITE, (self.x, self.y), self.radius)

    def check_hit_ship(self, ship):
        if self.x + self.radius >= ship.x >= self.x - self.radius - ship.width \
                and self.y + self.radius >= ship.y >= self.y - self.radius - ship.height:
            return True
        else:
            return False

    def check_hit_floor(self):
        if self.y >= height:
            return True
        else:
            return False

    def move(self, speed):
        self.y += speed


class Bullet:

    def __init__(self, x, y, radius):
        self.x = int(x)
        self.y = int(y)
        self.index = 0
        self.radius = int(radius)

    def draw(self):
        pygame.draw.circle(display_surf, WHITE, (self.x, self.y), self.radius)

    def check_hit_chicken(self, chickens, bullets, scoreboard):
        for chicken_index, chicken in enumerate(chickens):
            if chicken.x + self.radius + chicken.radius >= self.x >= chicken.x - self.radius + chicken.radius \
                    and chicken.y + self.radius + chicken.radius >= self.y >= chicken.y - self.radius + chicken.radius:
                scoreboard.score += 10
                chickens.pop(chicken_index)
                bullets.pop(self.index)

    def check_out_of_range(self, bullets):
        if self.y <= 0:
            bullets.pop(self.index)

    def move(self, speed):
        self.y -= speed


class Ship:

    def __init__(self, w, h, x, y, speed):
        self.width = int(w)
        self.height = int(h)
        self.x = int(x)
        self.y = int(y)
        self.dir_x = 0
        self.dir_y = 0
        self.speed = int(speed)

    def draw(self):
        pygame.draw.rect(display_surf, WHITE, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        self.dir_x = 0
        self.dir_y = 0

    def shoot(self, bullets):
        bullet = Bullet(self.x, self.y, 10)
        bullets.append(bullet)


class Scoreboard:

    def __init__(self, x, y, font, size, score):
        self.x = int(x)
        self.y = int(y)
        self.font = font
        self.size = int(size)
        self.score = score

    def display(self):
        font = pygame.font.Font(self.font, self.size)
        display_score = font.render("Score: " + str(self.score), True, WHITE)
        display_surf.blit(display_score, (self.x, self.y))


class Game:

    def __init__(self, ship, chickens, bullets, scoreboard, speed):
        self.ship = ship
        self.chickens = chickens
        self.bullets = bullets
        self.scoreboard = scoreboard
        self.speed = speed

    def draw_arena(self, background):
        display_surf.fill(BLACK)
        self.display_image(background)
        self.ship.draw()
        for chicken in self.chickens:
            chicken.draw()
        for bullet in self.bullets:
            bullet.draw()
        self.scoreboard.display()

    def display_image(self, img):
        img = pygame.transform.scale(img, (width, height))
        display_surf.blit(img, (0, 0))

    def load_sound(self, music, loop, channel):
        pygame.mixer.Channel(channel).play(music, loop)

    def ship_hit_floor(self):
        if self.ship.y >= height - self.ship.height:
            self.ship.y = height - self.ship.height
        elif self.ship.y <= 0:
            self.ship.y = 0
        elif self.ship.x >= width - self.ship.width:
            self.ship.x = width - self.ship.width
        elif self.ship.x <= 0:
            self.ship.x = 0

    def update(self):
        for chicken in self.chickens:
            chicken.move(3)
        for bullet_index, bullet in enumerate(self.bullets):
            bullet.index = bullet_index
            bullet.move(3)
            bullet.check_out_of_range(self.bullets)
            bullet.check_hit_chicken(self.chickens, self.bullets, self.scoreboard)
        self.ship_hit_floor()


def main():
    pygame.init()
    high_score = 0

    background = pygame.image.load(os.path.join('data', 'background.jpg')).convert()
    game_over_img = pygame.image.load(os.path.join('data', 'game_over.png')).convert()
    start = pygame.image.load(os.path.join('data', 'space_invader.png')).convert()
    hit_wall_sound = pygame.mixer.Sound(os.path.join('data', 'hit_wall.wav'))
    game_over_sound = pygame.mixer.Sound(os.path.join('data', 'gameover.wav'))
    start_screen = True
    music = os.path.join('data', 'techno_house_loop.mp3')
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)

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
        chicken_cooldown = 700
        bullet_cooldown = 300
        last_time_chicken = pygame.time.get_ticks()
        last_time_bullet = pygame.time.get_ticks()
        ship = Ship(20, 30, width/2, height/2, 25)
        chickens = []
        bullets = []
        scoreboard = Scoreboard(width - 100, 10, None, 30, 0)
        die = False
        play = True
        game = Game(ship, chickens, bullets, scoreboard, 5)
        a_pressed = False
        d_pressed = False
        w_pressed = False
        s_pressed = False

        while play:
            now = pygame.time.get_ticks()
            if now - last_time_chicken >= chicken_cooldown:
                chicken = Chicken(random.randrange(10, width - 10), 0, 10)
                chickens.append(chicken)
                last_time_chicken = now
            elif now - last_time_bullet >= bullet_cooldown:
                bullet = Bullet(ship.x + ship.width/2, ship.y - 10, 10)
                bullets.append(bullet)
                last_time_bullet = now
            for one in chickens:
                if one.check_hit_floor() or one.check_hit_ship(ship):
                    die = True
                    break

            game.draw_arena(background)
            game.update()
            pygame.display.update()
            fps_clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_a:
                        a_pressed = True
                    elif event.key == K_d:
                        d_pressed = True
                    elif event.key == K_w:
                        w_pressed = True
                    elif event.key == K_s:
                        s_pressed = True
                elif event.type == KEYUP:
                    if event.key == K_a:
                        a_pressed = False
                    elif event.key == K_d:
                        d_pressed = False
                    elif event.key == K_w:
                        w_pressed = False
                    elif event.key == K_s:
                        s_pressed = False
            if a_pressed:
                ship.dir_y = 0
                ship.dir_x = -1
            elif d_pressed:
                ship.dir_y = 0
                ship.dir_x = 1
            elif w_pressed:
                ship.dir_y = -1
                ship.dir_x = 0
            elif s_pressed:
                ship.dir_y = 1
                ship.dir_x = 0
            ship.move()

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
                    game_over = pygame.font.Font(None, 120).render("Your score: " + str(scoreboard.score), True, WHITE)
                    high_score_display = pygame.font.Font(None, 50).render("High score: " + str(high_score), True, WHITE)
                    play_again_display = pygame.font.Font(None, 50).render("Play again?(y/n)", True, WHITE)
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


if __name__ == "__main__":
    main()
