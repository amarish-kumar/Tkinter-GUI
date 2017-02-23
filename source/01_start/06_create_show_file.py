#!/usr/bin/python2.7
#23 Feb 2017

import Tkinter
import tkMessageBox

root = Tkinter.Tk() #Creating GUI aplication's main window
root.attributes("-fullscreen",True)

#------------ Widgets --------------
v = Tkinter.StringVar()
labName = Tkinter.Label(root,textvariable=v,relief=Tkinter.RAISED,padx=15,pady=5)
v.set("Filename")
labName.pack()

txtFilename = Tkinter.Text(root,height=1,width=100,bg="#d1c8c6",fg="#0000ff",pady=5)
txtFilename.pack()

labAge = Tkinter.Label(root,text="Content",relief=Tkinter.RAISED,padx=16,pady=5)
labAge.pack()

txtContent = Tkinter.Text(root,height=20,width=100,bg="#e7a496")
txtContent.pack()

def pwd():
	import os
	tkMessageBox.showinfo("Current directory's full path",os.getcwd())

butName = Tkinter.Button(root,text="Show Current path",command=pwd)
butName.pack()

def show_text():
	global txtContent
	print txtContent.get(1.0,Tkinter.END)  #0.0 will raise an error

def save():
	print "\n************************************************"
	global txtFilename
	filename=txtFilename.get(1.0,Tkinter.END).strip()
	if len(filename)!=0:
		print "Filename : ",filename 
		global txtContent
		content=txtContent.get(1.0,Tkinter.END)
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

	

butSave=Tkinter.Button(root,text='Save', command=save)
butSave.pack()

butShowText=Tkinter.Button(root,text='Show text', command=show_text)
butShowText.pack()

def show_file_content():
	global txtPath
	filepath = txtPath.get(1.0,Tkinter.END).strip() #strip() is required to remove newline from end
	print "Filepath : "+filepath
	import os
	if os.path.exists(filepath):
		if os.path.isfile(filepath):
			try:
				f = open(filepath,"r")
				l = f.readlines()
				print l
				content = ''.join(l)
				tkMessageBox.showinfo("Content of "+filepath,content)
			except:
				tkMessageBox("Error","Error while reading file.")
			finally:
				f.close()
		else:
			tkMessageBox.showinfo("Error","You only  need to specify the fullcd path path of file")
	else:
		tkMessageBox.showerror("Error","This is not a valid path or path does not exist.")

txtPath = Tkinter.Text(root,height=1,width=100,bg="#d1c8c6",fg="#0000ff",pady=5)
txtPath.insert(Tkinter.INSERT,"hello.py")
txtPath.pack()

butShowFile=Tkinter.Button(root,text='Show File Content', command=show_file_content)
butShowFile.pack()
#-----------------------------------

root.mainloop() #Entering the main event loop to take action against each event triggered by the user.
