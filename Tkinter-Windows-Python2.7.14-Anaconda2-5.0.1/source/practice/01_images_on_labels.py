"""
	{
		"Python version": "Python 2.7.14 :: Anaconda, Inc.",
		"aim": "Tkinter GUI programming",
		"createdOn": "12 Feb 2018",
		"updatedOn": "12 Feb 2018",
		"codedBy": "Rishikesh Agrawani"
	}
"""
import Tkinter as tk 

try:
	root = tk.Tk()

	user_logo = tk.PhotoImage(file="..\\..\\images\\Mobile-Tap2.gif");
	img_label_wgt = tk.Label(image=user_logo);
	img_label_wgt.pack(side="left")

	text_label_wgt = tk.Label(root, text="Hey I know Python, JavaScript, Go. \
		\nWhat about you?\nI like Python and Go.");
	text_label_wgt.pack(side="right")

	root.mainloop(); 
except KeyboardInterrupt as err:
	print(err.args)
	print("You have terminated the GUI by using keyboard.")
