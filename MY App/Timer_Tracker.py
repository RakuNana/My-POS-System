from tkinter import *
from datetime import *
import mysql.connector
import entity

db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="my_app_database",
            passwd="password",
            auth_plugin="mysql_native_password"
    )

mycursor = db.cursor()
mycursor = db.cursor(buffered=True)


def time_tracker():
    time_trac = Tk()
    time_trac.title(" Clock in/out")

    list_insert = " SELECT Title FROM my_app_data WHERE Password = " + entity.pass_number
    mycursor.execute(list_insert)
    title_fetch = mycursor.fetchone()

    job_title = Listbox(time_trac,height=2)
    job_title.grid(row=0,column=0)

    job_title.insert(0,title_fetch)



    global in_btn
    in_btn = Button(time_trac, text="Clock In" , bg="green",command=clocking_in)
    in_btn.grid(row=1,column=1)

    global out_btn
    out_btn = Button(time_trac, text="Clock Out" , bg="red",command=clocking_out)
    out_btn.grid(row=1,column=2)

    out_btn["state"] = DISABLED

def clocking_in():
    in_btn["state"] = DISABLED
    out_btn["state"] = NORMAL
    global in_time
    in_time = datetime.now()
    name_getter = " SELECT First_name, Last_name FROM my_app_data WHERE Password = " + entity.pass_number
    mycursor.execute(name_getter)
    name_insert = mycursor.fetchall()

    

    print("Clocked in as : " + "".join(str(name_insert)[2:-2]) + " at: " + str(in_time.strftime("%y-%m-%d,%H:%M:%S")))

def clocking_out():
    in_btn["state"] = NORMAL
    out_btn["state"] = DISABLED
    global out_time
    out_time = datetime.now()
    print("Clocked out at : " + str(out_time.strftime("%y-%m-%d,%H:%M:%S")))
    print(out_time - in_time)
