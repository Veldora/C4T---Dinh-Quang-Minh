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
icon_surf = pygame.image.load(os.path.join('data', 'icon.png'))
display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Shooter")
pygame.display.set_icon(icon_surf)

fps_clock = pygame.time.Clock()


class Chicken:

    def __init__(self, x, y, radius, speed):
        self.x = int(x)
        self.y = int(y)
        self.radius = int(radius)
        self.speed = speed

    def draw(self, game, img):
        game.display_image(img, self.x - self.radius - 1, self.y - self.radius - 1, 2 * self.radius + 1, 2 * self.radius + 1)

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

    def move(self):
        self.y += self.speed


class Bullet:

    def __init__(self, x, y, radius, speed):
        self.x = int(x)
        self.y = int(y)
        self.index = 0
        self.radius = int(radius)
        self.speed = speed
        self.explosion = False
        self.explosion_time = 0

    def draw(self, game, img, explosion_img):
        if self.explosion:
            game.display_image(explosion_img, self.x - self.radius - 10, self.y - self.radius - 10, 40, 40)
        else:
            game.display_image(img, self.x - self.radius - 16, self.y - self.radius - 7, 53, 40)

    def check_hit_chicken(self, chickens, scoreboard, game, music):
        for chicken_index, chicken in enumerate(chickens):
            if chicken.x + self.radius + chicken.radius >= self.x >= chicken.x - self.radius - chicken.radius \
                    and chicken.y + self.radius + chicken.radius >= self.y >= chicken.y - self.radius - chicken.radius:
                scoreboard.score += 10
                game.load_sound(music, 0, 2)
                self.explosion = True
                self.explosion_time = pygame.time.get_ticks()
                chickens.pop(chicken_index)

    def check_out_of_range(self, bullets):
        if self.y <= 0:
            bullets.pop(self.index)

    def move(self, bullets):
        if not self.explosion:
            self.y -= self.speed
        else:
            now = pygame.time.get_ticks()
            if now - self.explosion_time >= 400:
                bullets.pop(self.index)


class Ship:

    def __init__(self, w, h, x, y):
        self.width = int(w)
        self.height = int(h)
        self.x = int(x)
        self.y = int(y)

    def draw(self, game, img):
        game.display_image(img, self.x - 15, self.y - 13, 50, 64)

    def move(self, pos):
        self.x = pos[0] - self.width/2
        self.y = pos[1] - self.height/2


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

    def draw_arena(self, background, bullet_img, chicken_img, ship_img, explosion_img):
        display_surf.fill(BLACK)
        self.display_image(background, 0, 0, width, height)
        self.ship.draw(self, ship_img)
        for chicken in self.chickens:
            chicken.draw(self, chicken_img)
        for bullet in self.bullets:
            bullet.draw(self, bullet_img, explosion_img)
        self.scoreboard.display()

    def display_image(self, img, x, y, w, h):
        img = pygame.transform.scale(img, (w, h))
        display_surf.blit(img, (x, y))

    def load_sound(self, music, loop, channel):
        pygame.mixer.Channel(channel).play(music, loop)

    def ship_hit_floor(self, music, check_hit):
        if self.ship.y > height - self.ship.height:
            self.ship.y = height - self.ship.height
            if check_hit:
                self.load_sound(music, 0, 1)
                check_hit = False
        elif self.ship.y < 0:
            self.ship.y = 0
            if check_hit:
                self.load_sound(music, 0, 1)
                check_hit = False
        elif self.ship.x > width - self.ship.width:
            self.ship.x = width - self.ship.width
            if check_hit:
                self.load_sound(music, 0, 1)
                check_hit = False
        elif self.ship.x < 0:
            self.ship.x = 0
            if check_hit:
                self.load_sound(music, 0, 1)
                check_hit = False
        else:
            check_hit = True
        return check_hit

    def update(self, pos, music, hit_wall_sound, check_hit):
        for chicken in self.chickens:
            chicken.move()
        for bullet_index, bullet in enumerate(self.bullets):
            bullet.index = bullet_index
            bullet.move(self.bullets)
            bullet.check_out_of_range(self.bullets)
            bullet.check_hit_chicken(self.chickens, self.scoreboard, self, music)
        check_hit = self.ship_hit_floor(hit_wall_sound, check_hit)
        self.ship.move(pos)
        return check_hit


def main():
    global mouse_pos
    pygame.init()
    high_score = 0
    start_screen = True

    # load anh va am thanh
    background = pygame.image.load(os.path.join('data', 'background.jpg')).convert()
    score_display = pygame.image.load(os.path.join('data', 'lose.jpg')).convert()
    bullet_img = pygame.image.load(os.path.join('data', 'mine-bullet.png')).convert_alpha()
    chicken_img = pygame.image.load(os.path.join('data', 'chicken.png')).convert_alpha()
    ship_img = pygame.image.load(os.path.join('data', 'spaceship.png')).convert_alpha()
    bullet_explosion = pygame.image.load(os.path.join('data', 'explosion1.gif')).convert_alpha()
    game_over_img = pygame.image.load(os.path.join('data', 'game_over.png')).convert()
    start = pygame.image.load(os.path.join('data', 'space_invader.png')).convert()
    hit_wall_sound = pygame.mixer.Sound(os.path.join('data', 'hit_wall.wav'))
    boom_sound = pygame.mixer.Sound(os.path.join('data', 'boom.wav'))
    game_over_sound = pygame.mixer.Sound(os.path.join('data', 'gameover.wav'))
    music = os.path.join('data', 'techno_house_loop.mp3')
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)

    # man hinh mo dau game
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

    # game
    while True:
        fps = 20
        time_speed = 1
        chicken_cooldown = 900
        bullet_cooldown = 800
        check_fps = True
        check_last_time = True
        check_hit = True
        last_time_chicken = pygame.time.get_ticks()
        last_time_bullet = pygame.time.get_ticks()
        ship = Ship(20, 44, width/2, height/2)
        chickens = []
        bullets = []
        scoreboard = Scoreboard(width - 200, 30, None, 40, 0)
        die = False
        play = True
        game = Game(ship, chickens, bullets, scoreboard, 5)
        mouse_pos = [width/2, height/2]

        while play:
            # tao object chicken va bullet sau mot khoang thoi gian nhat dinh
            now = pygame.time.get_ticks()
            if now - last_time_chicken >= chicken_cooldown:
                chicken = Chicken(random.randrange(10, width - 10), 0, 15, time_speed)
                chickens.append(chicken)
                last_time_chicken = now
            elif now - last_time_bullet >= bullet_cooldown:
                bullet = Bullet(ship.x + ship.width/2, ship.y - 10, 10, time_speed)
                bullets.append(bullet)
                last_time_bullet = now
            for one in chickens:
                if one.check_hit_floor() or one.check_hit_ship(ship):
                    die = True
                    break

            # xu ly su kien
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()

            # tang speed va giam thoi gian tao object
            if scoreboard.score != 0 and check_fps:
                if scoreboard.score % 1000 == 0:
                    time_speed += 1
                    check_fps = False
                elif scoreboard.score % 100 == 0:
                    fps += 2
                    check_fps = False
            elif scoreboard.score % 100 != 0:
                check_fps = True
            if bullet_cooldown > 100:
                if scoreboard.score % 170 == 0 and check_last_time:
                    bullet_cooldown -= 50
                    chicken_cooldown -= 50
                    check_last_time = False
                elif scoreboard.score % 170 != 0:
                    check_last_time = True

            # cap nhat khung hinh
            game.draw_arena(background, bullet_img, chicken_img, ship_img, bullet_explosion)
            check_hit = game.update(mouse_pos, boom_sound, hit_wall_sound, check_hit)
            pygame.display.update()
            fps_clock.tick(fps)

            # game over
            if die:
                # check high score
                if scoreboard.score > high_score:
                    high_score = scoreboard.score
                game.load_sound(game_over_sound, 0, 0)
                display_surf.fill(BLACK)

                # hien thi man hinh game over
                for i in range(150):
                    game.display_image(game_over_img, 0, 0, width, height)
                    pygame.display.update()

                # hien thi man hinh play again
                display_surf.fill(BLACK)
                play_again = True
                while play_again:

                    # hien thi score va high score
                    game.display_image(score_display, 0, 0, width, height)
                    game_over = pygame.font.Font(None, 120).render("Your score: " + str(scoreboard.score), True, WHITE)
                    high_score_display = pygame.font.Font(None, 50).render("High score: " + str(high_score), True, WHITE)
                    play_again_display = pygame.font.Font(None, 50).render("Play again?(y/n)", True, WHITE)
                    display_surf.blit(game_over, ((width - game_over.get_width()) // 2, (height - game_over.get_height()) // 2 - 220))
                    display_surf.blit(high_score_display, ((width - high_score_display.get_width()) // 2, (height - game_over.get_height()) // 2 - 110))
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
