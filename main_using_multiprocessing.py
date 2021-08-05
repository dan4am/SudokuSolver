import threading
import multiprocessing as mp
from tkinter import *
import time
import sys
from gui.gui_solver import launch_gui
from src.android_solver import launch, set_ip

connexion_choice=[]
end_thread=True
list_processes = []
list_processes_from_device = []
widgets_entry_ip=[]
device_connection_choice=[]
exit_event   =  threading.Event()
exit_event.set()


def process_android_solver():
    def launch_from_root():
        launch(path_root=1)
    mp.Process(target=launch_from_root()).start()


def random_grid():
    launch_gui(exit_event,root_path=1)

def process_gui_solver(root):
    global exit_event,list_threads
    if len (device_connection_choice) != 0:
        delete(root)

    if (len(list_processes) != 0):
        if(not list_processes[0].is_alive()):
            list_processes.clear()


    if (len(list_processes) == 0):
        root.geometry("300x170")
        p1 = mp.Process(target=random_grid)
        list_processes.append(p1)
        p1.daemon = True
        p1.start()

def from_device():
    print(len(list_processes_from_device))
    launch_gui(exit_event,android=1,root_path=1)

def process_gui_solver_from_device():
    global exit_event, list_processes_from_device

    if (len(list_processes_from_device) != 0):
        if (not list_processes_from_device[0].is_alive()):
            list_processes_from_device.clear()



    if (len(list_processes_from_device) == 0):
        p1 = mp.Process(target=from_device)
        p1.daemon = True
        list_processes_from_device.append(p1)
        p1.start()

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
        ip_entry.focus()
        ip_entry.insert(0,"192.168.1.19")

        button_start = Button(root, text="Start", command = lambda : save_ip(root, ip_entry,for_gui_or_cli))
        ip_entry.bind('<Return>', lambda event,root = root,ip_entry = ip_entry, choice = for_gui_or_cli : save_ip(root, ip_entry,choice))
        widgets_entry_ip.append(ip)
        widgets_entry_ip.append(ip_entry)
        widgets_entry_ip.append(button_start)

        ip.pack(anchor = W, side = LEFT)
        ip_entry.pack(anchor = W, pady = 10, padx = 10, side = LEFT)
        button_start.pack(side = LEFT, padx = 10)
        # print (var.get())

        root.geometry("300x300")
    else:
        root.geometry("300x280")

def save_ip(root, ip_entry, choice):
    set_ip(ip_entry.get())
    # print(ip_entry.get())
    if choice == 1:
        process_android_solver()

    else:
        process_gui_solver_from_device()

def delete(root):
    global  device_connection_choice
    if len (device_connection_choice) != 0:
        for widget in device_connection_choice:
            widget.destroy()
    if len(device_connection_choice) != 0:
        for widget in widgets_entry_ip:
            widget.destroy()
        root.geometry("300x170")

def android_device(root,for_gui_or_cli):



    delete(root)


    choice = IntVar(root, value = -1)

    button_wired = Radiobutton(root,text = "Device connected via USB",tristatevalue=0, value = 2, variable = choice,
                               bg ="white", anchor = W,justify = LEFT)
    button_wireless = Radiobutton(root,text = "Device connected via Wi-Fi",tristatevalue=0,value = 1, variable = choice,
                                  bg ="white", anchor = W,justify = LEFT)
    button_done = Button(root,text = "Done",command = lambda : entry_ip(root,choice,for_gui_or_cli))

    button_cancel = Button(root,text = "cancel",command = lambda : delete(root))

    device_connection_choice.append(button_wired)
    device_connection_choice.append(button_wireless)
    device_connection_choice.append(button_done)
    device_connection_choice.append(button_cancel)
    button_cancel.pack(side=TOP, anchor=CENTER)
    button_wireless.pack(side = TOP, pady = 10, anchor = W )

    button_wired.pack(side = TOP, anchor = W )
    button_done.pack(side = TOP, anchor = CENTER )

    root.geometry("300x280")

def launch_main():
    global exit_event
    print(sys.path[0])
    root = Tk()
    root.configure(bg="white")
    root.title("Sudoku solver")

    # button_android_solver = Button(root,text = "Android solver",width = 30, command = threading.Thread(target=launch, daemon=True).start)
    button_random_sudoku_grid = Button(root,text = "Random sudoku grid", width = 30,command = lambda:  process_gui_solver(root) )
    button_android_solver = Button(root,text = "Android solver",width = 30, command = lambda : android_device(root, 1))
    button_grid_from_android_device= Button(root,text = "Grid from android device", width = 30, command = lambda : android_device(root, 2))

    button_random_sudoku_grid.pack(pady = 10)
    button_android_solver.pack(pady = 10)
    button_grid_from_android_device.pack(pady = 10)

    root.geometry("300x170")
    root.iconbitmap('assets/Images/icon.ico')
    root.resizable(width=False, height=False)
    root.mainloop()
    sys.exit(0)


def main():
    print( mp.get_all_start_methods())

    main_process =  threading.Thread(target=launch_main())
    main_process.start()

if __name__ == '__main__':
    main()