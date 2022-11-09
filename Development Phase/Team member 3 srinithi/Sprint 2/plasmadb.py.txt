from email.mime import image
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk    #pip isntall pillow
from tkinter import messagebox
import mysql.connector





def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All fields are required")
        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="221184@SJ",database="plasmadb")
            my_cursor=conn.cursor()
            query=("select * from donordetails where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another email")
            else:
                my_cursor.execute("insert into donordetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                   self.var_name.get(),
                                                                                   self.var_email.get(),
                                                                                   self.var_mobile.get(),
                                                                                   self.var_age.get(),
                                                                                   self.var_gender.get(),
                                                                                   self.var_bloodgroup.get(),
                                                                                   self.var_aadhar.get(),
                                                                                   self.var_state.get(),
                                                                                   self.var_city.get(),
                                                                                   self.var_password.get(),
                                                                                      )) 
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registered")