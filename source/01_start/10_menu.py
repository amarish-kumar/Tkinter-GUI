#24 Feb 2017

from Tkinter import *
import tkFont
from os import system

root = Tk()
# root.attributes("-fullscreen",True)
root.title("BoomFox editor")
root.geometry("500x500")
#...........................
tahoma30px_font = tkFont.Font(family="Helvetica",size=15)

bfox_menubar = Menu(root,font=tahoma30px_font,fg="green")

bfox_filemenu = Menu(bfox_menubar,tearoff=0,font=tahoma30px_font) #Choices will be added starting at position 0 

def create():
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
	system("open https://msdn.microsoft.com/en-us/library/aa239193(v=vs.60).aspx")

def linux_help():
	system("open http://www.computerhope.com/issues/ch000773.htm")

bfox_filemenu.add_command(label="Create",command=create)
bfox_filemenu.add_command(label="Read",command=create)
bfox_filemenu.add_command(label="Update",command=create)
bfox_filemenu.add_command(label="Delete",command=create)
bfox_filemenu.add_separator()
bfox_filemenu.add_command(label="Close",command=create)
bfox_menubar.add_cascade(label="Crud",menu=bfox_filemenu)

bfox_finallymenu = Menu(bfox_menubar,tearoff=0)
bfox_finallymenu.add_command(label="Save",command=create)
bfox_finallymenu.add_command(label="Save as",command=create)
bfox_finallymenu.add_command(label="Rename",command=create)
bfox_finallymenu.add_separator()
bfox_finallymenu.add_command(label="Exit",command=create)
bfox_menubar.add_cascade(label="Finally",menu=bfox_finallymenu)

bfox_sendmenu = Menu(bfox_menubar,tearoff=0)
bfox_sendmenu.add_command(label="As mail",command=create)
bfox_sendmenu.add_command(label="Via bluetooth",command=create)
bfox_sendmenu.add_command(label="As text message",command=create)
bfox_menubar.add_cascade(label="Send",menu=bfox_sendmenu)

bfox_sharemenu = Menu(bfox_menubar,tearoff=0)
bfox_sharemenu.add_command(label="Google+",command=google_plus)
bfox_sharemenu.add_command(label="Facebook",command=facebook)
bfox_sharemenu.add_command(label="Linkedin",command=linkedin)
bfox_menubar.add_cascade(label="Share",menu=bfox_sharemenu)

bfox_helpmenu = Menu(bfox_menubar,tearoff=0)
bfox_helpmenu.add_command(label="Mac OS X",command=mac_help)
bfox_helpmenu.add_command(label="Windows",command=windows_help)
bfox_helpmenu.add_command(label="Linux",command=linux_help)
bfox_menubar.add_cascade(label="Help",menu=bfox_helpmenu) #Search box automatically comes for text 'Help' 

#..............
root.config(menu=bfox_menubar)
root.mainloop()