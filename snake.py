import pygame
from pygame.locals import *
from random import randrange


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Snake the game')
    background = pygame.Surface(screen.get_size())
    clock = pygame.time.Clock()
    cell_size = 20
    green_tail = (0, 200, 0)
    green_head = (0, 120, 0)
    red_apple = (200, 0, 0)
    start_pos_x, start_pos_y = 300, 300  # center of game map
    x1, y1 = 0, 0
    direction = ['']
    food_x = round(randrange(0, 600 - cell_size) / 20.0) * 20.0
    food_y = round(randrange(0, 600 - cell_size) / 20.0) * 20.0
    snake_cells_pos = []
    snake_len = 1
    key_press_check = False
    font_style = pygame.font.SysFont('', 50)
    red = (225, 0, 0)
    checking = True
    frame = 0
    independence = 9

    def our_snake(snake_list):
        for cell1 in snake_list:
            if cell1 == snake_list[-1]:
                pygame.draw.rect(screen, green_head, [cell1[0], cell1[1], cell_size, cell_size])
            else:
                pygame.draw.rect(screen, green_tail, [cell1[0], cell1[1], cell_size, cell_size])

    def message(msg, colour):
        text = font_style.render(msg, True, colour)
        screen.blit(text, [600 / 2.75, 600 / 2.5])

    while 1:
        if not checking:
            screen.fill((255, 255, 255))
            screen.blit(background, (0, 0))
            message("You Lost!", red)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                if pygame.key.get_pressed()[pygame.K_r]:
                    main()
                    return
            pygame.display.flip()  # draw all on display
            clock.tick(60)
        else:
            check_pos = True
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                if event.type == KEYDOWN and not key_press_check:
                    if pygame.key.get_pressed()[pygame.K_RIGHT] and direction[0] != 'left':
                        x1 = 20
                        y1 = 0
                        direction[0] = 'right'
                        key_press_check = True
                    elif pygame.key.get_pressed()[pygame.K_LEFT] and direction[0] != 'right':
                        x1 = -20
                        y1 = 0
                        direction[0] = 'left'
                        key_press_check = True
                    elif pygame.key.get_pressed()[pygame.K_UP] and direction[0] != 'down':
                        x1 = 0
                        y1 = -20
                        direction[0] = 'up'
                        key_press_check = True
                    elif pygame.key.get_pressed()[pygame.K_DOWN] and direction[0] != 'up':
                        x1 = 0
                        y1 = 20
                        direction[0] = 'down'
                        key_press_check = True
            if frame % independence == 0:
                start_pos_x += x1
                start_pos_y += y1
            if start_pos_x >= 600:
                start_pos_x = 0
            elif start_pos_x < 0:
                start_pos_x = 580
            elif start_pos_y < 0:
                start_pos_y = 580
            elif start_pos_y >= 600:
                start_pos_y = 0
            background.fill((250, 250, 250))
            if frame % independence == 0:
                screen.blit(background, (0, 0))
            pygame.draw.rect(screen, red_apple, [food_x, food_y, cell_size, cell_size])
            snake_head = [start_pos_x, start_pos_y]
            if frame % independence == 0:
                snake_cells_pos.append(snake_head)
            if len(snake_cells_pos) > snake_len:
                del snake_cells_pos[0]
            for cell in snake_cells_pos[:-1]:
                if cell == snake_head:
                    checking = False
            if start_pos_x == food_x and start_pos_y == food_y:
                while check_pos:  # while apple pos not in snake body
                    check_all_cells = 0
                    for cell in snake_cells_pos:
                        if cell[0] == food_x and cell[1] == food_y:
                            food_x = round(randrange(0, 600 - cell_size) / 20.0) * 20.0
                            food_y = round(randrange(0, 600 - cell_size) / 20.0) * 20.0
                        else:
                            check_all_cells += 1
                    if check_all_cells == snake_len:
                        check_pos = False
                snake_len += 1
            if frame % independence == 0:
                our_snake(snake_cells_pos)
                key_press_check = False
                frame = 0
            for cell in range(0, 31):
                pygame.draw.line(screen, (0, 0, 0), [cell_size * cell, 0], [cell_size * cell, 600])
                pygame.draw.line(screen, (0, 0, 0), [0, cell_size * cell], [600, cell_size * cell])
            pygame.display.flip()  # draw all on display
            frame += 1
            clock.tick(60)  # frame rate


if __name__ == '__main__':
    main()
