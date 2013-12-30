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
		self.varinit=Tkinter.StringVar()
		self.messageinit=Tkinter.Message(self,textvariable=self.varinit, relief=Tkinter.RAISED, width=100)
		self.messageinit.grid(column=0, row=1, sticky='EW')
		self.varinit.set("Welcome to the task app")
		
		
		#task list
		self.var1=Tkinter.StringVar()
		self.message1=Tkinter.Message(self,textvariable=self.var1, relief=Tkinter.RAISED, width=100)
		self.message1.grid(column=0, row=2, sticky='EW')
		self.var1.set("tasks?")
		
		#entry
		#tasks.new_t(self.entry)
		self.entry=Tkinter.Entry(self)
		self.entry.grid(column=0,row=3,sticky='EW')
		stuff=Tkinter.StringVar()
		
		stuff.set(self.entry.get)
		self.entry.bind("<Return>", self.OnButtonClick1(stuff))
		
		#self.OnButtonClick1()
		#tasks.new_t(stuff)
		#tasks.new_t(self.entry)
		
#		button = Tkinter.Button(self, text=u"Click me!", command=self.OnButtonClick1)
#		button.grid(column=2, row=3)
		
		
		self.grid_columnconfigure(0,weight=1)
		self.resizable(True, True)
	
	def OnButtonClick1(self, d):
		print str(d)

if __name__=="__main__":
	app=tasksapp_tk(None)
	app.title('task app')
	app.mainloop()
	