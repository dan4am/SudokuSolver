import json
#
# test = [[9,0,0,4,0,0,0,0,0],
#         [0,0,8,0,2,9,4,0,0],
#         [0,0,7,8,0,0,0,0,3],
#         [1,7,0,5,0,0,0,4,0],
#         [0,0,0,0,9,8,0,0,7],
#         [8,5,0,0,0,7,6,0,0],
#         [6,0,3,9,0,1,0,0,0],
#         [0,0,0,0,0,0,0,0,9],
#         [4,0,0,2,0,0,0,8,0]]


test = [[9,0,0,4,0,0,8,7,0],
        [0,0,8,7,2,9,4,0,0],
        [0,4,7,8,0,0,0,0,3],
        [1,7,0,5,0,2,0,4,8],
        [0,0,4,0,9,8,0,0,7],
        [8,5,0,0,4,7,6,0,0],
        [6,0,3,9,0,1,0,0,4],
        [7,0,0,0,0,4,0,0,9],
        [4,9,0,2,0,0,0,8,0]]

# test = [[0,9,0,8,0,0,0,0,0],
#   [1,0,4,3,5,0,0,0,0],
#   [5,6,0,4,2,0,3,7,0],
#   [9,3,5,1,0,8,0,4,0],
#   [0,0,6,5,0,4,8,0,0],
#   [0,4,0,7,0,2,6,5,3],
#   [0,5,3,0,4,7,0,8,6],
#   [0,0,0,0,8,5,7,0,4],
#   [0,0,0,0,0,3,0,9,0]]

test_result = [[9,0,0,4,0,0,0,0,0],
               [0,0,8,0,2,9,4,0,0],
               [0,0,7,8,0,0,0,0,3],
               [1,7,0,5,0,0,0,4,0],
               [0,0,0,0,9,8,0,0,7],
               [8,5,0,0,0,7,6,0,0],
               [6,0,3,9,0,1,0,0,0],
               [0,0,0,0,0,0,0,0,9],
               [4,0,0,2,0,0,0,8,0]]


def check_if_number_in_line(number, line):
    global test
    result = False
    for i in range (9):
        result = result or test[line][i] == number
    return result

def check_if_number_in_column(number, column):
    global test
    result = False
    for i in range (9):
        result = result or test[i][column] == number
    return result

def check_if_number_in_square(number, square):
    global test
    starting_line = int( square/3) * 3
    starting_column = int(square%3) * 3
    result = False
    for i in range (3):
        for j in range(3):
            result = result or test[starting_line + i][starting_column + j] == number
    return result

def check_by_each_number():
    list_possibilities = []
    result = open("test-render.txt", "r+")
    for i in range (9):
        for j in range (9):
            list_possibilities.append([])
            if (not test[i][j] == 0):
                square = int(i / 3) * 3 + int(j / 3)
                list_possibilities[-1]=["coord = "+str(i+1)+" ,"+ str(j+1)+", "+str(square+1),"possibilities= ",test[i][j], "completed"]
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
    result = open("fill_by_line.txt", "r+")
    list_list_possibilities = []

    #we first choose a number between 1 and 9
    line = 0
    for line in range (9):
        list_possible_positions = []
        for number in range (1,10):
            list_possible_positions.append([str(number) +" ="])
            #then we choose a line and do an action for each column in that line
            for column in range (9):
                square = int(line / 3) * 3 + int(column / 3)
                if (test[line][column] == 0):
                    if (not check_if_number_in_line(number,line)):
                        if(not check_if_number_in_column(number,column) and not check_if_number_in_square(number,square)):
                            list_possible_positions[-1].append ((line+1,column+1))

                else:
                    if (test[line][column] == number):
                        # list_possible_positions[-1].append (str(line+1) + " ,"+ str(column+1))
                        list_possible_positions.pop()
        list_list_possibilities.append(list_possible_positions)

    for occurence in range(9):
        result.write("\n\n\n"+"Line number "+ str(occurence+1) + "\n" )
        for line in list_list_possibilities[occurence]:
            result.write(str(line) + "\n")




    # for list in list_possibilities:
    #     result.write(str(list) + "\n")
def fill_by_column():
    result = open("fill_by_column.txt", "r+")
    list_list_possibilities = []

    # we first choose a number between 1 and 9
    for column in range(9):
        list_possible_positions = []
        for number in range(1, 10):
            list_possible_positions.append([str(number) + " ="])
            # then we choose a line and do an action for each column in that line
            for line in range(9):
                square = int(line / 3) * 3 + int(column / 3)
                if (test[line][column] == 0):
                    if (not check_if_number_in_column(number, column)):
                        if (not check_if_number_in_line(number, line) and not check_if_number_in_square(number,
                                                                                                            square)):
                            list_possible_positions[-1].append((line+1,column+1))

                else:
                    if (test[line][column] == number):
                        # list_possible_positions[-1].append (str(line+1) + " ,"+ str(column+1))
                        list_possible_positions.pop()
        list_list_possibilities.append(list_possible_positions)

    for occurence in range(9):
        result.write("\n\n\n" + "Column number " + str(occurence + 1) + "\n")
        for line in list_list_possibilities[occurence]:
            result.write(str(line) + "\n")

def fill_by_square():
    result = open("fill_by_square.txt", "r+")
    list_list_possibilities = []

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

                    if (test[line][column] == 0):
                        if (not check_if_number_in_square(number, square)):
                            if (not check_if_number_in_line(number, line) and not check_if_number_in_column(number,
                                                                                                            column)):
                                list_possible_positions[-1].append((line+1,column+1))

                    else:
                        if (test[line][column] == number):
                            # list_possible_positions[-1].append (str(line+1) + " ,"+ str(column+1))
                            list_possible_positions.pop()
        list_list_possibilities.append(list_possible_positions)

    for occurence in range(9):
        result.write("\n\n\n" + "square number " + str(occurence + 1) + "\n")
        for line in list_list_possibilities[occurence]:
            result.write(str(line) + "\n")

def main():
    fill_by_line()
    fill_by_column()
    fill_by_square()
    check_by_each_number()
if __name__ == "__main__":
    main()