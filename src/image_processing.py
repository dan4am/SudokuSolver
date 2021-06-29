import sys
from ppadb.client import Client
import numpy as np
sys.path.append("..")
from src.solver import *
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

thickness =3
width = 106
height = 106
top_left_x = 48
top_left_y = 385

selector_centering = 50
selector_top_left_x = 120
selector_top_left_y = 1503

selector_width = 192
selector_height = 108


def connect_device():
    adb = Client(host='127.0.0.1',port=5037)
    devices = adb.devices()
    # print(devices)
    if len(devices) == 0:
        print("No Devices Attached")
        quit()
    return devices[0]


def take_screenshot(device):
    image = device.screencap()
    with open('../gui/screen1.png', 'wb') as f:
        f.write(image)
    # return image

list_numbers_as_pic=[]
for i in range(1,10):
    img = cv2.imread(str(i)+".png",0)
    list_numbers_as_pic.append(img)

def read_number(array,x,y):
    result = []
    for i in range (top_left_y + (thickness * y)+(height*(y-1)), top_left_y + (thickness *y )+(height*(y-1))+height):
        result.append([])
        for j in range (top_left_x+ (thickness * x) +(width * (x-1)), top_left_x+(width * (x-1))+ (thickness * x)+width):
            result[-1].append (array[i][j])
    return np.array(result)


def from_pic_to_number(pic):
    result = pytesseract.image_to_string(pic, config='--psm 10')
    result = result[0]
    if result == 'A':
        result = 4
    elif result == '_':
        result  = 0
    else:
        result = int(result)
    return result


def from_img_to_array(img):
    result = []
    for y in range (1,10):
        result.append([])
        for x in range(1,10):
            pic = read_number(img,x,y)
            result[-1].append(from_pic_to_number(pic))
    return result


def read_img_bw(path):
    img = cv2.imread(path, 0)
    for i in range (len(img)):
        for j in range( len (img[0])):
            if (img[i][j] < 150):
                img[i][j] = 0
            else:
                img[i][j] = 255

    # cv2.imwrite("test2.png", img)

    return img




def tap(device,x,y):
    x1 = top_left_x+ (thickness * x) + (width * (x-1)) + 4
    y1 = top_left_y + (thickness * y) + (height*(y-1)) + 4
    device.shell('input tap ' + str(x1)+" "+ str(y1))

def select_number(device, number):
    x = (number-1) % 3 + 1
    y = (number - 1) // 3 + 1

    x1 = selector_top_left_x+ (selector_centering * x) + (selector_width * (x-1)) + 4
    y1 = selector_top_left_y + (selector_centering * y) + (selector_height*(y-1)) + 4

    device.shell('input tap ' + str(x1) + " " + str(y1))

def solve_by_column(device):

    results = fill_by_column()
    no_possibility = True
    x=0
    y=0
    for square in results:
        if (len (square[1] )> 1):
            no_possibility = False
    while(not no_possibility):
        for list in results:
            if (len(list[1]) > 1):
                for i in range (1, len (list[1])):
                    x = list[1][i][1][0]
                    y = list[1][i][1][1]

                    default_board[x-1][y-1] = int(list[1][i][0][0])
                    number = int(list[1][i][0][0])

                    print(str(x) + "," + str(y)+" : "+str(number))

                    for line in default_board:
                        print(line)
                    tap(device, y, x)
                    select_number(device,number)


        results = fill_by_column()
        no_possibility = True
        for square in results:
            if (len(square[1]) > 1):
                no_possibility = False
        print( "loop finished column")


def solve_by_square(device):
    # copy_board(array)
    results = fill_by_square()
    no_possibility = True
    x=0
    y=0
    for square in results:
        if (len (square[1] )> 1):
            no_possibility = False
    while(not no_possibility):
        for list in results:
            if (len(list[1]) > 1):
                for i in range (1, len (list[1])):
                    x = list[1][i][1][0]
                    y = list[1][i][1][1]

                    default_board[x-1][y-1] = int(list[1][i][0][0])
                    number = int(list[1][i][0][0])

                    print(str(x) + "," + str(y)+" : "+str(number))
                    tap(device, y, x)
                    select_number(device,number)


        results = fill_by_square()
        no_possibility = True
        for square in results:
            if (len(square[1]) > 1):
                no_possibility = False
        print( "loop finished square")

def solve_by_line(device):
    # copy_board(array)
    results = fill_by_line()
    no_possibility = True
    x=0
    y=0
    for square in results:
        if (len (square[1] )> 1):
            no_possibility = False
    while(not no_possibility):
        for list in results:
            if (len(list[1]) > 1):
                for i in range (1, len (list[1])):
                    x = list[1][i][1][0]
                    y = list[1][i][1][1]

                    default_board[x-1][y-1] = int(list[1][i][0][0])
                    number = int(list[1][i][0][0])

                    print(str(x) + "," + str(y)+" : "+str(number))
                    tap(device, y, x)
                    select_number(device,number)


        results = fill_by_line()
        no_possibility = True
        for square in results:
            if (len(square[1]) > 1):
                no_possibility = False
        print( "loop finished line")





def main():
    # img = read_img_bw('screen.png')
    # test = from_img_to_array(img)
    # for line in test:
    #     print (line)

    device = connect_device()
    take_screenshot(device)
    # device.shell('input tap 600 455')
    img = read_img_bw('../gui/screen1.png')
    array = from_img_to_array(img)
    # for line in array:
    #     print (line)
    copy_board(array)
    solve_by_column(device)
    solve_by_square(device)
    solve_by_line(device)
    solve_by_column(device)
    solve_by_square(device)
    solve_by_line(device)

    # select_number(device,1)
    # cv2.imshow("window_name", img)
    # cv2.waitKey(0)

if __name__ == '__main__':
    main()
