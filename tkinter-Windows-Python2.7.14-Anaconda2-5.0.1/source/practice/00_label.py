"""
	{
		"Python version": "Python 2.7.14 :: Anaconda, Inc.",
		"aim": "Tkinter GUI programming",
		"createdOn": "12 Feb 2018",
		"updatedOn": "12 Feb 2018",
		"codedBy": "Rishikesh Agrawani"
	}
"""
import Tkinter as tk; 
# import tkinter as tk; # it also works on Python 2.7.14

root = tk.Tk();
label = tk.Label(root, text="Python");
label.pack();

root.mainloop();
