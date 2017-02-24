from Tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.attributes("-fullscreen",True)

# img = Image.open("./Book.png")
photo = ImageTk.PhotoImage(file="../../images/fireworks.gif")
photo2 = ImageTk.PhotoImage(file="../../images/PocketCube.gif")

txt_name = Text(root,height=200,width=200)
txt_name.insert(END,"\n")
txt_name.image_create(END,image=photo)
txt_name.pack(side=LEFT)

# txt_name2 = Text(root,height=200,width=200)
# txt_name2.image_create(END,image=photo2)
# txt_name2.pack(side=RIGHT)
# lab_name = Label(root,text="Greatness is an identification of Great man",image=photo2)
# lab_name.pack(side=RIGHT)

root.mainloop()