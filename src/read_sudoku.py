import sys
from random import seed
from random import randint



def get_grid(line_number, root_path=None):
    # # with open('../assets/sudoku.csv') as f:
    # with open('assets/sudoku.csv') as f:
    #     lines = f.readlines()
    path = ""
    if root_path:
        path = 'assets/sudoku.csv'
        # path = 'assets/hardsudoku.txt'
    else:
        path = '../assets/sudoku.csv'
        # path = '../assets/hardsudoku.txt'
    with open(path) as fp:
        for i, line in enumerate(fp):
            if i == line_number:
                lines = line
    # file = open('../assets/sudoku.csv')
    # lines = file.readline()
    # print(lines)
    sudoku=[]
    for i in range (9):
        sudoku.append([lines [i*9:(i*9)+9]])
        # sudoku.append([lines [line_number] [i*9:(i*9)+9]])
        for j in  range(9):
            sudoku[-1].append(int (sudoku[-1][0][j]))
        sudoku[-1].pop(0)
    # for k in sudoku:
    #     print (k)
    return sudoku

def get_rand_grid(root_path =None):
    number = randint(1,1000000)
    # number = randint(1,376)
    print (number)
    if root_path:
        return get_grid(number, root_path = 1)
    else:
        return get_grid(number)
def main():
    print (get_grid(2))
    # array = get_rand_grid()
    # for i in array:
    #     print (i)




if __name__ == "__main__":
    main()