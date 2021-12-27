import pygame
import sys
import random

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
    start_button = Button(200, 200, 150, 50, (255, 0, 0), 0, 'Arial', 40, '  start')
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= start_button.x and x <= start_button.x + start_button.width and y >= start_button.y and y <= start_button.y + start_button.height:
                    gameover = True
                    #вызов игры
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







if __name__ == '__main__':
    menu()