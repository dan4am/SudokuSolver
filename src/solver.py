import sys
sys.path.append("..")
from src.image_processing import *
#
# default_board =   [[9, 0, 0, 4, 0, 0, 0, 0, 0],
#                    [0, 0, 8, 0, 2, 9, 4, 0, 0],
#                    [0, 0, 7, 8, 0, 0, 0, 0, 3],
#                    [1, 7, 0, 5, 0, 0, 0, 4, 0],
#                    [0, 0, 0, 0, 9, 8, 0, 0, 7],
#                    [8, 5, 0, 0, 0, 7, 6, 0, 0],
#                    [6, 0, 3, 9, 0, 1, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 9],
#                    [4, 0, 0, 2, 0, 0, 0, 8, 0]]


# default_board = [[9, 0, 0, 4, 0, 0, 8, 7, 0],
#                  [0, 0, 8, 7, 2, 9, 4, 0, 0],
#                  [0, 4, 7, 8, 0, 0, 0, 0, 3],
#                  [1, 7, 0, 5, 0, 2, 0, 4, 8],
#                  [0, 0, 4, 0, 9, 8, 0, 0, 7],
#                  [8, 5, 0, 0, 4, 7, 6, 0, 0],
#                  [6, 0, 3, 9, 0, 1, 0, 0, 4],
#                  [7, 0, 0, 0, 0, 4, 0, 0, 9],
#                  [4, 9, 0, 2, 0, 0, 0, 8, 0]]
default = []
# default_board = [[0,0,3,0,2,0,6,0,0],
#                  [9,0,0,3,0,5,0,0,1],
#                  [0,0,1,8,0,6,4,0,0],
#                  [0,0,8,1,0,2,9,0,0],
#                  [7,0,0,0,0,0,0,0,8],
#                  [0,0,6,7,0,8,2,0,0],
#                  [0,0,2,6,0,9,5,0,0],
#                  [8,0,0,2,0,3,0,0,9],
#                  [0,0,5,0,1,0,3,0,0]]

# default_board=[[0,1,0,0,0,7,3,0,0],
#                [0,0,0,3,0,0,5,0,9],
#                [0,0,6,8,0,0,0,0,0],
#                [0,8,0,0,9,0,0,0,0],
#                [0,0,0,5,0,2,0,0,0],
#                [5,0,9,7,0,0,0,0,1],
#                [0,0,7,0,0,3,0,8,4],
#                [9,6,1,0,0,0,0,0,5],
#                [8,4,3,2,5,0,0,0,0]]

# default_board = [[0,0,3,0,2,0,6,0,0],
#    [9,0,0,3,0,5,0,0,1],
#    [0,0,1,8,0,6,4,0,0],
#    [0,0,8,1,0,2,9,0,0],
#    [7,0,0,0,0,0,0,0,8],
#    [0,0,6,7,0,8,2,0,0],
#    [0,0,2,6,0,9,5,0,0],
#    [8,0,0,2,0,3,0,0,9],
#    [0,0,5,0,1,0,3,0,0]]
#
# default_board = [[0, 9, 0, 8, 0, 0, 0, 0, 0],
#                  [1, 0, 4, 3, 5, 0, 0, 0, 0],
#                  [5, 6, 0, 4, 2, 0, 3, 7, 0],
#                  [9, 3, 5, 1, 0, 8, 0, 4, 0],
#                  [0, 0, 6, 5, 0, 4, 8, 0, 0],
#                  [0, 4, 0, 7, 0, 2, 6, 5, 3],
#                  [0, 5, 3, 0, 4, 7, 0, 8, 6],
#                  [0, 0, 0, 0, 8, 5, 7, 0, 4],
#                  [0, 0, 0, 0, 0, 3, 0, 9, 0]]

# default_board = [[2,0,5,9,1,0,0,0,0],
#                  [0,0,0,7,0,2,6,0,0],
#                  [7,9,0,0,5,0,0,2,8],
#                  [6,0,7,0,3,0,0,5,0],
#                  [0,2,0,0,4,0,8,1,0],
#                  [5,0,0,1,6,0,0,0,3],
#                  [0,0,1,0,0,0,0,0,9],
#                  [0,6,0,0,0,0,0,8,0],
#                  [3,0,0,0,0,5,0,0,0]]


default_board = [[0,0,0,0,0,9,0,0,0],
                 [1,0,5,4,7,0,0,8,0],
                 [4,8,0,0,0,0,5,0,0],
                 [0,4,8,0,0,0,0,6,0],
                 [2,0,0,0,8,7,0,0,0],
                 [0,9,0,2,0,0,1,3,0],
                 [0,0,2,3,6,0,0,0,5],
                 [6,0,4,0,0,8,7,0,2],
                 [0,0,0,0,0,2,0,4,6]]

test_result = [[9, 0, 0, 4, 0, 0, 0, 0, 0],
               [0, 0, 8, 0, 2, 9, 4, 0, 0],
               [0, 0, 7, 8, 0, 0, 0, 0, 3],
               [1, 7, 0, 5, 0, 0, 0, 4, 0],
               [0, 0, 0, 0, 9, 8, 0, 0, 7],
               [8, 5, 0, 0, 0, 7, 6, 0, 0],
               [6, 0, 3, 9, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 9],
               [4, 0, 0, 2, 0, 0, 0, 8, 0]]

def define_unchangeables():
    global default
    default.clear()
    for line in range (9):
        default.append([])
        for column in range (9):
            if default_board[line][column] == 0:
                default[-1].append(0)
            else:
                default[-1].append(1)

def copy_board(array):
    for i in range(len (array)):
        for j in range (len (array[0])):
            default_board[i][j] = array[i][j]


def check_if_number_in_line(number, line):
    global default_board
    result = False
    for i in range (9):
        result = result or default_board[line][i] == number
    return result
def check_double_in_line(number, line):
    global default_board
    count = 0
    for i in range (9):
        if default_board[line][i] == number:
            count += 1
    return count >= 2

def check_if_number_in_column(number, column):
    global default_board
    result = False
    for i in range (9):
        result = result or default_board[i][column] == number
    return result

def check_double_in_column(number, column):
    global default_board
    count = 0
    for i in range(9):
        if default_board[i][column] == number:
            count += 1
    return count >= 2


def check_if_number_in_square(number, square):
    global default_board
    starting_line = int( square/3) * 3
    starting_column = int(square%3) * 3
    result = False
    for i in range (3):
        for j in range(3):
            result = result or default_board[starting_line + i][starting_column + j] == number
    return result
def check_double_in_square(number, line, column):
    global default_board
    square = (line //3) * 3 + (column//3)
    starting_line = int( square/3) * 3
    starting_column = int(square%3) * 3
    count = 0
    for i in range (3):
        for j in range(3):
            if default_board[starting_line + i][starting_column + j] == number:
                count += 1
    return count >= 2


def check_by_each_number():
    list_possibilities = []
    result = open("test-render.txt", "r+")
    for i in range (9):
        for j in range (9):
            list_possibilities.append([])
            if (not default_board[i][j] == 0):
                square = int(i / 3) * 3 + int(j / 3)
                list_possibilities[-1]=["coord = " + str(i+1) +" ," + str(j+1) +", " + str(square+1),"possibilities= ", default_board[i][j], "completed"]
            else:
                square = int(i/3) * 3 + int( j/3)
                list_possibilities[-1].append("coord = " + str(i+1) + " ," + str(j+1) + ", " + str(square+1))
                list_possibilities[-1].append("possibilities= ")
                for k in range (1,10):


                    # print (square)
                    if ((not check_if_number_in_line(k,i))  and (not check_if_number_in_column(k,j)) and
                            (not check_if_number_in_square(k,square)) ):
                        list_possibilities[-1].append(k)

    for list in list_possibilities:
        result.write(str(list) + "\n")

        # else:
        #     print (0)

def fill_by_line():
    # result = open("fill_by_line.txt", "r+")
    list_list_possibilities = []
    sure_choices = []

    #we first choose a number between 1 and 9
    line = 0
    for line in range (9):
        list_possible_positions = []
        for number in range (1,10):
            list_possible_positions.append([str(number) +" ="])
            #then we choose a line and do an action for each column in that line
            for column in range (9):
                square = int(line / 3) * 3 + int(column / 3)
                if (default_board[line][column] == 0):
                    if (not check_if_number_in_line(number,line)):
                        if(not check_if_number_in_column(number,column) and not check_if_number_in_square(number,square)):
                            list_possible_positions[-1].append ((line+1,column+1))

                else:
                    if (default_board[line][column] == number):
                        # list_possible_positions[-1].append (str(line+1) + " ,"+ str(column+1))
                        list_possible_positions.pop()
        list_list_possibilities.append(list_possible_positions)

    for occurence in range(9):
        # result.write("\n\n\n" + "square number " + str(occurence + 1) + "\n")
        sure_choices.append(["square " + str(occurence + 1) + " ="])
        for i in range(9):
            sure_choices[-1].append([str(i + 1) + " possibilties"])
        for line in list_list_possibilities[occurence]:
            if len(line) == 2:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][1].append(line)
            if len(line) == 3:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][2].append(line)
            if len(line) == 4:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][3].append(line)
            if len(line) == 5:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][4].append(line)
            if len(line) == 6:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][5].append(line)
            if len(line) == 7:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][6].append(line)
            if len(line) == 8:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][7].append(line)
            if len(line) == 9:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][8].append(line)
            if len(line) == 10:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][9].append(line)

            # else:
            #     sure_choices[-1].append([""])
            # result.write(str(line) + "\n")
    return sure_choices
    # for occurence in range (9):



    # for list in list_possibilities:
    #     result.write(str(list) + "\n")
def fill_by_column():
    # result = open("fill_by_column.txt", "r+")
    list_list_possibilities = []
    sure_choices = []

    # we first choose a number between 1 and 9
    for column in range(9):
        list_possible_positions = []
        for number in range(1, 10):
            list_possible_positions.append([str(number) + " ="])
            # then we choose a line and do an action for each column in that line
            for line in range(9):
                square = int(line / 3) * 3 + int(column / 3)
                if (default_board[line][column] == 0):
                    if (not check_if_number_in_column(number, column)):
                        if (not check_if_number_in_line(number, line) and not check_if_number_in_square(number,
                                                                                                            square)):
                            list_possible_positions[-1].append((line+1,column+1))

                else:
                    if (default_board[line][column] == number):
                        # list_possible_positions[-1].append (str(line+1) + " ,"+ str(column+1))
                        list_possible_positions.pop()
        list_list_possibilities.append(list_possible_positions)

    for occurence in range(9):
        # result.write("\n\n\n" + "square number " + str(occurence + 1) + "\n")
        sure_choices.append(["square " + str(occurence + 1) + " ="])
        for i in range(9):
            sure_choices[-1].append([str(i + 1) + " possibilties"])
        for line in list_list_possibilities[occurence]:
            if len(line) == 2:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][1].append(line)
            if len(line) == 3:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][2].append(line)
            if len(line) == 4:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][3].append(line)
            if len(line) == 5:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][4].append(line)
            if len(line) == 6:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][5].append(line)
            if len(line) == 7:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][6].append(line)
            if len(line) == 8:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][7].append(line)
            if len(line) == 9:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][8].append(line)
            if len(line) == 10:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][9].append(line)

            # else:
            #     sure_choices[-1].append([""])
            # result.write(str(line) + "\n")
    return sure_choices
    # for occurence in range (9):

def fill_by_column():
    # result = open("fill_by_column.txt", "r+")
    list_list_possibilities = []
    sure_choices = []

    # we first choose a number between 1 and 9
    for column in range(9):
        list_possible_positions = []
        for number in range(1, 10):
            list_possible_positions.append([str(number) + " ="])
            # then we choose a line and do an action for each column in that line
            for line in range(9):
                square = int(line / 3) * 3 + int(column / 3)
                if (default_board[line][column] == 0):
                    if (not check_if_number_in_column(number, column)):
                        if (not check_if_number_in_line(number, line) and not check_if_number_in_square(number,
                                                                                                            square)):
                            list_possible_positions[-1].append((line+1,column+1))

                else:
                    if (default_board[line][column] == number):
                        # list_possible_positions[-1].append (str(line+1) + " ,"+ str(column+1))
                        list_possible_positions.pop()
        list_list_possibilities.append(list_possible_positions)

    for occurence in range(9):
        # result.write("\n\n\n" + "square number " + str(occurence + 1) + "\n")
        sure_choices.append(["square " + str(occurence + 1) + " ="])
        for i in range(9):
            sure_choices[-1].append([str(i + 1) + " possibilties"])
        for line in list_list_possibilities[occurence]:
            if len(line) == 2:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][1].append(line)
            if len(line) == 3:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][2].append(line)
            if len(line) == 4:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][3].append(line)
            if len(line) == 5:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][4].append(line)
            if len(line) == 6:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][5].append(line)
            if len(line) == 7:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][6].append(line)
            if len(line) == 8:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][7].append(line)
            if len(line) == 9:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][8].append(line)
            if len(line) == 10:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][9].append(line)

            # else:
            #     sure_choices[-1].append([""])
            # result.write(str(line) + "\n")
    return sure_choices
    # for occurence in range (9):

def fill_by_square():
    # result = open("fill_by_square.txt", "r+")
    list_list_possibilities = []
    sure_choices = []

    # we first choose a number between 1 and 9
    for square in range(9):
        list_possible_positions = []
        for number in range(1, 10):
            list_possible_positions.append([str(number) + " ="])
            starting_line = int(square / 3) * 3
            starting_column = int(square % 3) * 3
            # then we choose a line and do an action for each column in that line
            for line in range(starting_line,starting_line + 3):
                for column in range(starting_column,starting_column + 3):

                    if (default_board[line][column] == 0):
                        if (not check_if_number_in_square(number, square)):
                            if (not check_if_number_in_line(number, line) and not check_if_number_in_column(number,
                                                                                                            column)):
                                list_possible_positions[-1].append((line+1,column+1))

                    else:
                        if (default_board[line][column] == number):
                            # list_possible_positions[-1].append (str(line+1) + " ,"+ str(column+1))
                            list_possible_positions.pop()
        list_list_possibilities.append(list_possible_positions)

    for occurence in range(9):
        # result.write("\n\n\n" + "square number " + str(occurence + 1) + "\n")
        sure_choices.append(["square "+ str (occurence + 1) + " ="])
        for i in range (9):
            sure_choices[-1].append([str(i+1) + " possibilties"])
        for line in list_list_possibilities[occurence]:
            if len (line) == 2:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][1].append(line)
            if len (line) == 3:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][2].append(line)
            if len (line) == 4:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][3].append(line)
            if len (line) == 5:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][4].append(line)
            if len (line) == 6:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][5].append(line)
            if len (line) == 7:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][6].append(line)
            if len (line) == 8:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][7].append(line)
            if len (line) == 9:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][8].append(line)
            if len (line) == 10:
                # sure_choices[-1][1].append(["1 possibility"])
                sure_choices[-1][9].append(line)



            # else:
            #     sure_choices[-1].append([""])
            # result.write(str(line) + "\n")
    return sure_choices
    # for occurence in range (9):


def main():
    test = fill_by_line()
    test = fill_by_column()
    test = fill_by_square()
    # check_by_each_number()
    # print (test)
    for column in test:
        print (column)

    # for line in default:
    #     print( line)
if __name__ == "__main__":
    main()