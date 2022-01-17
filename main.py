import pygame
import sys
from random import randrange

size = width, height = 800, 700
black = 0, 0, 0
white = 255, 255, 255

background = pygame.image.load("img/bg.png")


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
    screen = pygame.display.set_mode(size)
    gameover = False
    start_button = Button(200, 200, 300, 50, (203, 190, 181), 0, 'Arial', 40, '          Начало')
    start_button1 = Button(200, 275, 300, 50, (203, 190, 181), 0, 'Arial', 40, ' Крестики-шарики')
    exit_button = Button(200, 350, 300, 50, (203, 190, 181), 0, 'Arial', 40, '          Выход')
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= start_button.x and x <= start_button.x + start_button.width and y >= start_button.y and y <= start_button.y + start_button.height:
                    gameover = True
                    puzzle()
                elif x >= start_button1.x and x <= start_button1.x + start_button1.width and y >= start_button1.y and y <= start_button1.y + start_button1.height:
                    #запуск шариков
                    pass
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
    sq = 800
    cell = 25
    SIZE = [sq, sq]

    x, y = randrange(0, sq, cell), randrange(0, sq, cell)
    apple = randrange(0, sq, cell), randrange(0, sq, cell)
    length = 1
    snake = [(x, y)]
    dx, dy = 0, 0
    fps = 5

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((0, 0, 0))
        [(pygame.draw.rect(screen, (0, 255, 0), (i, j, cell, cell))) for i, j in snake]
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
            apple = randrange(0, sq, cell), randrange(0, sq, cell)
            length += 1

        if x < 0 or x > sq - cell or y < 0 or y > sq - cell:
            menu()
            # gameover
        if len(snake) != len(set(snake)):
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


    continue_button = Button(width - 400, 100, 276, 50, (203, 190, 181), 0, 'Calibri', 50, 'Продолжить')
    restart_button = Button(width - 400, 175, 276, 50, (203, 190, 181), 0, 'Calibri', 50, 'Заново')
    exit_button = Button(width - 400, 250, 276, 50, (203, 190, 181), 0, 'Calibri', 50, 'Выход')

    screen.blit(background, (0, 0))
    continue_button.process_draw(screen)
    restart_button.process_draw(screen)
    exit_button.process_draw(screen)
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= continue_button.x and x <= continue_button.x + continue_button.width and y >= continue_button.y and y <= continue_button.y + continue_button.height:
                    start = True
                if x >= restart_button.x and x <= restart_button.x + restart_button.width and y >= restart_button.y and y <= restart_button.y + restart_button.height:
                    puzzle()
                if x >= exit_button.x and x <= exit_button.x + exit_button.width and y >= exit_button.y and y <= exit_button.y + exit_button.height:
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


if __name__ == '__main__':
    menu()