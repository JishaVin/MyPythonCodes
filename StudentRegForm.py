from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc
from tkinter import filedialog
from PIL import Image, ImageTk

##-----------------------Common Functions------------------------------------


def only_numbers(char):
        return char.isdigit()

#------------------------------------------------Student Registration Form-----------------------------------------------------
def StudentRegn():
    
    

    def CloseClick():
        Stwindow.destroy()

    def clearControls():
        AdmnNo.set("")
        FName.set("")
        LName.set("")
        ddClass.set("Choose your class")
        ddDiv.set("Choose your Division")
        label_photo.config(image="")
        house=IntVar(value=0)
        gender=IntVar(value=0)

    def uploadImg():
        global image,label_photo
        filename = filedialog.askopenfilename(title = "Select an Image", filetype = (("jpeg files","*.jpg"),("PNG  files","*.png")))
        image = Image.open(filename) # Read the Image
            
        resize_image = image.resize((200, 160)) # Reszie the image using resize() method

        show_img = ImageTk.PhotoImage(resize_image) # create label and to add the resize image

        label_photo = Label(img_LabelFrame,image=show_img)
        label_photo.config(image=show_img)

        label_photo.image = show_img
        label_photo.pack()
    
    def save_Img():
        savepath="D:\\SES\\" + AdmnNo.get() + ".jpg"
        image.save(savepath)

    def SaveClick():
        if  AdmnNo.get()=="" or FName.get()=="" or LName.get()=="" or ddClass.get()=="" or ddDiv.get()=="" or ddClass.get()== "Choose your class" or ddDiv.get()== "Choose your Division" :
            messagebox.showerror("Error","Enter All the Details",parent=Stwindow)
            
        else:
                try:
                    con = pyodbc.connect(driver='{SQL Server}',
                    Server='(local)',
                    Database='SES',
                    Trusted_Connection='yes')
                    cur = con.cursor()

                    storedProc = "exec Update_StudentDetails @AdmnNo = ?, @FName = ?, @LName = ?, @Class = ?" 
                    params = (int(AdmnNo.get()),FName.get(), LName.get(), ddClass.get()+ddDiv.get()) 
                    cur.execute(storedProc, params)
                    con.commit()
                    save_Img()
                    #---------------
                    


                    messagebox.showerror("Saved Successfully","Saved Successfully", parent = Stwindow) 
                except Exception as es:
                    messagebox.showerror("Error" , f"Error Due to : {str(es)}", parent = Stwindow)
                except IOError:
                    pass

                clearControls()
                    

      
    Stwindow=Tk()
    Stwindow.title('Student Registration Form')
    Stwindow.geometry('700x700')


    lblHeading=Label(Stwindow,text=" Student Registration Form",width=20,font=("bold",20))
    lblHeading.place(x=90,y=53)

    AdmnNo = StringVar()
    FName = StringVar()
    LName = StringVar()
    ddClass=StringVar()
    ddDiv=StringVar()

    global  house, gender
    house=IntVar(value=0)
    gender=IntVar(value=0)
   
    lblAdmNo=Label(Stwindow,text="Admission No.:",width=20,font=("bold",10))
    lblAdmNo.place(x=80,y=130)


    validation = Stwindow.register(only_numbers)
    entryAdmNo=Entry(Stwindow, width=40 , textvariable = AdmnNo, validate="key", validatecommand=(validation, '%S'))
    entryAdmNo.focus()
    entryAdmNo.place(x=240,y=130)

    img_LabelFrame = ttk.LabelFrame(Stwindow, text="")
    img_LabelFrame.place(x=490,y=90, width=200,height=160)


    lblFName=Label(Stwindow,text="First Name :",width=20,font=("bold",10))
    lblFName.place(x=80,y=180)

    
    entryFName=Entry(Stwindow, width=40 , textvariable = FName)
    entryFName.place(x=240,y=180)

    lblLName=Label(Stwindow,text="Last Name :",width=20,font=("bold",10))
    lblLName.place(x=80,y=240)

    entryLName=Entry(Stwindow, width=40 , textvariable = LName)
    entryLName.place(x=240,y=240)

    btn=Button(Stwindow, text='Upload Photo',width=15,bg='brown',fg='white', command = uploadImg).place(x=525,y=260)
    
    lblClass=Label(Stwindow,text="Class :",width=20,font=("bold",10))
    lblClass.place(x=80,y=290)


    classOptions=["6", "7","8", "9","10","11","12"]
    ddClass.set("Choose your class")
    dropclass=OptionMenu(Stwindow,ddClass,*classOptions)
    dropclass.pack()
    dropclass.place(x=240,y=290)

    lblDiv=Label(Stwindow,text="Division :",width=20,font=("bold",10))
    lblDiv.place(x=380,y=290)

    divOptions=["A", "B", "C","D", "E", "F"]
    ddDiv.set("Choose your Division")
    dropDiv=OptionMenu(Stwindow,ddDiv,*divOptions)
    dropDiv.pack()
    dropDiv.place(x=500,y=290)

    lblGender=Label(Stwindow,text="Gender",width=20,font=("bold",10))
    lblGender.place(x=80,y=340)
    Radiobutton(Stwindow, text="Male",padx = 5,value=1,variable=gender).place(x=235,y=340)
    Radiobutton(Stwindow, text="Female",padx = 5,value=2,variable=gender).place(x=335,y=340)

    lblHouse=Label(Stwindow,text="House",width=20,font=("bold",10))
    lblHouse.place(x=80,y=390)
    Radiobutton(Stwindow, text="Blue",padx = 5,value=1,variable=house).place(x=235,y=390)
    Radiobutton(Stwindow, text="Green",padx = 5,value=2,variable=house).place(x=335,y=390)
    Radiobutton(Stwindow, text="Red",padx = 5,value=3,variable=house).place(x=435,y=390)
    Radiobutton(Stwindow, text="Yellow",padx = 5,value=4,variable=house).place(x=535,y=390)

    btn=Button(Stwindow, text='Save',width=18,bg='brown',fg='white', command = SaveClick).place(x=180,y=450)
    btn=Button(Stwindow, text='Close',width=18,bg='brown',fg='white',command = CloseClick).place(x=330,y=450)

if __name__ == "__main__":
    StudentRegn()
