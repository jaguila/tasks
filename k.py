from Tkinter import *

master = Tk()
e = Entry(master, width=50)
e.delete(0, END)
e.insert(0, "a default value")
e.focus_set()
e.pack()



text = e.get()
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry
	
def makemessage(parent, width=None, **options):
	message=Message(parent, **options)
#	if width:
#		entry.config(width=width)
	message.pack()
	return message

user = makeentry(master, "User name:", 10)
password = makeentry(master, "Password:", 10, show="*")
content = StringVar()
entry = Entry(master, text='duh', textvariable=content)

text = content.get()
content.set(text)

def callback():
#	new2=makeentry(master,e.get(),10)
#    print e.get()
	new3=makemessage(master,100, text=e.get())
	return new3

	


b = Button(master, text="get", width=10, command=callback)
b.pack()
new=makeentry(master, e.get(),10)
mainloop()