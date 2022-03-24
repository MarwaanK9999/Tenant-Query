import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import mysql.connector
from mysql.connector import Error

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(MainPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        master.title("Main")
        master.geometry("600x700")
        master.resizable(width=False, height=False)
        
        self.create_data()

        global viewDetails

        ft1 = tkFont.Font(family='Times', size=16)

        ft2 = tkFont.Font(family='Times', size=16)

        viewDetails = Listbox(self, font=ft2, justify="left")
        viewDetails.grid(row=0, columnspan=2, pady=10, ipadx=110, ipady=110)
        
        ViewCurrentMonth = Button(self, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="View outstanding payments for current month", command=lambda: self.viewCurrentPayment())
        ViewCurrentMonth.grid(row=1, column=0, ipadx=93)

        ViewPreviousMonth = Button(self, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="View outstanding payments for previous month", command=lambda: self.viewPreviousPayment())
        ViewPreviousMonth.grid(row=2, column=0, ipadx=87)

        ViewDiscount = Button(self, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="View tenants with discount", command=lambda: self.viewDiscount())
        ViewDiscount.grid(row=3, column=0, ipadx=170)

        Clear = Button(self, bg="#01aaed", borderwidth="4px", font=ft1, fg="#000000", justify="center", text="Clear", command=lambda: self.clearList())
        Clear.grid(row=4, column=0, ipadx=261) 


    def create_db_connection(self, host_name, user_name, user_password,db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
        except Error as err:
            print(f"Error: '{err}'")
        return connection

    def execute_query(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
        except Error as err:
            print(f"Error: '{err}'")

    def execute_get_query(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Error as err:
            print(f"Error: '{err}'")

    def create_data(self):

        connection = self.create_db_connection(
            "localhost", "root", "residentz", "tenantpayments")
        queryShowTables = "SHOW TABLES"

        a = self.execute_get_query(connection, queryShowTables)

        results_list = [item[0] for item in a]

        table = "payments"

        if table not in results_list:
            queryCreate = "CREATE TABLE payments (flatid INT AUTO_INCREMENT PRIMARY KEY, tenantname VARCHAR(255), tenantsurname VARCHAR(255), currentpayment FLOAT(7,2), previouspayment FLOAT(7,2), discount VARCHAR(255))"
            b = self.execute_query(connection, queryCreate)
            queryInsert = """
                INSERT INTO payments
                (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
                VALUES('Jason','Momoa','8000.00','8000.00','Yes')
                ;
                """
            x = self.execute_query(connection, queryInsert)
            queryInsert = """
                INSERT INTO payments
                (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
                VALUES('Brent','Affleck','0.00','8000.00','No')
                ;
                """
            x = self.execute_query(connection, queryInsert)
            queryInsert = """
                INSERT INTO payments
                (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
                VALUES('Jenna','Garner','8000.00','0.00','No')
                ;
                """
            x = self.execute_query(connection, queryInsert)
            queryInsert = """
                INSERT INTO payments
                (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
                VALUES('Peters','Davids','0.00','0.00','No')
                ;
                """
            x = self.execute_query(connection, queryInsert)
            queryInsert = """
                INSERT INTO payments
                (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
                VALUES('Nikita','Minaj','8000.00','8000.00','Yes')
                ;
                """
            x = self.execute_query(connection, queryInsert)
            queryInsert = """
                INSERT INTO payments
                (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
                VALUES('Taylor-Lautner','Swift','8000.00','0.00','No')
                ;
                """
            x = self.execute_query(connection, queryInsert)
            queryInsert = """
                INSERT INTO payments
                (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
                VALUES('Selena-Kyle','Gomez','0.00','0.00','No')
                ;
                """
            x = self.execute_query(connection, queryInsert)
            queryInsert = """
                INSERT INTO payments
                (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
                VALUES('Thierry-Henry','Cavill','8000.00','8000.00','Yes')
                ;
                """
            x = self.execute_query(connection, queryInsert)
            queryInsert = """
                INSERT INTO payments
                (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
                VALUES('Carole','Basculin','0.00','0.00','No')
                ;
                """
            x = self.execute_query(connection, queryInsert)
            queryInsert = """
                INSERT INTO payments
                (payments.tenantname,payments.tenantsurname,payments.currentpayment,payments.previouspayment,payments.discount)
                VALUES('Liu-Kang','Sang-Tsung','8000.00','0.00','No')
                ;
                """
            x = self.execute_query(connection, queryInsert)

    def viewCurrentPayment(self):

        viewDetails.delete(0, END)
        
        connection = self.create_db_connection(
            "localhost", "root", "residentz", "tenantpayments")
        
        query2 = """
        SELECT payments.tenantname, payments.tenantsurname, payments.flatid, payments.currentpayment 
        FROM payments
        WHERE payments.currentpayment = 0
        """
        y = self.execute_get_query(connection, query2)

        viewDetails.insert(END, "Tenant Details:")
        viewDetails.insert(END, " ")

        for items in y:
            newList = list(items)
            tenantName = newList[0]
            tenantSurname = newList[1]
            flatID = newList[2]
            currentPayment = newList[3]
            newString = "Tenant Full Name: " + tenantName + " " + tenantSurname  
            viewDetails.insert(END, newString)
            newString = "Flat Number: " + str(flatID)
            viewDetails.insert(END, newString)
            newString = "Amount Paid For This Month: " + "R" + str(currentPayment)
            viewDetails.insert(END, newString)
            viewDetails.insert(END, " ")

    def viewPreviousPayment(self):

        viewDetails.delete(0, END)

        connection = self.create_db_connection(
            "localhost", "root", "residentz", "tenantpayments")

        query2 = """
        SELECT payments.tenantname, payments.tenantsurname, payments.flatid, payments.previouspayment 
        FROM payments
        WHERE payments.previouspayment = 0
        """
        y = self.execute_get_query(connection, query2)

        viewDetails.insert(END, "Tenant Details:")
        viewDetails.insert(END, " ")

        for items in y:
            newList = list(items)
            tenantName = newList[0]
            tenantSurname = newList[1]
            flatID = newList[2]
            previousPayment = newList[3]
            newString = "Tenant Full Name: " + tenantName + " " + tenantSurname
            viewDetails.insert(END, newString)
            newString = "Flat Number: " + str(flatID)
            viewDetails.insert(END, newString)
            newString = "Amount Paid For Last Month: " + "R" + str(previousPayment)
            viewDetails.insert(END, newString)
            viewDetails.insert(END, " ")

    def viewDiscount(self):

        viewDetails.delete(0, END)

        connection = self.create_db_connection(
            "localhost", "root", "residentz", "tenantpayments")

        query2 = """
        SELECT payments.tenantname, payments.tenantsurname, payments.flatid, payments.discount
        FROM payments
        WHERE payments.discount = 'Yes'
        """
        y = self.execute_get_query(connection, query2)

        viewDetails.insert(END, "Tenant Details:")
        viewDetails.insert(END, " ")

        for items in y:
            newList = list(items)
            tenantName = newList[0]
            tenantSurname = newList[1]
            flatID = newList[2]
            discount = newList[3]
            newString = "Tenant Full Name: " + tenantName + " " + tenantSurname
            viewDetails.insert(END, newString)
            newString = "Flat Number: " + str(flatID)
            viewDetails.insert(END, newString)
            newString = "Discount " + discount
            viewDetails.insert(END, newString)
            viewDetails.insert(END, " ")

    def clearList(self):
        viewDetails.delete(0, END)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
