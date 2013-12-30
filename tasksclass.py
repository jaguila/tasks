#redo of task with classes
import sqlite3
import time
class tasks:
	def __init__(self):
		self.ques=raw_input("new tasks?(ntask), completed a task?(comp), print tasks(ptask),delete a task?(d), view not completed tasks(nc), view completed tasks(c), add timer for task(t)???")
		conn=sqlite3.connect('task4.db');
		c=conn.cursor();
		c.execute('''CREATE TABLE IF NOT EXISTS tasks (category text, task text, completed text(1), time decimal(6,2))''')
		conn.commit()
	def new_t(self):
		catn=raw_input('What is the category of your task?');
		taskn=raw_input('what is your task?')
		compn='n';
		tasktime=0;
	#	c.execute(
	#	conn.commit();
		print "task %s has been created" %catn
		quest=self.ques
		return quest
	def run(self):
		quest=self.ques
		if quest=='n':
			print "new task"
		elif quest=='t':
			print "time"
		else:
			print "ok"
			
d=tasks()
#d.quest()
d.run()
#d.ques


