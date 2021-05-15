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
#     Buttons        #
######################


help_mode_button=[610,265]
help_mode_banner=[563,75]


######################
# Define some sizes  #
######################

frame_width = 450
frame_height = 450
frame_up_left_corner = [75,75]

######################
#       States       #
######################

done = False
current_state = 1 #menu = 0, game = 1, gameover=2, gukenyura = 3, waiting from menu = 5, waiting from set board = 6
MENU = 0
PLAY = 1
HELP_MODE = 2
HELP = 3


selected_case=[-1,-1]

pygame.init()
size = (900,600)
screen = pygame.display.set_mode(size)



def screen_coordinates_to_board_coordinates(x,y):
    new_x = x - frame_up_left_corner[0]
    new_y = y - frame_up_left_corner[1]
    line = int (new_y/50) + 1
    column = int(new_x/50) + 1

    return [line, column]



def game_coordinates_to_data(x, y):
    global current_state
    result =[0,0]
    if(current_state == MENU):
        print ("nothing")

    elif(current_state == PLAY):
        if (x >= frame_up_left_corner[0] and x <= frame_up_left_corner[0] + frame_width ) and \
                (y >= frame_up_left_corner[1] and y <= frame_up_left_corner[1]+frame_height):
            result = screen_coordinates_to_board_coordinates(x,y)
            return[1, result[0], result[1]]
        elif (x >= help_mode_button[0] and x <= help_mode_button[0] + 205 and
                y >= help_mode_button[1] and y <= help_mode_button[1] + 70):
            return[2, 0, 0]

        else:
            return [1,0,0]

    elif(current_state == HELP_MODE):
        if (x >= frame_up_left_corner[0] and x <= frame_up_left_corner[0] + frame_width ) and \
                (y >= frame_up_left_corner[1] and y <= frame_up_left_corner[1]+frame_height):
            result = screen_coordinates_to_board_coordinates(x,y)
            return[3, result[0], result[1]]

        else:
            return [2,0,0]
    else :
        return [-1,0,0]

def key_selection(test, event,selected_case):
    global current_state
    if event.key == pygame.K_RIGHT:
        pass
    elif event.key == pygame.K_KP1:
        test[selected_case[0] - 1][selected_case[1] - 1] = 1
    elif event.key == pygame.K_KP2:
        test[selected_case[0] - 1][selected_case[1] - 1] = 2
    elif event.key == pygame.K_KP3:
        test[selected_case[0] - 1][selected_case[1] - 1] = 3
    elif event.key == pygame.K_KP4:
        test[selected_case[0] - 1][selected_case[1] - 1] = 4
    elif event.key == pygame.K_KP5:
        test[selected_case[0] - 1][selected_case[1] - 1] = 5
    elif event.key == pygame.K_KP6:
        test[selected_case[0] - 1][selected_case[1] - 1] = 6
    elif event.key == pygame.K_KP7:
        test[selected_case[0] - 1][selected_case[1] - 1] = 7
    elif event.key == pygame.K_KP8:
        test[selected_case[0] - 1][selected_case[1] - 1] = 8
    elif event.key == pygame.K_KP9:
        test[selected_case[0] - 1][selected_case[1] - 1] = 9
    elif event.key == pygame.K_KP0:
        test[selected_case[0] - 1][selected_case[1] - 1] = 0
    elif event.key == pygame.K_1:
        test[selected_case[0] - 1][selected_case[1] - 1] = 1
    elif event.key == pygame.K_2:
        test[selected_case[0] - 1][selected_case[1] - 1] = 2
    elif event.key == pygame.K_3:
        test[selected_case[0] - 1][selected_case[1] - 1] = 3
    elif event.key == pygame.K_4:
        test[selected_case[0] - 1][selected_case[1] - 1] = 4
    elif event.key == pygame.K_5:
        test[selected_case[0] - 1][selected_case[1] - 1] = 5
    elif event.key == pygame.K_6:
        test[selected_case[0] - 1][selected_case[1] - 1] = 6
    elif event.key == pygame.K_7:
        test[selected_case[0] - 1][selected_case[1] - 1] = 7
    elif event.key == pygame.K_8:
        test[selected_case[0] - 1][selected_case[1] - 1] = 8
    elif event.key == pygame.K_9:
        test[selected_case[0] - 1][selected_case[1] - 1] = 9
    elif event.key == pygame.K_0:
        test[selected_case[0] - 1][selected_case[1] - 1] = 0
    elif event.key == pygame.K_ESCAPE:
        test[selected_case[0] - 1][selected_case[1] - 1] = 0
    elif event.key == pygame.K_g:
        current_state = HELP_MODE




def draw_frame(help_button = None):
    global size, help_mode_button
    # pygame.draw.line(screen, BLACK, [100, 100], [500, 100], 1)
    # pygame.draw.line(screen, BLACK, [100, 100], [100, 500], 1)
    # pygame.draw.line(screen, BLACK, [100, 500], [500, 500], 1)
    # pygame.draw.line(screen, BLACK, [100, 100], [100, 500], 1)
    screen.fill(WHITE)
    #help_mode button

    if(current_state == PLAY):

        if(help_button):
            pygame.draw.rect(screen, BLACK, pygame.Rect(help_mode_button[0], help_mode_button[1], 205, 70))
            font_obj = pygame.font.Font("../assets/fonts/ARLRDBD.TTF", 32)
            text_surface_obj = font_obj.render("help mode", True, WHITE)
            text_rect_obj = text_surface_obj.get_rect()
            text_rect_obj.center = (help_mode_button[0] + 102, help_mode_button[1] + 35)
            screen.blit(text_surface_obj, text_rect_obj)

        else:
            pygame.draw.rect(screen, BLACK, pygame.Rect(help_mode_button[0], help_mode_button[1], 205, 70),2)
            font_obj = pygame.font.Font("../assets/fonts/ARLRDBD.TTF", 32)
            text_surface_obj = font_obj.render("help mode", True, BLACK)
            text_rect_obj = text_surface_obj.get_rect()
            text_rect_obj.center = (help_mode_button[0] + 102, help_mode_button[1] + 35)
            screen.blit(text_surface_obj, text_rect_obj)



    elif (current_state == HELP_MODE):

        #draw the banner of help mode
        pygame.draw.rect(screen, BLACK, pygame.Rect(help_mode_banner[0], help_mode_banner[1], 299, 30), 2)
        font_obj = pygame.font.Font("../assets/fonts/ARLRDBD.TTF", 30)
        text_surface_obj = font_obj.render("help mode", True, BLACK)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (help_mode_banner[0] + 150, help_mode_banner[1] + 14)
        screen.blit(text_surface_obj, text_rect_obj)

        #draw the possibiities.




    # top horizontal line
    pygame.draw.line(screen, BLACK, [frame_up_left_corner[0], frame_up_left_corner[1]],
                     [frame_up_left_corner[0]+frame_width, frame_up_left_corner[1]],3)
    # bottom horizontal line
    pygame.draw.line(screen, BLACK,  [frame_up_left_corner[0], frame_up_left_corner[1]+frame_height],
                     [frame_up_left_corner[0]+frame_width, frame_up_left_corner[1]+frame_height], 3)

    # left vertical line
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

    # fill the board
    font_obj = pygame.font.Font("../assets/fonts/ARLRDBD.TTF", 25)
    for line in range (9):

        for column in range (9):
            if(default_board[line][column] != 0):
                # if(not (line == selected_case[0] -1 and column == selected_case[1] -1)):
                    text_surface_obj = font_obj.render(str(default_board[line][column]), True, BLACK)
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
                if default_board[line][column] != 0 :
                    text_surface_obj = font_obj.render(str(default_board[line][column]), True, WHITE)
                    text_rect_obj = text_surface_obj.get_rect()
                    text_rect_obj.center = (x, y)
                    text_rect_obj.height = 50
                    text_rect_obj.width = 50
                    screen.blit(text_surface_obj, text_rect_obj)






define_unchangeables()



def main():
    global selected_case,current_state
    done = False
    clock = pygame.time.Clock()
    moves = 0
    screen.fill(WHITE)
    draw_frame()
    while (not done):
        position = pygame.mouse.get_pos()

        if(position[0] >= help_mode_button[0] and position[0] <= help_mode_button[0] + 205 and
                position[1] >= help_mode_button[1] and position[1] <= help_mode_button[1] + 70 ):
            draw_frame(help_button=1)
        else:
            draw_frame()
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    data = game_coordinates_to_data(position[0], position[1])
                    print (data)
                    if(data[0] == 1):
                        print(default[data[1]-1][data[2]-1])
                        # for line in default:
                        #     print(line)

                        if(not (data[1] ==0  and data[2] == 0)):
                            if(default[data[1]-1][data[2]-1] == 0  ):
                                selected_case = [data[1],data[2]]
                            else:
                                selected_case = [-1, -1]
                        else:
                            selected_case = [-1, -1]
                            # pass
                    elif (data [0] == 2):
                        current_state = HELP_MODE
                    elif (data[0] == 3):
                        if (not (data[1] == 0 and data[2] == 0)):
                            if (default[data[1] - 1][data[2] - 1] == 0):
                                selected_case = [data[1], data[2]]
                            else:
                                selected_case = [-1, -1]
                        else:
                            selected_case = [-1, -1]

                    # print (selected_case)


            elif event.type == pygame.KEYDOWN:
                key_selection(default_board, event, selected_case)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
