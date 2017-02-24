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

but_name = Tkinter.Button(root,text="Name",command=show_name)
but_name.pack()

but_age = Tkinter.Button(root,text="Age",command=show_age)
but_age.pack()

but_prog_langs = Tkinter.Button(root,text="Programming languages",command=show_prog_langs)
but_prog_langs.pack()

but_table = Tkinter.Button(root,text="Show tables from 1 to 10",command=show_table)
but_table.pack()


def show_text():
	global txt_age
	print txt_age.get(1.0,Tkinter.END)  #0.0 will raise an error

but_show_text=Tkinter.Button(root,text='Show text', command=show_text)
but_show_text.pack()

	
v = Tkinter.StringVar()
lab_name = Tkinter.Label(root,text="Name",textvariable=v,relief=Tkinter.RAISED)
v.set("Do you like programming?")
lab_name.pack()

lab_age = Tkinter.Label(root,text="Age")
lab_age.pack()

txt_name = Tkinter.Text(root)
txt_name.pack()

txt_age = Tkinter.Text(root,height=20,width=20)
txt_age.pack()
#-----------------------------------

root.mainloop() #Entering the main event loop to take action against each event triggered by the user.
