import os
import sys

sys.path.append("..")
from src.image_processing import *
from src.solver import *
from ppadb.client import Client
import time

ip = "192.168.1.19"


def set_ip(ip_str):
    global ip
    ip = ip_str


def connect_device():
    os.system("adb kill-server")
    time.sleep(0.05)
    os.system("adb start-server")
    adb = Client(host='127.0.0.1',port=5037)
    adb.remote_connect(ip, 5555)
    devices = adb.devices()
    # print(devices)
    if len(devices) == 0:
        print("No Devices Attached")
        quit()
    return devices[0]

def disconnect_device():
    adb = Client(host='127.0.0.1',port=5037)
    adb.remote_disconnect()
    os.system("adb kill-server")

events=["sendevent  /dev/input/event4 3 58 5",
        "sendevent  /dev/input/event4 3 53 ",#1
        "sendevent  /dev/input/event4 3 54 ",#2
        "sendevent /dev/input/event4 3 330 1",
        "sendevent  /dev/input/event4 0 0 0",
        "sendevent  /dev/input/event4 0 2 0",
        "sendevent  /dev/input/event4 0 0 0"]

def take_screenshot(device,path_root=None):
    image = device.screencap()
    if path_root:
        with open('gui/screen1.png', 'wb') as f:
            f.write(image)
    else:
        with open('../gui/screen1.png', 'wb') as f:
            f.write(image)


def tap(device,x,y):
    x1 = top_left_x+ (thickness * x) + (width * (x-1)) + 4
    y1 = top_left_y + (thickness * y) + (height*(y-1)) + 4
    device.shell('input tap ' + str(x1)+" "+ str(y1) )
    # for i in range(len(events)):
    #     command = events[i]
    #     if (i == 1 or i == 8):
    #         command = command + str(x1)
    #     if (i == 2 or i == 9):
    #         command = command + str(y1)
    #     device.shell(command)
    #

def test(device, x, y):
    for i in range(len(events)):
        command = events[i]
        if (i == 1 or i == 8):
            command = command + str(x)
        if (i == 2 or i == 9):
            command = command + str(y)
        device.shell(command)

def select_number(device, number):
    x = (number-1) % 3 + 1
    y = (number - 1) // 3 + 1

    x1 = selector_top_left_x+ (selector_centering * x) + (selector_width * (x-1)) + 4
    y1 = selector_top_left_y + (selector_centering * y) + (selector_height*(y-1)) + 4

    device.shell('input tap ' + str(x1) + " " + str(y1))
    #
    # for i in range(len(events)):
    #     command = events[i]
    #     if (i == 1 or i == 8):
    #         command = command + str(x1)
    #     if (i == 2 or i == 9):
    #         command = command + str(y1)
    #     device.shell(command)

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
                    time.sleep(0.1)
                    select_number(device,number)
                    time.sleep(0.1)


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



def launch(path_root = None):
    device = connect_device()


    if path_root:
        take_screenshot(device, path_root=1)
        img = read_img_bw('gui/screen1.png')
    else:
        take_screenshot(device)
        img = read_img_bw('../gui/screen1.png')

    array = from_img_to_array(img)
    copy_board(array)
    solve_by_column(device)
    solve_by_square(device)
    solve_by_line(device)
    solve_by_column(device)
    solve_by_square(device)
    solve_by_line(device)

    disconnect_device()


def main():
    launch()
    # print(sys.path[0])
if __name__ == '__main__':
    main()
