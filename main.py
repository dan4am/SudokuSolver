from src.android_solver import launch, set_ip
from gui.gui_solver import launch_gui
from _thread import *
import threading
import sys
from gui import *
from tkinter import *
from tkinter import filedialog


connexion_choice=[]

widgets_entry_ip=[]
device_connection_choice=[]

def thread_android_solver():
    threading.Thread(target=launch).start()


def thread_gui_solver(root):
    if len (device_connection_choice) != 0:
        for widget in device_connection_choice:
            widget.destroy()

    root.geometry("300x200")
    t1 = threading.Thread(target=launch_gui)
    t1.daemon = True
    t1.start()
    # t1.join()

def thread_gui_solver_from_device():
    def from_device():
        launch_gui(android=1)

    t1 = threading.Thread(target=from_device)
    t1.daemon = True
    t1.start()

def entry_ip(root, choice,for_gui_or_cli):
    global widgets_entry_ip
    if len(device_connection_choice) != 0:
        for widget in widgets_entry_ip:
            widget.destroy()

    choice_num = choice.get()

    if (choice_num == 1):
        a = StringVar()
        ip = Label (root,justify = LEFT, text = "Set IP address",bg = "white")
        ip_entry = Entry(root,justify = LEFT,textvariable = a)

        button_start = Button(root, text="Start", command = lambda : save_ip(root, ip_entry.get(),for_gui_or_cli))
        widgets_entry_ip.append(ip)
        widgets_entry_ip.append(ip_entry)
        widgets_entry_ip.append(button_start)

        ip.pack(anchor = W, side = LEFT)
        ip_entry.pack(anchor = W, pady = 10, padx = 10, side = LEFT)
        button_start.pack(side = LEFT, padx = 10)
        # print (var.get())

        root.geometry("300x270")
    else:
        root.geometry("300x250")

def save_ip(root, ip, choice):
    set_ip(ip)
    print(ip)
    if choice == 1:
        thread_android_solver()

    else:
        thread_gui_solver_from_device()

def android_device(root,for_gui_or_cli):

    global  device_connection_choice
    if len (device_connection_choice) != 0:
        for widget in device_connection_choice:
            widget.destroy()


    choice = IntVar(root, value = -1)

    button_wired = Radiobutton(root,text = "Device connected via USB",tristatevalue=0, value = 2, variable = choice,
                               bg ="white", anchor = W,justify = LEFT)
    button_wireless = Radiobutton(root,text = "Device connected via Wi-Fi",tristatevalue=0,value = 1, variable = choice,
                                  bg ="white", anchor = W,justify = LEFT)
    button_done = Button(root,text = "Done",command = lambda : entry_ip(root,choice,for_gui_or_cli))

    device_connection_choice.append(button_wired)
    device_connection_choice.append(button_wireless)
    device_connection_choice.append(button_done)
    button_wireless.pack(side = TOP, pady = 10, anchor = W )
    button_wired.pack(side = TOP, anchor = W )
    button_done.pack(side = TOP, anchor = CENTER )
    root.geometry("300x250")

def main():

    print(sys.path[0])
    root = Tk()
    root.configure(bg="white")
    root.title("Sudoku solver")

    # button_android_solver = Button(root,text = "Android solver",width = 30, command = threading.Thread(target=launch, daemon=True).start)
    button_android_solver = Button(root,text = "Android solver",width = 30, command = lambda : android_device(root, 1))
    button_random_sudoku_grid = Button(root,text = "Random sudoku grid", width = 30,command = lambda:  thread_gui_solver(root) )
    button_grid_from_android_device= Button(root,text = "Grid from android device", width = 30, command = lambda : android_device(root, 2))

    button_random_sudoku_grid.pack(pady = 10)
    button_android_solver.pack(pady = 10)
    button_grid_from_android_device.pack(pady = 10)

    root.geometry("300x200")

    root.mainloop()


if __name__ == '__main__':
    main()