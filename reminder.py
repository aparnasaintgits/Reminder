import sqlite3
import subprocess as subpro   
import sys   
db=sqlite3.connect('newprjt.db')
cur=db.cursor()
def rem():
	print("\n\nReminder Application!\nOptions:\n  1 : Create table 'reminder'\n  2 : Add reminders\n  3 : View reminders\n  4 : Update reminder\n 5 : Exit")
	option = input('Enter the option : ')
	if option == '1':

		
		
		try:        
		    cur =db.cursor()
		    cur.execute('''CREATE TABLE remin (
		    ID INTEGER PRIMARY KEY AUTOINCREMENT,
		    Title TEXT (20) NOT NULL,
		    DateTime TEXT (20) NOT NULL);''')
		    print ('Reminder table created')
		except:
		    print ('Error')
		    db.rollback()
        rem() 
	elif option == '2':
		
		Title = input('\nEnter Subject : ')
	    DateTime = input('\nEnter reminder time in DD/MM/YYYY HH:MM:SS format : ')
		qry="insert into remin (Title, DateTime) values('"+Title+"', '"+DateTime+"');"
		try:
		    cur=db.cursor()
		    cur.execute(qry)
		    db.commit()
		    print ("\nReminder added ")
		except:
		    print ("\nOperation Failed!!!")
		    db.rollback()
		rem() 
	
	elif option == '3':
		
		print("\n")
		sql="SELECT * from remin;"
		cur=db.cursor()
		cur.execute(sql)
		flag=False
	    data=cur.fetchall()
		for x in data:
			flag = True
			print(x)
		if flag == False:
			print("\nNo Data found")
		
		rem() 
	elif option == '4':
		ID = input('\nEnter reminder Id : ')
		Title = input('\nEnter new reminder title : ')
		DateTime = input('\nEnter new reminder time in DD/MM/YYYY HH:MM:SS format : ')
		qry="update remin set Title=?,DateTime=? where ID=?;"
		try:
		    cur=db.cursor()
		    cur.execute(qry, (Title,DateTime,ID))
		    db.commit()

		    print("\nReminder updated ")
		except:
		    print("\nUpdation Error")
		    db.rollback()
	    rem()
	elif option == '5':
		db.close()
		print("Thank you for using our application")
		sys.exit()
	else:
		print("Failed")

rem() 
