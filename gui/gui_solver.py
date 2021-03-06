import time
import time
import sys
import threading
sys.path.append("..")
from src.solver import *
from gui.util import *
from src.android_solver import connect_device,disconnect_device,take_screenshot,tap,select_number
from src.image_processing import *
from src.read_sudoku import *


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

clear_button=[610,175]
help_mode_button=[610,265]
new_grid_button=[610,355]

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

######################
#     Sub States     #
######################
HELP_POSSIBILITIES=4

# screen = []


selected_case=[-1,-1]
threads=[]


# pygame.init()
# size = (900,600)
# screen = pygame.display.set_mode(size)



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
        elif (x >= clear_button[0] and x <= clear_button[0] + 205 and
              y >= clear_button[1] and y <= clear_button[1] + 70):
            return [5, 0, 0]
        elif (x >= new_grid_button[0] and x <= new_grid_button[0] + 205 and
              y >= new_grid_button[1] and y <= new_grid_button[1] + 70):
            return [6, 0, 0]

        else:
            return [1,0,0]

    elif(current_state == HELP_MODE):
        if (x >= frame_up_left_corner[0] and x <= frame_up_left_corner[0] + frame_width ) and \
                (y >= frame_up_left_corner[1] and y <= frame_up_left_corner[1]+frame_height):
            result = screen_coordinates_to_board_coordinates(x,y)
            return[3, result[0], result[1]]

        else:
            return [2,0,0]
    elif(current_state == HELP_POSSIBILITIES):
        pass
    else :
        return [-1,0,0]

def key_selection(test, event,selected_case,event_th, screen, clock, android = None,device = None, root_path=None):
    global current_state
######################################################laod a random grid###########################
    if event.key == pygame.K_r:
        if root_path:
            array = get_rand_grid(root_path=1)
            copy_board(array)
        else:
            array = get_rand_grid()
            copy_board(array)
        define_unchangeables()
######################################################laod a random grid###########################

########################################using keyboard arrows##############################
    elif event.key == pygame.K_LEFT:
        if(selected_case[0] == -1 and selected_case[1] == -1):
            selected_case[0] = 1
            selected_case[1] = 1
        if selected_case[1] == 1:
            temp_case = 9
        else:
            temp_case = selected_case[1] - 1
        # while (default[selected_case[0]-1][temp_case - 1] == 1):
        #     if temp_case == 1:
        #         temp_case = 9
        #     else:
        #         temp_case -= 1
        selected_case[1]=temp_case


    elif event.key == pygame.K_RIGHT:
        if (selected_case[0] == -1 and selected_case[1] == -1):
            selected_case[0] = 1
            selected_case[1] = 1
        if selected_case[1] == 9:
            temp_case = 1
        else:
            temp_case = selected_case[1] + 1
        # while (default[selected_case[0] - 1][temp_case - 1] == 1):
        #     if temp_case == 9:
        #         temp_case = 1
        #     else:
        #         temp_case += 1
        selected_case[1] = temp_case

    elif event.key == pygame.K_UP:
        if (selected_case[0] == -1 and selected_case[1] == -1):
            selected_case[0] = 1
            selected_case[1] = 1
        if selected_case[0] == 1:
            temp_case = 9
        else:
            temp_case = selected_case[0] - 1
        # while (default [temp_case - 1][selected_case[1] - 1] == 1):
        #     if temp_case == 1:
        #         temp_case = 9
        #     else:
        #         temp_case -= 1
        selected_case[0] = temp_case


    elif event.key == pygame.K_DOWN:
        if (selected_case[0] == -1 and selected_case[1] == -1):
            selected_case[0] = 1
            selected_case[1] = 1
        if selected_case[0] == 9:
            temp_case = 1
        else:
            temp_case = selected_case[0] + 1
        # while (default[temp_case - 1][selected_case[1] - 1] == 1):
        #     if temp_case == 9:
        #         temp_case = 1
        #     else:
        #         temp_case += 1
        selected_case[0] = temp_case
########################################using keyboard arrows##############################

########################################filling grid#######################################
    elif event.key == pygame.K_KP1:
        if(default[selected_case[0]-1][selected_case[1]-1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 1
            if android:
                select_number(device, 1)
    elif event.key == pygame.K_KP2:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 2
            if android:
                select_number(device, 2)
    elif event.key == pygame.K_KP3:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 3
            if android:
                select_number(device, 3)
    elif event.key == pygame.K_KP4:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 4
            if android:
                select_number(device, 4)
    elif event.key == pygame.K_KP5:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 5
            if android:
                select_number(device, 5)
    elif event.key == pygame.K_KP6:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 6
            if android:
                select_number(device, 6)
    elif event.key == pygame.K_KP7:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 7
            if android:
                select_number(device, 7)
    elif event.key == pygame.K_KP8:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 8
            if android:
                select_number(device, 8)
    elif event.key == pygame.K_KP9:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 9
            if android:
                select_number(device, 9)
    elif event.key == pygame.K_KP0:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            temp = test[selected_case[0] - 1][selected_case[1] - 1]
            test[selected_case[0] - 1][selected_case[1] - 1] = 0
            if android:
                select_number(device,temp)
    elif event.key == pygame.K_1:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 1
            if android:
                select_number(device, 1)
    elif event.key == pygame.K_2:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 2
            if android:
                select_number(device, 2)

    elif event.key == pygame.K_3:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 3
            if android:
                select_number(device, 3)
    elif event.key == pygame.K_4:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 4
            if android:
                select_number(device, 4)

    elif event.key == pygame.K_5:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 5
            if android:
                select_number(device, 5)

    elif event.key == pygame.K_6:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 6
            if android:
                select_number(device, 6)

    elif event.key == pygame.K_7:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 7
            if android:
                select_number(device, 7)
    elif event.key == pygame.K_8:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 8
            if android:
                select_number(device, 8)
    elif event.key == pygame.K_9:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 9
            if android:
                select_number(device, 9)
    elif event.key == pygame.K_0:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 0
            if android:
                select_number(device,test[selected_case[0] - 1][selected_case[1] - 1] )
    elif event.key == pygame.K_DELETE:
        if (default[selected_case[0] - 1][selected_case[1] - 1] != 1):
            test[selected_case[0] - 1][selected_case[1] - 1] = 0
            if android:
                select_number(device,test[selected_case[0] - 1][selected_case[1] - 1] )
    elif event.key == pygame.K_ESCAPE:
        clear()

    ########################################filling grid#######################################


    ######################################start auto solving###################################
    elif event.key ==  pygame.K_s:
        if root_path:
            visualize_by_square(event_th, screen, clock, root_path=1)

            # visualize_by_column(clock)

            visualize_by_line(event_th, screen, clock, root_path=1)

            visualize_by_square(event_th, screen, clock, root_path=1)

            visualize_by_column(event_th, screen, clock, root_path=1)

        else:

            visualize_by_square(event_th, screen, clock)

            # visualize_by_column(clock)

            visualize_by_line(event_th, screen, clock)

            visualize_by_square(event_th, screen, clock)

            visualize_by_column(event_th, screen, clock)
 ######################################start auto solving###################################


def draw_frame(screen, help_button = None, clear = None, new_grid = None,root_path = None):
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
            if root_path:
                font_obj = pygame.font.Font("assets/fonts/ARLRDBD.TTF", 32)
            else:
                font_obj = pygame.font.Font("../assets/fonts/ARLRDBD.TTF", 32)
            text_surface_obj = font_obj.render("Solve", True, WHITE)
            text_rect_obj = text_surface_obj.get_rect()
            text_rect_obj.center = (help_mode_button[0] + 102, help_mode_button[1] + 35)
            screen.blit(text_surface_obj, text_rect_obj)

        else:
            pygame.draw.rect(screen, BLACK, pygame.Rect(help_mode_button[0], help_mode_button[1], 205, 70),2)
            if root_path:
                font_obj = pygame.font.Font("assets/fonts/ARLRDBD.TTF", 32)
            else:
                font_obj = pygame.font.Font("../assets/fonts/ARLRDBD.TTF", 32)
            text_surface_obj = font_obj.render("Solve", True, BLACK)
            text_rect_obj = text_surface_obj.get_rect()
            text_rect_obj.center = (help_mode_button[0] + 102, help_mode_button[1] + 35)
            screen.blit(text_surface_obj, text_rect_obj)

        if(clear):
            pygame.draw.rect(screen, BLACK, pygame.Rect(clear_button[0], clear_button[1], 205, 70))
            if root_path:
                font_obj = pygame.font.Font("assets/fonts/ARLRDBD.TTF", 32)
            else:
                font_obj = pygame.font.Font("../assets/fonts/ARLRDBD.TTF", 32)
            text_surface_obj = font_obj.render("Clear", True, WHITE)
            text_rect_obj = text_surface_obj.get_rect()
            text_rect_obj.center = (clear_button[0] + 102, clear_button[1] + 35)
            screen.blit(text_surface_obj, text_rect_obj)
        else:
            pygame.draw.rect(screen, BLACK, pygame.Rect(clear_button[0], clear_button[1], 205, 70), 2)
            if root_path:
                font_obj = pygame.font.Font("assets/fonts/ARLRDBD.TTF", 32)
            else:
                font_obj = pygame.font.Font("../assets/fonts/ARLRDBD.TTF", 32)
            text_surface_obj = font_obj.render("Clear", True, BLACK)
            text_rect_obj = text_surface_obj.get_rect()
            text_rect_obj.center = (clear_button[0] + 102, clear_button[1] + 35)
            screen.blit(text_surface_obj, text_rect_obj)

        if (new_grid):
            pygame.draw.rect(screen, BLACK, pygame.Rect(new_grid_button[0], new_grid_button[1], 205, 70))
            if root_path:
                font_obj = pygame.font.Font("assets/fonts/ARLRDBD.TTF", 32)
            else:
                font_obj = pygame.font.Font("../assets/fonts/ARLRDBD.TTF", 32)
            text_surface_obj = font_obj.render("New Grid", True, WHITE)
            text_rect_obj = text_surface_obj.get_rect()
            text_rect_obj.center = (new_grid_button[0] + 102, new_grid_button[1] + 35)
            screen.blit(text_surface_obj, text_rect_obj)
        else:
            pygame.draw.rect(screen, BLACK, pygame.Rect(new_grid_button[0], new_grid_button[1], 205, 70), 2)
            if root_path:
                font_obj = pygame.font.Font("assets/fonts/ARLRDBD.TTF", 32)
            else:
                font_obj = pygame.font.Font("../assets/fonts/ARLRDBD.TTF", 32)
            text_surface_obj = font_obj.render("New Grid", True, BLACK)
            text_rect_obj = text_surface_obj.get_rect()
            text_rect_obj.center = (new_grid_button[0] + 102, new_grid_button[1] + 35)
            screen.blit(text_surface_obj, text_rect_obj)

    elif (current_state == HELP_MODE):

        #draw the banner of help mode
        pygame.draw.rect(screen, BLACK, pygame.Rect(help_mode_banner[0], help_mode_banner[1], 299, 30), 2)
        if root_path:
            font_obj = pygame.font.Font("assets/fonts/ARLRDBD.TTF", 30)
        else:
            font_obj = pygame.font.Font("../assets/fonts/ARLRDBD.TTF", 30)
        text_surface_obj = font_obj.render("help mode", True, BLACK)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (help_mode_banner[0] + 150, help_mode_banner[1] + 14)
        screen.blit(text_surface_obj, text_rect_obj)

        #draw the possibiities.
        font_obj = pygame.font.Font("../assets/fonts/ARLRDBD.TTF", 30)



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
    if root_path:
        font_obj = pygame.font.Font("assets/fonts/ARLRDBD.TTF", 25)
    else:
        font_obj = pygame.font.Font("../assets/fonts/ARLRDBD.TTF", 25)
    for line in range (9):

        for column in range (9):
            if(default_board[line][column] != 0):
                # if(not (line == selected_case[0] -1 and column == selected_case[1] -1)):
                    if(default[line][column] == 1):
                        text_surface_obj = font_obj.render(str(default_board[line][column]), True, BLACK)
                    else:
                        number_in_case = default_board[line][column]
                        if (check_double_in_column(number_in_case, column) or check_double_in_line(number_in_case,line)
                        or check_double_in_square(number_in_case, line, column)):
                            text_surface_obj = font_obj.render(str(default_board[line][column]), True, RED)
                        else:
                            text_surface_obj = font_obj.render(str(default_board[line][column]), True, GREEN)
                        # check_if_number_in_square(number_in_case, )
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
                    if(default[line][column] == 1):
                        text_surface_obj = font_obj.render(str(default_board[line][column]), True,WHITE)
                    else:
                        number_in_case = default_board[line][column]
                        if (check_double_in_column(number_in_case, column) or check_double_in_line(number_in_case,line)
                        or check_double_in_square(number_in_case, line, column)):
                            text_surface_obj = font_obj.render(str(default_board[line][column]), True, RED)
                        else:
                            text_surface_obj = font_obj.render(str(default_board[line][column]), True, GREEN)
                    text_rect_obj = text_surface_obj.get_rect()
                    text_rect_obj.center = (x, y)
                    text_rect_obj.height = 50
                    text_rect_obj.width = 50
                    screen.blit(text_surface_obj, text_rect_obj)




def visualize_by_square(event_th,screen,clock,root_path =None):
    global selected_case
    results = fill_by_square()
    no_possibility = True
    for square in results:
        if (len (square[1] )> 1):
            no_possibility = False
    while((not no_possibility) and event_th.isSet()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        for list in results:
            if (len(list[1]) > 1):
                for i in range (1, len (list[1])):
                    selected_case[0] = list[1][i][1][0]
                    selected_case[1] = list[1][i][1][1]
                    print (selected_case)
                    time.sleep(0.04)
                    if root_path:
                        draw_frame(screen, root_path=1)
                    else:
                        draw_frame(screen)

                    pygame.display.flip()
                    # print (int(list[1][i][0][0]))
                    default_board[selected_case[0]-1][selected_case[1]-1] = int(list[1][i][0][0])
                    # time.sleep(0.07)
                    if root_path:
                        draw_frame(screen, root_path=1)
                    else:
                        draw_frame(screen)
                    pygame.display.flip()


        results = fill_by_square()
        no_possibility = True
        for square in results:
            if (len(square[1]) > 1):
                no_possibility = False
        pygame.display.flip()
        print( "loop finished square")
        clock.tick(60)


def visualize_by_column(event_th,screen, clock,root_path = None):
    global selected_case
    results = fill_by_column()
    no_possibility = True
    for square in results:
        if (len (square[1] )> 1):
            no_possibility = False
    while((not no_possibility) and event_th.isSet()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        for list in results:
            if (len(list[1]) > 1):
                for i in range (1, len (list[1])):
                    selected_case[0] = list[1][i][1][0]
                    selected_case[1] = list[1][i][1][1]
                    print (selected_case)
                    time.sleep(0.04)
                    if root_path:
                        draw_frame(screen, root_path=1)
                    else:
                        draw_frame(screen)
                    pygame.display.flip()
                    # print (int(list[1][i][0][0]))
                    default_board[selected_case[0]-1][selected_case[1]-1] = int(list[1][i][0][0])
                    # time.sleep(0.1)
                    if root_path:
                        draw_frame(screen, root_path=1)
                    else:
                        draw_frame(screen)
                    pygame.display.flip()


        results = fill_by_column()
        no_possibility = True
        for square in results:
            if (len(square[1]) > 1):
                no_possibility = False
        pygame.display.flip()
        print( "loop finished column")
        clock.tick(60)

def visualize_by_line(event_th,screen, clock,root_path = None):
    global selected_case
    results = fill_by_line()
    no_possibility = True
    for square in results:
        if (len (square[1] )> 1):
            no_possibility = False
    while((not no_possibility) and event_th.isSet()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        for list in results:
            if (len(list[1]) > 1):
                for i in range (1, len (list[1])):
                    selected_case[0] = list[1][i][1][0]
                    selected_case[1] = list[1][i][1][1]
                    print (selected_case)
                    time.sleep(0.04)
                    if root_path:
                        draw_frame(screen,root_path=1)
                    else:
                        draw_frame(screen)
                    pygame.display.flip()
                    # print (int(list[1][i][0][0]))
                    default_board[selected_case[0]-1][selected_case[1]-1] = int(list[1][i][0][0])
                    # time.sleep(0.1)
                    if root_path:
                        draw_frame(screen, root_path=1)
                    else:
                        draw_frame(screen)
                    pygame.display.flip()


        results = fill_by_line()
        no_possibility = True
        for square in results:
            if (len(square[1]) > 1):
                no_possibility = False
        pygame.display.flip()
        print( "loop finished line")
        clock.tick(60)



def launch_gui(event_th = True,android = None, root_path = None ):
    global selected_case, current_state, end_thread
    device = None
    if android:
        device = connect_device()

        if root_path:
            take_screenshot(device,path_root = 1)
            img = read_img_bw('gui/screen1.png')
        else:
            take_screenshot(device)
            img = read_img_bw('../gui/screen1.png')
        array = from_img_to_array(img)
        copy_board(array)
        define_unchangeables()
    else:
        if root_path:
            pygame.display.set_icon(pygame.image.load("assets/Images/icon.png"))
            rand_array = get_rand_grid(root_path=1)
            copy_board(rand_array)
        else:
            pygame.display.set_icon(pygame.image.load("../assets/Images/icon.png"))
            rand_array = get_rand_grid()
            copy_board(rand_array)
        define_unchangeables()

    pygame.init()
    size = (900, 600)
    screen = pygame.display.set_mode(size)





    done = False
    clock = pygame.time.Clock()
    moves = 0
    screen.fill(WHITE)
    if root_path:
        draw_frame(screen,root_path = 1)
    else:
        draw_frame(screen)
    while ((not done) and event_th.isSet() ):
        position = pygame.mouse.get_pos()

        if(position[0] >= help_mode_button[0] and position[0] <= help_mode_button[0] + 205 and
                position[1] >= help_mode_button[1] and position[1] <= help_mode_button[1] + 70 ):
            if root_path:
                draw_frame(screen,help_button=1, root_path=1)
            else:
                draw_frame(screen,help_button=1)

        elif (position[0] >= clear_button[0] and position[0] <= clear_button[0] + 205 and
                position[1] >= clear_button[1] and position[1] <= clear_button[1] + 70):
            if root_path:
                draw_frame(screen, clear = 1, root_path=1)
            else:
                draw_frame(screen, clear = 1)

        elif (position[0] >= new_grid_button[0] and position[0] <= new_grid_button[0] + 205 and
                position[1] >= new_grid_button[1] and position[1] <= new_grid_button[1] + 70):
            if root_path:
                draw_frame(screen, new_grid = 1, root_path=1)
            else:
                draw_frame(screen, new_grid = 1)
        else:
            if root_path:
                draw_frame(screen, root_path=1)
            else:
                draw_frame(screen)
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    data = game_coordinates_to_data(position[0], position[1])
                    # print (data)
                    if(data[0] == 1):
                        # print(default[data[1]-1][data[2]-1])
                        # for line in default:
                        #     print(line)

                        if(not (data[1] ==0  and data[2] == 0)):
                            if(default[data[1]-1][data[2]-1] == 0  ):
                                # if android:
                                #     tap(device, data[2], data[1])
                                selected_case = [data[1],data[2]]

                            else:
                                selected_case = [-1, -1]
                        else:
                            selected_case = [-1, -1]
                            # pass
                    elif (data [0] == 2):
                        # current_state = HELP_MODE
                        # visualize_by_line(clock)
                        if root_path:
                            visualize_by_square(event_th,screen, clock,root_path = 1)

                            # visualize_by_column(clock)

                            visualize_by_line(event_th,screen, clock,root_path = 1)

                            visualize_by_square(event_th,screen, clock,root_path = 1)

                            visualize_by_column(event_th,screen, clock,root_path = 1)

                        else:

                            visualize_by_square(event_th,screen,clock)

                            # visualize_by_column(clock)

                            visualize_by_line(event_th,screen,clock)

                            visualize_by_square(event_th,screen,clock)

                            visualize_by_column(event_th, screen,clock)

                    elif (data[0] == 3):
                        if (not (data[1] == 0 and data[2] == 0)):
                            if (default[data[1] - 1][data[2] - 1] == 0):
                                selected_case = [data[1], data[2]]
                                by_c= fill_by_column()
                                by_l= fill_by_line()
                                by_s= fill_by_square()
                                print("by line = "+ str (by_l[selected_case[0]-1][selected_case[1]-1]))
                                print("by column = "+ str (by_c[selected_case[0]-1][selected_case[1]-1]))
                                print("by square = "+ str (by_s[selected_case[0]-1][selected_case[1]-1]))
                            else:
                                selected_case = [-1, -1]
                        else:
                            selected_case = [-1, -1]
                    elif(data[0] == 5):
                        clear()
                    elif(data[0] == 6):
                        if root_path:
                            array = get_rand_grid(root_path=1)
                            copy_board(array)
                        else:
                            array = get_rand_grid()
                            copy_board(array)
                        define_unchangeables()
                    # print (selected_case)


            elif event.type == pygame.KEYDOWN:
                # if android:
                #     key_selection(default_board, event, selected_case,android = 1, device = device)
                # else:
                   if root_path:
                       key_selection(default_board, event, selected_case,event_th, screen, clock, root_path = 1)

                   else:
                       key_selection(default_board, event, selected_case,event_th, screen, clock)


        pygame.display.flip()
        clock.tick(60)

    if android:
        disconnect_device()
    pygame.quit()
    sys.exit(0)



def main():
    rand_event  = threading.Event()
    rand_event.set()
    launch_gui(rand_event)

if __name__ == '__main__':
    main()
