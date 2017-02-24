from Tkinter import *
import tkFont

root = Tk()
root.attributes("-fullscreen",True)
#..................................

lab_city = Label(root, text="City")	#City
lab_city.pack()

helvetica20px_font = tkFont.Font(family="Helvetica",size=20)
lab_state = Label(root, text="State",font=helvetica20px_font,bg="navy",fg="white")	#State
lab_state.pack()

tahoma30px_font = tkFont.Font(family="Helvetica",size=30)
lab_country = Label(root, text="Country",font=tahoma30px_font,fg="#0000ff",bg="pink")	#State
lab_country.pack()

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
#..............
root.mainloop()



