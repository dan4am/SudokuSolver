import pygame
import os
import time
import sys
sys.path.append("..")
from src.solver import *
from gui.util import *

######################
# Define some colors #
######################

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (220, 220, 220)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



######################
# Define some sizes  #
######################

frame_width = 450
frame_height = 450
frame_up_left_corner = [75,75]



######################
# States             #
######################

done = False
Current_state = 1 #menu = 0, game = 1, gameover=2, gukenyura = 3, waiting from menu = 5, waiting from set board = 6
MENU = 0
PLAY = 1
REPLAY = 2
HELP = 3


selected_case=[-1,-1]

pygame.init()
size = (600,600)
screen = pygame.display.set_mode(size)



def screen_coordinates_to_board_coordinates(x,y):
    new_x = x - frame_up_left_corner[0]
    new_y = y - frame_up_left_corner[1]
    line = int (new_y/50) + 1
    column = int(new_x/50) + 1

    return [line, column]



def game_coordinates_to_data(x, y):
    result =[0,0]
    if(Current_state == MENU):
        pass

    elif(Current_state == PLAY):
        if (x >= frame_up_left_corner[0] and x <= frame_up_left_corner[0] + frame_width ) and \
                (y >= frame_up_left_corner[1] and y <= frame_up_left_corner[1]+frame_height):
            result = screen_coordinates_to_board_coordinates(x,y)
            return[1, result[0], result[1]]

        else:
            return [0,0,0]
    else :
        return [0,0,0]


def draw_frame():
    # pygame.draw.line(screen, BLACK, [100, 100], [500, 100], 1)
    # pygame.draw.line(screen, BLACK, [100, 100], [100, 500], 1)
    # pygame.draw.line(screen, BLACK, [100, 500], [500, 500], 1)
    # pygame.draw.line(screen, BLACK, [100, 100], [100, 500], 1)
    screen.fill(WHITE)

    #top horizontal line
    pygame.draw.line(screen, BLACK, [frame_up_left_corner[0], frame_up_left_corner[1]],
                     [frame_up_left_corner[0]+frame_width, frame_up_left_corner[1]],3)
    #bottom horizontal line
    pygame.draw.line(screen, BLACK,  [frame_up_left_corner[0], frame_up_left_corner[1]+frame_height],
                     [frame_up_left_corner[0]+frame_width, frame_up_left_corner[1]+frame_height], 3)

    #left vertical line
    pygame.draw.line(screen, BLACK, [frame_up_left_corner[0], frame_up_left_corner[1]],
                     [frame_up_left_corner[0], frame_up_left_corner[1]+frame_height], 3)

    #rignt vertical line
    pygame.draw.line(screen, BLACK, [frame_up_left_corner[0]+frame_width, frame_up_left_corner[1]],
                     [frame_up_left_corner[0]+frame_width, frame_up_left_corner[1]+frame_height], 3)

    # other horizontal lines
    for line in range (1,9):
        if line == 3 or line == 6 :
            pygame.draw.line(screen, BLACK, [frame_up_left_corner[0], frame_up_left_corner[1] + 50 * line],
                             [frame_up_left_corner[0] + frame_width, frame_up_left_corner[1] + 50 * line], 3)
        else:
            pygame.draw.line(screen, BLACK, [frame_up_left_corner[0], frame_up_left_corner[1] + 50 * line],
                             [frame_up_left_corner[0] + frame_width, frame_up_left_corner[1] + 50 * line], 1)

    # other vertical lines
    for column in range(1, 9):
        if column == 3 or column == 6:
            pygame.draw.line(screen, BLACK, [frame_up_left_corner[0]+50*column, frame_up_left_corner[1]],
                             [frame_up_left_corner[0]+50*column, frame_up_left_corner[1] + frame_height], 3)
        else:
            pygame.draw.line(screen, BLACK, [frame_up_left_corner[0] + 50 * column, frame_up_left_corner[1]],
                             [frame_up_left_corner[0] + 50 * column, frame_up_left_corner[1] + frame_height], 1)

    #fill the board
    font_obj = pygame.font.Font("../assets/fonts/ARLRDBD.TTF", 25)
    for line in range (9):

        for column in range (9):
            if(test[line][column] != 0):
                # if(not (line == selected_case[0] -1 and column == selected_case[1] -1)):
                    text_surface_obj = font_obj.render(str(test[line][column]), True, BLACK)
                    text_rect_obj = text_surface_obj.get_rect()
                    x = column * 50 + 25 + frame_up_left_corner[0]
                    y = line * 50 + 25 + frame_up_left_corner[1]
                    text_rect_obj.center = (x, y)
                    text_rect_obj.height = 50
                    text_rect_obj.width = 50
                    screen.blit(text_surface_obj, text_rect_obj)

            if ( (line == selected_case[0] - 1 and column == selected_case[1] - 1)):

                x = column * 50 + 25 + frame_up_left_corner[0]
                y = line * 50 + 25 + frame_up_left_corner[1]
                pygame.draw.line(screen, BLACK, [x -25, y],
                                 [x+25,y], 49)
                if test[line][column] != 0 :
                    text_surface_obj = font_obj.render(str(test[line][column]), True, WHITE)
                text_rect_obj = text_surface_obj.get_rect()
                text_rect_obj.center = (x, y)
                text_rect_obj.height = 50
                text_rect_obj.width = 50
                screen.blit(text_surface_obj, text_rect_obj)







def main():
    global selected_case
    done = False
    clock = pygame.time.Clock()
    moves = 0
    screen.fill(WHITE)
    draw_frame()
    while (not done):
        draw_frame()
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    data = game_coordinates_to_data(position[0], position[1])

                    selected_case = [data[1],data[2]]
                    print (selected_case)


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pass
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
