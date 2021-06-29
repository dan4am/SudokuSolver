import sys
sys.path.append("..")
from src.image_processing import *
from src.solver import *
from ppadb.client import Client

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
