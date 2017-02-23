#!/usr/bin/python2.7
#23 Feb 2017

import Tkinter
import tkMessageBox

root = Tkinter.Tk() #Creating GUI aplication's main window

#------------ Widgets --------------
def show_name():
	print "My name is Rishikesh Agrawani."

def show_age():
	tkMessageBox.showinfo("I am 24.")

def show_prog_langs():
	prog_langs=["C","C++","Python","Goalng","Core java", "C#"]
	tkMessageBox.showinfo("Programming languages", "I like "+", ".join(prog_langs)) #Title,Message

def show_table():
	st=""
	for i in xrange(1,11):
		for j in xrange(1,11):
			print i*j,"\t",
			st+=str(i*j)+'\t'
		print "\n"
		st+='\n'
	tkMessageBox.showinfo("Table",st)

butName = Tkinter.Button(root,text="Name",command=show_name)
butName.pack()

butAge = Tkinter.Button(root,text="Age",command=show_age)
butAge.pack()

butProgLangs = Tkinter.Button(root,text="Programming languages",command=show_prog_langs)
butProgLangs.pack()

butTable = Tkinter.Button(root,text="Show tables from 1 to 10",command=show_table)
butTable.pack()


def show_text():
	global txtAge
	print txtAge.get(1.0,Tkinter.END)  #0.0 will raise an error

butShowText=Tkinter.Button(root,text='Show text', command=show_text)
butShowText.pack()

	
v = Tkinter.StringVar()
labName = Tkinter.Label(root,text="Name",textvariable=v,relief=Tkinter.RAISED)
v.set("Do you like programming?")
labName.pack()

labAge = Tkinter.Label(root,text="Age")
labAge.pack()

txtName = Tkinter.Text(root)
txtName.pack()

txtAge = Tkinter.Text(root,height=20,width=20)
txtAge.pack()
#-----------------------------------

root.mainloop() #Entering the main event loop to take action against each event triggered by the user.
