#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter




#start of app
class simpleapp_tk(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()

#creates all the gui elements. pass does nothing
	def initialize(self):
#sets up layout
		self.grid()
		
		
		self.entryVariable = Tkinter.StringVar()
		#create widget then add it to layout manager(grid)
		self.entry=Tkinter.Entry(self,textvariable=self.entryVariable)
		#sticky is saying wheree it goes EW=east west
		self.entry.grid(column=0,row=2,sticky='EW')
		#bind certain keystrokes
		self.entry.bind("<Return>", self.OnPressEnter)
		self.entryVariable.set(u"Enter text here.")
		
		#test 2nd entry
		self.entry2=Tkinter.Entry(self)
		self.entry2.grid(column=0,row=3,sticky='EW')
		#bind certain keystrokes
		self.entry2.bind("<Return>", self.OnPressEnter)
		
		#prefilled entry
		self.text = Tkinter.Text(self, width=10, height=1)
		self.text.grid(column=0, row=1, sticky='EW')
		#text
		self.text.insert(Tkinter.INSERT, "task app")
		self.text.insert(Tkinter.END, "Dne")
		#self.text.pack()
		self.text.bind("<Return>", self.OnPressEnter)
		
		#message
		self.var=Tkinter.StringVar()
		self.label=Tkinter.Message(self, textvariable=self.var, relief=Tkinter.RAISED)
		self.label.grid(column=0, row=0, sticky='EW')
		self.var.set("Hey!? Hw are yu doing?")
		#self.label.pack()
		
		button = Tkinter.Button(self, text=u"Click me!", command=self.OnButtonClick)
		button.grid(column=1, row=0)
		
		#label, text alignment:anchor=left alightned, fg=foreground bg=background
<<<<<<< HEAD
		#label = Tkinter.Label(self, anchor="w", fg="white", bg="blue")
		label = Tkinter.Label(self, fg="white", bg="blue")
		label.grid(column=0, row=10,columnspan=2,sticky='EW')
=======
		label = Tkinter.Label(self, anchor="w", fg="white", bg="blue")
		label.grid(column=0, row=1,columnspan=2,sticky='EW')
		self.labelVariable.set(u"Hello !")
>>>>>>> a739b8726ada205aed71bc63e081b80d705955c6
		
		#will resize
		self.grid_columnconfigure(0,weight=1)
		#prevent vertical resizing
<<<<<<< HEAD
		self.resizable(True,True)
		#self.dialog=Pmw.SelectionDialog(self, title)
=======
		self.resizable(True,False)
		
>>>>>>> a739b8726ada205aed71bc63e081b80d705955c6
		
		
	def OnButtonClick(self):
		self.labelVariable.set( self.entryVariable.get()+" (Youclicked the button)" )
		#print "You clicked the button!"
		
	def OnPressEnter(self,event):
		self.labelVariable.set( self.entryVariable.get()+" (You pressed Enter)" )
		print "You pressed enter !"

#this __name__ is a variable that gets assigned as a default to the __main__ 
#if the file this is in is being run directly. Else will be the name of the module that ran it.
		
if __name__ =="__main__":
	app = simpleapp_tk(None)
	app.title('myapplication')
	#tells the program to loop until something happens)
	app.mainloop()
	
	
		