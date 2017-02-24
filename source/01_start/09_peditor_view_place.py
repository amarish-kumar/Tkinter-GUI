#24 Feb 2017

from Tkinter import *
import tkFont

root = Tk()
root.attributes("-fullscreen",True)
root.title("BoomFox editor") 

#Creating font
tahoma30px_font = tkFont.Font(family="Tahoma",size=30)

#Horizontally aligning labels
lab_editor_menu = Label(text="File",font=tahoma30px_font,bg="#5b2497",fg="White") 
lab_editor_menu.place(x=0,y=0)

print lab_editor_menu.winfo_width()
print lab_editor_menu.winfo_height()

lab_editor_menu = Label(text="Edit",font=tahoma30px_font,bg="#0bd5cc",fg="White") 
lab_editor_menu.place(x=55,y=0)

lab_editor_menu = Label(text="View",font=tahoma30px_font,bg="#5b2497",fg="White") 
lab_editor_menu.place(x=114,y=0)

lab_editor_menu = Label(text="Tools",font=tahoma30px_font,bg="#928046",fg="White") 
lab_editor_menu.place(x=186,y=0)

lab_editor_menu = Label(text="Help",font=tahoma30px_font,bg="#5b2497",fg="White") 
lab_editor_menu.place(x=266,y=0)

root.mainloop()