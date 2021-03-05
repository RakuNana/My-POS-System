from tkinter import *
import mysql.connector


#def data_table():
data_win = Tk()
data_win.title("Employee Information")


db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="my_app_database",
            passwd="password",
            auth_plugin="mysql_native_password"
    )

mycursor = db.cursor()
mycursor = db.cursor(buffered=True)

main_frame = Frame(data_win)
main_frame.grid(row=0,column=0)

label_frame= Frame(data_win,padx=125)
label_frame.grid(row=1,column=0)

button_frame = Frame(data_win,)
button_frame.grid(row=2,column=0)

table_frame = Frame(data_win)
table_frame.grid(row=3,column=0)

table_win = Label(table_frame,text=" ")
table_win.grid()

def delete_entry():
    del_entry = "DELETE FROM my_app_data WHERE Employee_id=" + e_id_box.get()
    mycursor.execute(del_entry)
    db.commit()
    e_id_box.delete(0,END)
    print("deleted!!")

    fn_box.delete(0,END)
    ln_box.delete(0,END)
    ades_box.delete(0,END)
    dob_box.delete(0,END)
    title_box.delete(0,END)
    salary_box.delete(0,END)
    paswrd_box.delete(0,END)
    e_id_box.delete(0,END)

def update_table():
    update_fn = "UPDATE my_app_data SET First_name = %s , Last_name = %s , Address = %s , Date_of_Birth = %s , Title = %s , Salary = %s , Password = %s WHERE Employee_id = %s"
    data_getter= (fn_box.get(),ln_box.get() ,ades_box.get() , dob_box.get() ,title_box.get() ,salary_box.get(), paswrd_box.get(), e_id_box.get())
    mycursor.execute(update_fn,data_getter)
    #mycursor.execute("CREATE TABLE my_app_data (First_name VARCHAR(20), Last_name VARCHAR(20), Address VARCHAR(50) , Date_of_Birth VARCHAR(20), Title VARCHAR(20) ,
    #Salary FLOAT(00.00), Employee_id int AUTO_INCREMENT , PRIMARY KEY (Employee_id))")
    db.commit()

    fn_box.delete(0,END)
    ln_box.delete(0,END)
    ades_box.delete(0,END)
    dob_box.delete(0,END)
    title_box.delete(0,END)
    salary_box.delete(0,END)
    paswrd_box.delete(0,END)
    e_id_box.delete(0,END)
    print("UPDATED!!!!")

def add_btn():
    inserts="INSERT INTO my_app_data (First_name , Last_name , Address , Date_of_Birth , Title , Salary , Password, Employee_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    entry_insereter = (fn_box.get(),ln_box.get() ,ades_box.get() , dob_box.get() ,title_box.get() ,salary_box.get(),paswrd_box.get() , e_id_box.get() )
    mycursor.execute(inserts,entry_insereter)
    db.commit()

    fn_box.delete(0,END)
    ln_box.delete(0,END)
    ades_box.delete(0,END)
    dob_box.delete(0,END)
    title_box.delete(0,END)
    salary_box.delete(0,END)
    paswrd_box.delete(0,END)
    e_id_box.delete(0,END)

    print("Changes saved!")

def fetch_btn():
    id_sel = "SELECT * FROM my_app_data WHERE Employee_id =" + e_id_box.get()
    mycursor.execute(id_sel)

    show_table = mycursor.fetchone()

    table_win.config(text="\n".join(str(n)for n in show_table))
    table_win.grid(row=8,column=1)

    print(show_table)

    e_id_box.delete(0,END)
#alterer = " ALTER TABLE my_app_data ADD password int(6)"

#mycursor.execute(alterer)
#-------------------------------------------------------------------------------
data_label = Label(label_frame,text= "Add/Edit entry")
data_label.grid(row=0,column=1)

fn_label = Label(label_frame,text= "First Name")
fn_label.grid(row=1,column=0)

ln_label = Label(label_frame,text= "Last Name")
ln_label.grid(row=2,column=0)

ades_label = Label(label_frame,text= "Address")
ades_label.grid(row=3,column=0)

dob_label = Label(label_frame,text= "Date of birth")
dob_label.grid(row=4,column=0)

title_label = Label(label_frame,text= "Title")
title_label.grid(row=5,column=0)

salary_label = Label(label_frame,text= "Salary")
salary_label.grid(row=6,column=0)

paswrd_label = Label(label_frame,text= "Password")
paswrd_label.grid(row=7,column=0)

e_id_label = Label(label_frame,text= "Employee ID")
e_id_label.grid(row=8,column=0)

#-------------------------------------------------------------------------------
fn_box = Entry(label_frame)
fn_box.grid(row=1,column=1)

ln_box = Entry(label_frame)
ln_box.grid(row=2,column=1)

ades_box = Entry(label_frame)
ades_box.grid(row=3,column=1)

dob_box = Entry(label_frame)
dob_box.grid(row=4,column=1)

title_box = Entry(label_frame)
title_box.grid(row=5,column=1)

salary_box = Entry(label_frame)
salary_box.grid(row=6,column=1)

paswrd_box = Entry(label_frame)
paswrd_box.grid(row=7,column=1)

e_id_box = Entry(label_frame,width=3)
e_id_box.grid(row=8,column=1)
#-------------------------------------------------------------------------------

add_button = Button(button_frame,text="Add Entry",command=add_btn)
add_button.grid(row=9,column=1)

update_button = Button(button_frame,text="Update Entry",command=update_table)
update_button.grid(row=10,column=1)

fetch_button = Button(button_frame,text="Fetch List",command=fetch_btn)
fetch_button.grid(row=9,column=2)

del_button = Button(button_frame,text="Delete Entry",command=delete_entry)
del_button.grid(row=10,column=2)


data_win.mainloop()
