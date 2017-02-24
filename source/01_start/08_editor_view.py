from Tkinter import *
import tkFont

root = Tk()
root.attributes("-fullscreen",True)
#..................................

tahoma30px_font = tkFont.Font(family="Helvetica",size=30)

#Horizontally aligning labels
lab_editor_menu = Label(text="File",font=tahoma30px_font,bg="#5b2497",fg="White") 
lab_editor_menu.pack(side=LEFT)

lab_editor_menu = Label(text="Edit",font=tahoma30px_font,bg="#565466",fg="White") 
lab_editor_menu.pack(side=LEFT)

lab_editor_menu = Label(text="View",font=tahoma30px_font,bg="#5b2497",fg="White") 
lab_editor_menu.pack(side=LEFT)

lab_editor_menu = Label(text="Tools",font=tahoma30px_font,bg="#565466",fg="White") 
lab_editor_menu.pack(side=LEFT)

lab_editor_menu = Label(text="Help",font=tahoma30px_font,bg="#5b2497",fg="White") 
lab_editor_menu.pack(side=LEFT)

root.mainloop()