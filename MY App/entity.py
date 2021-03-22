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

pass_number = None
pass_id_names = None

#mycursor.execute("""CREATE TABLE Employee_Clock_in_out ( EM_First_name VARCHAR(50), EM_Last_name VARCHAR(50), Clock_in_time VARCHAR(50),
#Clock_out_time VARCHAR(50),Time_worked_today VARCHAR(50) , Total_week_time VARCHAR(50) , Employee_Time_ID int PRIMARY KEY , FOREIGN KEY(Employee_Time_ID) REFERENCES my_app_data(Employee_id) )""")
#db.commit()

#mycursor.execute("DROP TABLE Employee_Clock_in_out")
#db.commit()

#mycursor.execute("SHOW TABLES")
#for x in mycursor:
    #print(x)
    
#mycursor.execute("ALTER TABLE my_app_data ADD Time_worked_week VARCHAR(50)")
#db.commit()

#mycursor.execute("CREATE TABLE my_app_data (First_name VARCHAR(20), Last_name VARCHAR(20), Address VARCHAR(50) , Date_of_Birth VARCHAR(20), Title VARCHAR(20) ,
#Salary FLOAT(00.00), Employee_id int AUTO_INCREMENT , PRIMARY KEY (Employee_id))")
