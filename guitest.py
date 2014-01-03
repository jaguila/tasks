import Tkinter
from tasksclass import tasks
import sqlite3

class tasksapp_tk(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		#must always initialize your imported classes first
		self.tasks=tasks()
		self.initialize()
		
	

	def initialize(self):
	#setup layout of grid	
		self.grid()
		#create widgets
		self.messageinit=Tkinter.Message(self,text="Welcome to the task app", relief=Tkinter.RAISED, width=100)
		self.messageinit.grid(column=0, row=0, sticky='EW')
#		self.messageinit.pack()
		
		
		#task list
		self.var1=Tkinter.StringVar()
		self.message1=Tkinter.Message(self,textvariable=self.var1, relief=Tkinter.RAISED, width=100)
		self.message1.grid(column=1, row=0, sticky='EW')
		self.var1.set("tasks?")
#		self.message1.pack()
		
		#entry
		#tasks.new_t(self.entry)
		self.label=Tkinter.Label(self, text="Task 1 Category")
		self.entry=Tkinter.Entry(self)
		self.var2=Tkinter.StringVar()
		self.label.grid(column=0, row=1, sticky='EW')
		self.entry.grid(column=1, row=1, sticky='EW')
#		self.entry.bind("<Return>",self.OnButtonClick1)
#		self.entry.pack()

		#fake button
		self.b=Tkinter.Button(self, text="get", width=10, command=self.OnButtonP)
		self.b.grid(column=0, row=4, sticky='EW')
	#	self.b.pack()		
		
		#entry2
		self.labelentry2=Tkinter.Label(self, text='Task 1')
		self.entry2=Tkinter.Entry(self)
		self.labelentry2.grid(column=0, row=2, sticky='EW')
		self.entry2.grid(column=1, row=2, sticky='EW')
		
		#self.entry2.pack()
		
		#submit button
		self.submit=Tkinter.Button(self, text='submit', width=10, command=self.OnButtonSubmit)
		self.submit.grid(column=3, row=3, sticky='EW')
		#self.submit.pack()
		#print entry

		#self.message2=Tkinter.Message(self, width=10, text=self.entry.get())
		#self.message2.grid(row=5, column=1, sticky='EW')	
		self.resizable(True, True)

	def makemessage(self, **options):
		message=Tkinter.Message(self, **options)
		message.pack()
		return message
		
	def OnButtonClick1(self):
		new=self.makemessage(text=self.entry.get())
		return new
	def OnButtonSubmit(self):		
		sub=self.tasks.new_t(self.entry.get(),self.entry2.get())
		return sub
	def OnButtonP(self):
		conn=sqlite3.connect('task4.db')
		conn.text_factory = str
		c=conn.cursor()
		c.execute('select rowid, category, task, completed, time from tasks')
		p=c.fetchall()
		i=5
		for row in p:
			n=self.makemessage(text=row)
			n.grid(column=0, row=i, sticky='EW')
			i=i+1
		print p
		return p
#	def listtable(self):
#		self.table=

if __name__=="__main__":
	app=tasksapp_tk(None)
	app.title('task app')
	app.mainloop()
	