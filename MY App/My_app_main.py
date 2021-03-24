from tkinter import *
from datetime import *
import Business_database
import Timer_Tracker
import entity
import mysql.connector


db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="my_app_database",
            passwd="password",
            auth_plugin="mysql_native_password"
    )

mycursor = db.cursor()
mycursor = db.cursor(buffered=True)


root = Tk()
root.title("My app!!!")

global password_box
password_box = Entry(bg="snow3")
password_box.grid(row=0,column=1)

name_label = Label(root,text="Keycode")
name_label.grid(row=0,column=0)

logged_in_label = Label(root,text= " ")
logged_in_label.grid(row=4,column=1)


class NumberPad:


    def __init__(self,master):

        frame_entry = Frame(master)
        frame_entry.grid(row=1, column=1)

        btn_0 = Button(master,text=0,command=button_zero)
        btn_0.grid(row=2,column=1)

        global employ_data
        employ_data = Button(root,text="Enter Data" , command=data_entry)
        employ_data.grid(row=2,column=2)

        employ_data["state"] = DISABLED

        keypad_nums = "1234567890"
        i = 0
        btn_pad=[]

        for r in range(3):
            for c in range(3):
                btn_pad.append(Button(frame_entry, text = keypad_nums[i] , command = lambda b = i : password_box.insert(END,keypad_nums[b])))
                btn_pad[i].grid(row=r,column=c)
                i += 1

def button_zero():
    zero = password_box.insert(END,"0")

def data_entry():
    employ_data["state"] = DISABLED
    Business_database.data_table()


def clear_btn():
    password_box.delete(0,END)
    employ_data["state"] = DISABLED

def match_id():
    try:
        pw_match = password_box.get()

        if pw_match == "0000":
            employ_data["state"] = NORMAL
            print("unlocked")
        else:
            print("locked")

        #unlock_data = "SELECT First_name , Last_name FROM my_app_data WHERE Password= 2728"
        get_title = "SELECT First_name , Last_name FROM my_app_data WHERE Password= " + pw_match
        mycursor.execute(get_title)
        pw_rec = mycursor.fetchone()
        print(pw_rec)

        password_box.delete(0,END)
        logged_in_label.config(text=" Logged in as : " + " ".join(pw_rec) )

        entity.pass_number = pw_match
        print(entity.pass_number)
        

        #entity.pass_id_names = "SELECT First_name , Last_name  WHERE Employee_id = " + pw_match

        Timer_Tracker.time_tracker()

    except:
        #employ_data["state"] = DISABLED
        #print("no employee")
        pass


enter_btn = Button(root,text="Enter" ,bg="green", command=match_id)
enter_btn.grid(row=3,column=0)

clear_btn = Button(root,text="Clear" , bg="red", command=clear_btn)
clear_btn.grid(row=3,column=1)


NP = NumberPad(root)
root.mainloop()
