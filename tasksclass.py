#redo of task with classes
import sqlite3
import time
class tasks:
	def __init__(self):
#		self.ques=raw_input("new tasks?(ntask), completed a task?(comp), print tasks(ptask),delete a task?(d), view not completed tasks(nc), view completed tasks(c), add timer for task(t)???")
		self.conn=sqlite3.connect('task4.db');
		self.c=self.conn.cursor();
		self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (category text, task text, completed text(1), time decimal(6,2))''')

		self.conn.commit()

		
	def new_t(self,catn,taskn):
#		catn=raw_input('What is the category of your task?');
		#catn="j2"
#		taskn=raw_input('what is your task?')
#		taskn='j'
		compn='n';
		timen=0;
	 	self.c.execute('INSERT INTO tasks VALUES(?,?,?,?)', (catn, taskn,compn,timen))
		self.conn.commit();
		
	def p_t(self):
		self.c.execute('select * from tasks')
		self.table=[]
		rows=self.c.fetchall()
		for row in rows:
			self.table.append(t[1])
		return self.table

		
		
	def poop(self):
		print "poop"
#		print "task %s has been created" %catn
#		quest=self.ques
#		return quest
#	def run(self):
#		quest=self.ques
#		if quest=='n':
#			print "new task"
#		elif quest=='t':
##			print "time"
#		else:
#			print "ok"
##			


d=tasks()
d

#d.quest()
#d.run()
#d.ques


