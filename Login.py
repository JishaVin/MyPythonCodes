from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc
#---------------------------------------------------------------Login Function --------------------------------------
def clear():
	userentry.delete(0,END)
	passentry.delete(0,END)

def LoginClose():
	win.destroy()	


def login():
     if user_name.get()=="" or password.get()=="":

         messagebox.showerror("Error","Enter User Name And Password",parent=win)	
     else:
            
         try:
          con = pyodbc.connect(driver='{SQL Server}',
          Server='(local)',
          Database='SES',
          Trusted_Connection='yes')
          cur = con.cursor()


          cur.execute("select UserID,isnull(IsAdmin,0) as IsAdmin from UserDetails where UserName=? and Password = ?",(user_name.get(),password.get()))
          row = cur.fetchone()

          if row==None:
              messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)

          elif row.UserID>0 and row.IsAdmin==1:
              messagebox.showinfo("Success Admin" , "Successfully Login" , parent = win)
              LoginClose()
##              OpenNewWindow()
        
          else:
              messagebox.showinfo("Success Student" , "Successfully Login" , parent = win)
              LoginClose()
##              OpenNewWindow()
              
              

              con.close()
         except Exception as es:
          messagebox.showerror("Error" , f"Error Due to : {str(es)}", parent = win)



#--------------------------APPLICATION STARTS HERE----------------------

win = Tk()
# app title
win.title("School Election System")

# window size
win.maxsize(width=500 ,  height=250)
win.minsize(width=500 ,  height=250)


#heading label
heading = Label(win , text = "Login" , font = 'Verdana 12 bold')
heading.place(x=10 , y=25)

username = Label(win, text= "User Name :" , font='Verdana 10 bold')
username.place(x=20,y=100)

userpass = Label(win, text= "Password :" , font='Verdana 10  bold')
userpass.place(x=20,y=140)

# Entry Box
user_name = StringVar()
password = StringVar()
	
userentry = Entry(win, width=40 , textvariable = user_name)
userentry.focus()
userentry.place(x=200 , y=102)

passentry = Entry(win, width=40, show="*" ,textvariable = password)
passentry.place(x=200 , y=142)


# button login and clear

btn_login = Button(win, text = "Login" ,font='Verdana 10',command = login)
btn_login.place(x=100, y=186)


btn_login = Button(win, text = "Clear" ,font='Verdana 10', command = clear)
btn_login.place(x=260, y=186)


win.mainloop()
