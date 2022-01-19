import pygame
import sys
from random import randrange

pygame.init()
size = width, height = 800, 700
black = 0, 0, 0
white = 255, 255, 255
background = pygame.image.load("img/bg.png")

pygame.mixer.music.load('img/excuse.ogg')

pygame.mixer.music.play()

sound_vill = pygame.mixer.Sound('img/villager.ogg')

sound_dam = pygame.mixer.Sound('img/damage.ogg')

sound_death = pygame.mixer.Sound('img/level.ogg')

sound_eat = pygame.mixer.Sound('img/eat.ogg')

sound_op = pygame.mixer.Sound('img/open.ogg')


def game1(self):
    if __name__ == '__main__':
        pygame.init()
        pygame.display.set_caption('КРЕСТИКИ-ШАРИКИ')
        size = width, height = 800, 700
        screen = pygame.display.set_mode(size)
        screen.fill((0, 0, 0))



        krest_nol = Krest_nol(3, 3)
        running = True

        while running:

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                Pause2()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    krest_nol.get_click(event.pos)
            krest_nol.render(screen)
            pygame.display.flip()
        pygame.quit()


class Krest_nol:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.krest_nol = [[0] * width for _ in range(height)]
        self.left = 145
        self.top = 90
        self.cell_size = 170
        self.field = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.counter = 1
        self.game_end = 0
        self.who = ''

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size,
                                  self.cell_size), 1)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x > self.width or cell_y < 0 or cell_y > self.height:
            return None
        return cell_x, cell_y

    def on_click(self, cell_coords):
        pause_flag = 1
        screen = pygame.display.set_mode(size)
        print(cell_coords)
        x_x = cell_coords[0] + 1
        y_y = cell_coords[1] + 1



        if self.game_end == 1:
            game1(screen)

        if self.field[y_y - 1][x_x - 1] == '' and self.counter % 2 != 0:
            self.field[y_y - 1][x_x - 1] = 'k'
            print(self.field)

            sound_dam.play()

            pygame.draw.line(screen, (0, 255, 0), (145 + 170*(x_x - 1), 90 + 170*(y_y - 1)), (145+170*(x_x), 90+170*(y_y)), 6)
            pygame.draw.line(screen, (0, 255, 0), (145 + 170*(x_x - 1), 90 + 170*(y_y)), (145+170*(x_x), 90+170*(y_y - 1)), 6)
            self.counter += 1
            '''win'''
            if self.counter >= 6:
                if self.field[0][0] == 'k':
                    if (self.field[0][1] == self.field[0][2] == 'k') or (self.field[1][0] == self.field[2][0] == 'k') or (self.field[1][1] == self.field[2][2] == 'k'):
                        print('WIî11iiiiiiiiiiinnnn')

                        self.game_end = 1
                        self.who = 'k'

                        if self.field[0][1] == self.field[0][2] == 'k':
                            pygame.draw.line(screen, (255, 0, 0), (230, 175), (570, 175), 15)

                        if self.field[1][0] == self.field[2][0] == 'k':
                            pygame.draw.line(screen, (255, 0, 0), (230, 175), (230, 515), 15)

                        if self.field[1][1] == self.field[2][2] == 'k':
                            pygame.draw.line(screen, (255, 0, 0), (230, 175), (570, 515), 15)

                if self.field[2][2] == 'k':
                    if (self.field[2][1] == self.field[2][0] == 'k') or (self.field[0][2] == self.field[1][2] == 'k'):
                        print('WIî11iiiiiiiiiiinnnn')

                        self.game_end = 1
                        self.who = 'k'

                        if self.field[2][1] == self.field[2][0] == 'k':
                            pygame.draw.line(screen, (255, 0, 0), (230, 515), (570, 515), 15)

                        if self.field[0][2] == self.field[1][2] == 'k':
                            pygame.draw.line(screen, (255, 0, 0), (570, 175), (570, 515), 15)

                if self.field[1][1] == 'k':
                    if (self.field[1][0] == self.field[1][2] == 'k') or (self.field[0][1] == self.field[2][1] == 'k'):
                        print('WIî11iiiiiiiiiiinnnn')

                        self.game_end = 1
                        self.who = 'k'

                        if self.field[1][0] == self.field[1][2] == 'k':
                            pygame.draw.line(screen, (255, 0, 0), (230, 345), (570, 345), 15)

                        if self.field[0][1] == self.field[2][1] == 'k':
                            pygame.draw.line(screen, (255, 0, 0), (400, 175), (400, 515), 15)

        if self.field[y_y - 1][x_x - 1] == '' and self.counter % 2 == 0:
            self.field[y_y - 1][x_x - 1] = 'n'
            print(self.field)

            sound_dam.play()

            pygame.draw.circle(screen, (255, 200, 0), (230 + 170*(x_x - 1), 175 + 170*(y_y - 1)), 85)
            self.counter += 1

            if self.counter >= 6:
                if self.field[0][0] == 'n':
                    if (self.field[0][1] == self.field[0][2] == 'n') or (self.field[1][0] == self.field[2][0] == 'n') or (self.field[1][1] == self.field[2][2] == 'n'):
                        print('yoyoyoyoyoyoyoyoyoyoyoy')
                        self.game_end = 1
                        self.who = 'n'

                        if self.field[0][1] == self.field[0][2] == 'n':
                            pygame.draw.line(screen, (255, 125, 0), (230, 175), (570, 175), 15)

                        if self.field[1][0] == self.field[2][0] == 'n':
                            pygame.draw.line(screen, (255, 125, 0), (230, 175), (230, 515), 15)

                        if self.field[1][1] == self.field[2][2] == 'n':
                            pygame.draw.line(screen, (255, 125, 0), (230, 175), (570, 515), 15)

                if self.field[2][2] == 'n':
                    if (self.field[2][1] == self.field[2][0] == 'n') or (self.field[0][2] == self.field[1][2] == 'n'):
                        print('yoyoyoyoyoyoyoyoyoyoyoy')
                        self.game_end = 1
                        self.who = 'n'

                        if self.field[2][1] == self.field[2][0] == 'n':
                            pygame.draw.line(screen, (255, 125, 0), (230, 515), (570, 515), 15)

                        if self.field[0][2] == self.field[1][2] == 'n':
                            pygame.draw.line(screen, (255, 125, 0), (570, 175), (570, 515), 15)

                if self.field[1][1] == 'n':
                    if (self.field[1][0] == self.field[1][2] == 'n') or (self.field[0][1] == self.field[2][1] == 'n'):
                        print('yoyoyoyoyoyoyoyoyoyoyoy')
                        self.game_end = 1
                        self.who = 'n'

                        if self.field[1][0] == self.field[1][2] == 'n':
                            pygame.draw.line(screen, (255, 125, 0), (230, 345), (570, 345), 15)

                        if self.field[0][1] == self.field[2][1] == 'n':
                            pygame.draw.line(screen, (255, 125, 0), (400, 175), (400, 515), 15)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


class Button:
    def __init__(self, x=None, y=None, w=None, h=None, color = (0, 0, 0), border = 0, font = 'Arial', text_size = 40, text = None):
        self.color = color
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.font = font
        self.text_size = text_size
        self.text = text
        self.border = border

    def process_draw(self, screen):
        pygame.font.init()
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), self.border)
        font = pygame.font.SysFont(self.font, self.text_size, True)
        data = self.text
        ts = font.render(data, False, black)
        screen.blit(ts, (self.x - 1, self.y))


def menu():
    pygame.init()
    pause_flag = 0
    pygame.display.set_caption('МЕНЮ')
    screen = pygame.display.set_mode(size)
    gameover = False
    start_button = Button(200, 200, 370, 50, (203, 190, 181), 0, 'Arial', 40, '       Червячок')
    start_button1 = Button(200, 275, 370, 50, (203, 190, 181), 0, 'Arial', 40, ' Крестики-шарики')
    exit_button = Button(200, 350, 370, 50, (203, 190, 181), 0, 'Arial', 40, '          Выход')
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= start_button.x and x <= start_button.x + start_button.width and y >= start_button.y and y <= start_button.y + start_button.height:
                    gameover = True
                    pygame.mixer.music.stop()
                    sound_op.play()
                    pygame.mixer.music.load('img/puz.mp3')

                    pygame.mixer.music.play()
                    puzzle()
                elif x >= start_button1.x and x <= start_button1.x + start_button1.width and y >= start_button1.y and y <= start_button1.y + start_button1.height:
                    pygame.mixer.music.stop()
                    sound_op.play()
                    pygame.mixer.music.load('img/mus.ogg')

                    pygame.mixer.music.play()
                    game1(screen)

                elif x >= exit_button.x and x <= exit_button.x + exit_button.width and y >= exit_button.y and y <= exit_button.y + exit_button.height:
                    exit()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if x >= start_button.x and x <= start_button.x + start_button.width and y >= start_button.y and y <= start_button.y + start_button.height:
                    start_button.border = 5
                    start_button.process_draw(screen)
                elif x >= start_button1.x and x <= start_button1.x + start_button1.width and y >= start_button1.y and y <= start_button1.y + start_button1.height:
                    start_button1.border = 5
                    start_button1.process_draw(screen)
                elif x >= exit_button.x and x <= exit_button.x + exit_button.width and y >= exit_button.y and y <= exit_button.y + exit_button.height:
                    exit_button.border = 5
                    exit_button.process_draw(screen)
                else:
                    start_button.border = 0
                    start_button.process_draw(screen)
                    start_button1.border = 0
                    start_button1.process_draw(screen)
                    exit_button.border = 0
                    exit_button.process_draw(screen)
            if event.type == pygame.QUIT:
                gameover = True
            screen.fill(white)
            screen.blit(background, (0, 0))
            start_button.process_draw(screen)
            start_button1.process_draw(screen)
            exit_button.process_draw(screen)
            pygame.display.flip()
            pygame.time.wait(10)
    sys.exit()

def puzzle():
    pause_flag = 0
    cell = 25
    SIZE = [800, 700]

    x, y = randrange(0, 800, cell), randrange(0, 700, cell)
    apple = randrange(0, 800, cell), randrange(0, 700, cell)
    length = 1
    snake = [(x, y)]
    dx, dy = 0, 0
    fps = 15

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (10, 200, 55), (10, 10, 780, 680))
        [(pygame.draw.rect(screen, (255, 125, 125), (i, j, cell, cell))) for i, j in snake]
        pygame.draw.rect(screen, (255, 0, 0), (*apple, cell, cell))

        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            dx, dy = 0, -1
        if key[pygame.K_a]:
            dx, dy = -1, 0
        if key[pygame.K_s]:
            dx, dy = 0, 1
        if key[pygame.K_d]:
            dx, dy = 1, 0
        if key[pygame.K_SPACE]:
            Pause()
        #баг после отжатия паузы нет яблок

        x += dx * cell
        y += dy * cell
        snake.append((x, y))
        snake = snake[-length:]

        if snake[-1] == apple:
            apple = randrange(0, 800, cell), randrange(0, 700, cell)
            length += 1
            sound_eat.play()

        if x < 0 or x > 800 - cell or y < 0 or y > 700 - cell:
            sound_death.play()
            pygame.mixer.music.load('img/excuse.ogg')

            pygame.mixer.music.play()
            menu()
            # gameover
        if len(snake) != len(set(snake)):
            sound_death.play()
            pygame.mixer.music.load('img/excuse.ogg')

            pygame.mixer.music.play()
            menu()
            # gameover

        pygame.display.flip()
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    pygame.quit()



def Pause():
    pygame.init()
    screen = pygame.display.set_mode(size)
    start = False


    continue_button = Button(width - 400, 100, 320, 50, (203, 190, 181), 0, 'Calibri', 50, 'Продолжить')
    restart_button = Button(width - 400, 175, 320, 50, (203, 190, 181), 0, 'Calibri', 50, 'Заново')
    exit_button = Button(width - 400, 250, 320, 50, (203, 190, 181), 0, 'Calibri', 50, 'Выход')

    screen.blit(background, (0, 0))
    continue_button.process_draw(screen)
    restart_button.process_draw(screen)
    exit_button.process_draw(screen)
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= continue_button.x and x <= continue_button.x + continue_button.width and y >= continue_button.y and y <= continue_button.y + continue_button.height:
                    sound_op.play()
                    start = True
                if x >= restart_button.x and x <= restart_button.x + restart_button.width and y >= restart_button.y and y <= restart_button.y + restart_button.height:
                    sound_op.play()
                    puzzle()
                if x >= exit_button.x and x <= exit_button.x + exit_button.width and y >= exit_button.y and y <= exit_button.y + exit_button.height:
                    sound_op.play()
                    pygame.mixer.music.load('img/excuse.ogg')

                    pygame.mixer.music.play()
                    menu()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if x >= continue_button.x and x <= continue_button.x + continue_button.width and y >= continue_button.y and y <= continue_button.y + continue_button.height:
                    continue_button.border = 5
                    continue_button.color = (255, 255, 255)
                    continue_button.process_draw(screen)
                elif x >= restart_button.x and x <= restart_button.x + restart_button.width and y >= restart_button.y and y <= restart_button.y + restart_button.height:
                    restart_button.border = 5
                    restart_button.color = (255, 255, 255)
                    restart_button.process_draw(screen)
                elif x >= exit_button.x and x <= exit_button.x + exit_button.width and y >= exit_button.y and y <= exit_button.y + exit_button.height:
                    exit_button.border = 5
                    exit_button.color = (255, 255, 255)
                    exit_button.process_draw(screen)
                else:
                    continue_button.border = 0
                    continue_button.color = (203,190,181)
                    continue_button.process_draw(screen)
                    restart_button.border = 0
                    restart_button.color = (203,190,181)
                    restart_button.process_draw(screen)
                    exit_button.border = 0
                    exit_button.color = (203,190,181)
                    exit_button.process_draw(screen)


            if event.type == pygame.QUIT:
                sys.exit()

            pygame.display.flip()

def Pause2():
    pygame.init()
    screen = pygame.display.set_mode(size)
    start = False

    restart_button = Button(width - 400, 175, 276, 50, (203, 190, 181), 0, 'Calibri', 50, 'Заново')
    exit_button = Button(width - 400, 250, 276, 50, (203, 190, 181), 0, 'Calibri', 50, 'Выход')

    screen.blit(background, (0, 0))
    restart_button.process_draw(screen)
    exit_button.process_draw(screen)
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= restart_button.x and x <= restart_button.x + restart_button.width and y >= restart_button.y and y <= restart_button.y + restart_button.height:
                    sound_op.play()
                    pygame.mixer.music.load('img/mus.ogg')

                    pygame.mixer.music.play()
                    game1(screen)
                if x >= exit_button.x and x <= exit_button.x + exit_button.width and y >= exit_button.y and y <= exit_button.y + exit_button.height:
                    pygame.mixer.music.stop()
                    sound_op.play()
                    pygame.mixer.music.load('img/excuse.ogg')

                    pygame.mixer.music.play()
                    menu()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if x >= restart_button.x and x <= restart_button.x + restart_button.width and y >= restart_button.y and y <= restart_button.y + restart_button.height:
                    restart_button.border = 5
                    restart_button.color = (255, 255, 255)
                    restart_button.process_draw(screen)
                elif x >= exit_button.x and x <= exit_button.x + exit_button.width and y >= exit_button.y and y <= exit_button.y + exit_button.height:
                    exit_button.border = 5
                    exit_button.color = (255, 255, 255)
                    exit_button.process_draw(screen)
                else:

                    restart_button.border = 0
                    restart_button.color = (203,190,181)
                    restart_button.process_draw(screen)
                    exit_button.border = 0
                    exit_button.color = (203,190,181)
                    exit_button.process_draw(screen)


            if event.type == pygame.QUIT:
                sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    menu()
