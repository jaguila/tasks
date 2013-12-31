import Tkinter
from tasksclass import tasks

class tasksapp_tk(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()
		tasks()
	

	def initialize(self):
	#setup layout of grid	
		self.grid()
		#create widgets
		self.messageinit=Tkinter.Message(self,text="Welcome to the task app", relief=Tkinter.RAISED, width=100)
#		self.messageinit.grid(column=1, row=0, sticky='EW')
		self.messageinit.pack()
		
		
		#task list
		self.var1=Tkinter.StringVar()
		self.message1=Tkinter.Message(self,textvariable=self.var1, relief=Tkinter.RAISED, width=100)
#		self.message1.grid(column=2, row=2, sticky='EW')
		self.var1.set("tasks?")
		self.message1.pack()
		
		#entry
		#tasks.new_t(self.entry)
		self.entry=Tkinter.Entry(self)
		self.var2=Tkinter.StringVar()
#		self.entry.bind("<Return>",self.OnButtonClick1)
		self.entry.pack()

		
		#print entry

		self.message2=Tkinter.Message(self, width=10, text=self.entry.get())
		self.message2.pack()
		
		
		self.b=Tkinter.Button(self, text="get", width=10, command=self.OnButtonClick1)

		self.b.pack()
		
		self.resizable(True, True)

	def makemessage(self, **options):
		message=Tkinter.Message(self, **options)
		message.pack()
		return message
		
	def OnButtonClick1(self):
		new=self.makemessage(text=self.entry.get())
		return new


if __name__=="__main__":
	app=tasksapp_tk(None)
	app.title('task app')
	app.mainloop()
	