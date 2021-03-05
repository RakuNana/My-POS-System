from tkinter import *
from datetime import *
import Business_database



root = Tk()
root.title("My app!!!")


passwrd_box = Entry()
passwrd_box.grid(row=0,column=1)

name_label = Label(root,text="Keycode")
name_label.grid(row=0,column=0)


class NumberPad:


    def __init__(self,master):
        frame_entry = Frame(master)
        frame_entry.grid(row=1, column=1)

        btn_0 = Button(master,text=0,command=button_zero)
        btn_0.grid(row=2,column=1)

        employ_data = Button(root,text="Enter Data" , command=data_entry)
        employ_data.grid(row=2,column=2)


        keypad_nums = "1234567890"
        i = 0
        btn_pad=[]

        for r in range(3):
            for c in range(3):
                btn_pad.append(Button(frame_entry, text = keypad_nums[i] , command = lambda b = i : passwrd_box.insert(END,keypad_nums[b])))
                btn_pad[i].grid(row=r,column=c)
                i += 1

def button_zero():
    zero = passwrd_box.insert(END,"0")


def clock_in():
    in_time = datetime.now()
    print(in_time)


def clock_out():
    out_time = datetime.now()
    print(out_time - in_time)


def data_entry():
    Business_database.data_table()
    print("works")


NP = NumberPad(root)
root.mainloop()
