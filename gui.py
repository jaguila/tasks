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
		self.entry.grid(column=0,row=0,sticky='EW')
		#bind certain keystrokes
		self.entry.bind("<Return>", self.OnPressEnter)
		self.entryVariable.set(u"Enter text here.")
		
		button = Tkinter.Button(self, text=u"Click me!", command=self.OnButtonClick)
		button.grid(column=1, row=0)
		
		#label, text alignment:anchor=left alightned, fg=foreground bg=background
		label = Tkinter.Label(self, anchor="w", fg="white", bg="blue")
		label.grid(column=0, row=1,columnspan=2,sticky='EW')
		self.labelVariable.set(u"Hello !")
		
		#will resize
		self.grid_columnconfigure(0,weight=1)
		#prevent vertical resizing
		self.resizable(True,False)
		
		
		
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
	
	
		