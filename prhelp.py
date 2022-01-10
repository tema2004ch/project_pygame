import pygame
import sys
import random

size = width, height = 800, 700
black = 0, 0, 0
white = 255, 255, 255
a = 3
b = 3

background = pygame.image.load("img/bg.png")
kr = pygame.image.load("img/krestik.png")
nol = pygame.image.load("img/nolik.png")

rect = kr.get_rect()


def game1(self):
    if __name__ == '__main__':
        pygame.init()
        pygame.display.set_caption('snich')
        size = width, height = 800, 700
        screen = pygame.display.set_mode(size)
        screen.fill((0, 0, 0))

        krest_nol = Krest_nol(a, b)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    krest_nol.get_click(event.pos)
            krest_nol.render(screen)
            pygame.display.flip()
        pygame.quit()


class Button:
    def __init__(self, x=None, y=None, w=None, h=None, color=(0, 0, 0), border=0, font='Arial', text_size=40, text=None):
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
    start_button = Button(200, 200, 150, 50, (255, 0, 0), 0, 'Arial', 40, '  start')
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= start_button.x and x <= start_button.x + start_button.width and y >= start_button.y and y <= start_button.y + start_button.height:
                    gameover = True
                    game1(screen)
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if x >= start_button.x and x <= start_button.x + start_button.width and y >= start_button.y and y <= start_button.y + start_button.height:
                    start_button.border = 5
                    start_button.process_draw(screen)
                else:
                    start_button.border = 0
                    start_button.process_draw(screen)
            if event.type == pygame.QUIT:
                gameover = True
            screen.fill(white)
            screen.blit(background, (0, 0))
            start_button.process_draw(screen)
            pygame.display.flip()
            pygame.time.wait(10)
    sys.exit()


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
        screen = pygame.display.set_mode(size)
        # pygame.draw.rect(screen, (255, 0, 0), (cell_coords[0], cell_coords[1], 100, 100))
        # pygame.display.update()
        print(cell_coords)
        x_x = cell_coords[0] + 1
        y_y = cell_coords[1] + 1

        if self.field[y_y - 1][x_x - 1] == '' and self.counter % 2 != 0:
            self.field[y_y - 1][x_x - 1] = 'k'
            print(self.field)
            pygame.draw.line(screen, (0, 255, 0), (145 + 170*(x_x - 1), 90 + 170*(y_y - 1)), (145+170*(x_x), 90+170*(y_y)), 6)
            pygame.draw.line(screen, (0, 255, 0), (145 + 170*(x_x - 1), 90 + 170*(y_y)), (145+170*(x_x), 90+170*(y_y - 1)), 6)
            self.counter += 1

        if self.field[y_y - 1][x_x - 1] == '' and self.counter % 2 == 0:
            self.field[y_y - 1][x_x - 1] = 'n'
            print(self.field)
            pygame.draw.circle(screen, (255, 200, 0), (230 + 170*(x_x - 1), 175 + 170*(y_y - 1)), 85)
            self.counter += 1

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


if __name__ == '__main__':
    menu()
