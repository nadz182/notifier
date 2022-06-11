from plyer import notification
from tkinter import *
from PIL import Image, ImageTk
import time
from tkinter import messagebox
title = "Notifier"

t = Tk()
t.title(title)
t.configure(background='gray')
t.geometry("500x300")
img = Image.open(r"LOGO.png")
tkimage = ImageTk.PhotoImage(img)
img_label = Label(t, image=tkimage).grid()

def get_details():
    get_title = title.get()
    get_msg = message.get()
    get_time = time1.get()

    if get_msg == "" or get_time == "" or get_title =="":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time))
        sec = int_time * 60
        messagebox.showinfo("notifier set", "Set notification??")
        t.destroy()
        time.sleep(sec)
        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Notifier",
                            app_icon=r"icon2.ico",
                            timeout=10)


t_label = Label(t, text="Title to notify", font=("open sans",10, 'bold'),fg="#ffffff", bg='gray')
t_label.place(x=12, y=110)

title = Entry(t, width="25", font=("poppins",10))
title.place(x=123, y=110)

m_label = Label(t, text="Display message", font=("poppins",10, 'bold'),fg="#ffffff", bg='gray')
m_label.place(x=12, y=150)

message = Entry(t, width="25", font=("poppins",10))
message.place(x=123, y=150)

time_label = Label(t, text="Time", font=("poppins",10, 'bold'),fg="#ffffff", bg='gray')
time_label.place(x=12, y=190)

time1 = Entry(t, width="10", font=("poppins",10))
time1.place(x=123, y=190)

min_label = Label(t, text="min", font=("poppins",10, 'bold'),fg="#ffffff", bg='gray')
min_label.place(x=200, y=190)

but = Button(t, text="Set notification",font=("poppins",13, 'bold'),fg="#ffffff", bg="#FFDE59",
             width=20, relief="raised",
             command=get_details)
but.place(x=170, y=230)

t.resizable(0,0)
t.mainloop()