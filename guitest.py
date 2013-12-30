from Tkinter import *

class tasksapp_tk(Tk):
	def __init__(self,parent):
		Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()

	def initialize(self):
	#setup layout of grid	
		self.grid()
		#create widgets
		self.varinit=StringVar()
		self.messageinit=Message(self,textvariable=self.varinit, relief=RAISED)
		self.messageinit.grid(column=0, row=0, sticky='EW')
		self.varinit.set=("Welcome to the task app")
		
		#task list
		self.var1=StringVar()
		self.message1=Message(self,textvariable=self.var1, relief=RAISED, width=10)
		self.message1.grid(column=0,row=1, sticky='EW')
		self.varinit.set=("tasks?")
		
		self.grid_columnconfigure(0,weight=1)

if __name__=="__main__":
	app=tasksapp_tk(None)
	app.title('task app')
	app.mainloop()
	