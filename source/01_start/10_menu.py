#24 Feb 2017

from Tkinter import *
import tkFont
import tkMessageBox
from os import system
from PIL import Image, ImageTk

root = Tk()
# root.attributes("-fullscreen",True)
root.title("BoomFox editor")
root.geometry("500x600")
#...........................
helvetica15px_font = tkFont.Font(family="Helvetica",size=15)

helvetica20px_font = tkFont.Font(family="Helvetica",size=20,weight="bold")

bfox_menubar = Menu(root,font=helvetica15px_font,fg="green")

bfox_filemenu = Menu(bfox_menubar,tearoff=0,font=helvetica15px_font) #Choices will be added starting at position 0 

v = StringVar()
# img = Image.open("Book.png")
# photo = ImageTk.PhotoImage(img)
lab_name = Label(root,textvariable=v,padx=15,pady=5,font=helvetica20px_font,fg="#194F30")
v.set("Filename")
# lab_name.pack()


txt_filename = Text(root, height=1,width=150,bg="#e7a496",pady=10,font=helvetica15px_font)
# txt_filename.pack()

lab_content = Label(root,text="Content",padx=15,pady=5,font=helvetica20px_font,fg="#194F30")#relief=RAISED
# lab_content.pack()

txt_content = Text(root,width=150,bg="#e7a496",font=helvetica15px_font)

def save():
	print "\n************************************************"
	global txt_filename
	filename=txt_filename.get(1.0,END).strip()
	if len(filename)!=0:
		print "Filename : ",filename 
		global txt_content
		content=txt_content.get(1.0,END)
		print "Content : ",content
		print "\n************************************************"
		try:
			f = open(filename,"w")
			f.write(content) #0.0 will raise an error
			tkMessageBox.showinfo( "Success",filename.strip()+" successfully created.")

		except:
			tkMessageBox.showinfo("Error","Error while creating file")
		finally:
			f.close()
	else:
		tkMessageBox.showinfo("Error","Filename should not be empty.")
		return

but_save=Button(root,text='Save', command=save)
# but_save.pack()

def create():
	global txt_content
	global txt_filename
	global lab_name
	global lab_content
	global but_save

	lab_name.pack()
	txt_filename.pack()
	lab_content.pack()
	txt_content.pack()
	but_save.pack()


def test():
	print "Enjoy Boomfox(Zoomlines)"

def facebook():
	print "Opening facebook in browser"
	system("open https://www.facebook.com/")

def linkedin():
	print "Opening linkedin in browser"
	system("open https://www.linkedin.com/")

def google_plus():
	print "Opening linkedin in browser"
	system("open https://plus.google.com/")

def mac_help():
	system("open https://www.tekrevue.com/tip/textedit-plain-text-mode/")

def windows_help():
	system("open http://superuser.com/questions/573342/open-a-file-with-text-editor")

def linux_help():
	system("open http://www.computerhope.com/issues/ch000773.htm")

"""Submenus"""
bfox_create_submenu = Menu(bfox_filemenu)
bfox_create_submenu.add_command(label="File",command=create)
bfox_create_submenu.add_command(label="Directory",command=test)

"""Menuitems"""
# bfox_filemenu.add_command(label="Create",command=test)
bfox_filemenu.add_cascade(label="Create",menu=bfox_create_submenu)
bfox_filemenu.add_command(label="Read",command=test)
bfox_filemenu.add_command(label="Update",command=test)
bfox_filemenu.add_command(label="Delete",command=test)
bfox_filemenu.add_separator()
bfox_filemenu.add_command(label="Close",command=test)
bfox_menubar.add_cascade(label="Crud",menu=bfox_filemenu)

bfox_finallymenu = Menu(bfox_menubar,tearoff=0)
bfox_finallymenu.add_command(label="Open",command=test)
bfox_finallymenu.add_command(label="Save",command=save)
bfox_finallymenu.add_command(label="Save as",command=test)
bfox_finallymenu.add_command(label="Rename",command=test)
bfox_finallymenu.add_separator()
bfox_finallymenu.add_command(label="Exit",command=test)
bfox_menubar.add_cascade(label="Finally",menu=bfox_finallymenu)

bfox_sendmenu = Menu(bfox_menubar,tearoff=0)
bfox_sendmenu.add_command(label="As mail",command=test)
bfox_sendmenu.add_command(label="Via bluetooth",command=test)
bfox_sendmenu.add_command(label="As text message",command=test)
bfox_menubar.add_cascade(label="Send",menu=bfox_sendmenu)

bfox_sharemenu = Menu(bfox_menubar,tearoff=0)
bfox_sharemenu.add_command(label="Google+",command=google_plus)
bfox_sharemenu.add_command(label="Facebook",command=facebook)
bfox_sharemenu.bind("Control-f",facebook)
bfox_sharemenu.add_command(label="Linkedin",command=linkedin)
bfox_sharemenu.bind("Control-l",linkedin)
bfox_menubar.add_cascade(label="Share",menu=bfox_sharemenu)

bfox_helpmenu = Menu(bfox_menubar,tearoff=0)
bfox_helpmenu.add_command(label="Mac OS X",command=mac_help)
bfox_helpmenu.add_command(label="Windows",command=windows_help)
bfox_helpmenu.add_command(label="Linux",command=linux_help)
bfox_menubar.add_cascade(label="Help",menu=bfox_helpmenu) #Search box automatically comes for text 'Help' 

#..............
root.config(menu=bfox_menubar)
root.mainloop()