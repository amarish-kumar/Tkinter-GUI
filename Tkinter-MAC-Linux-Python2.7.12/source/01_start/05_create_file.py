#!/usr/bin/python2.7
#23 Feb 2017

import Tkinter
import tkMessageBox

root = Tkinter.Tk() #Creating GUI aplication's main window
root.attributes("-fullscreen",True)

#------------ Widgets --------------
v = Tkinter.StringVar()
lab_name = Tkinter.Label(root,textvariable=v,relief=Tkinter.RAISED,padx=15,pady=5)
v.set("Filename")
lab_name.pack()

txt_filename = Tkinter.Text(root,height=1,width=100,bg="#d1c8c6",fg="#0000ff",pady=5)
txt_filename.pack()

lab_age = Tkinter.Label(root,text="Content",relief=Tkinter.RAISED,padx=16,pady=5)
lab_age.pack()

txt_content = Tkinter.Text(root,height=20,width=100,bg="#e7a496")
txt_content.pack()

def pwd():
	import os
	tkMessageBox.showinfo("Current directory's full path",os.getcwd())

but_name = Tkinter.Button(root,text="Show Current path",command=pwd)
but_name.pack()

def show_text():
	global txt_content
	print txt_content.get(1.0,Tkinter.END)  #0.0 will raise an error

def save():
	print "\n************************************************"
	global txt_filename
	filename=txt_filename.get(1.0,Tkinter.END).strip()
	if len(filename)!=0:
		print "Filename : ",filename 
		global txt_content
		content=txt_content.get(1.0,Tkinter.END)
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

but_save=Tkinter.Button(root,text='Save', command=save)
but_save.pack()

but_show_text=Tkinter.Button(root,text='Show text', command=show_text)
but_show_text.pack()

#-----------------------------------

root.mainloop() #Entering the main event loop to take action against each event triggered by the user.
