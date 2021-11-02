# !/usr/bin/env python3
# Assignment Week 6 - Putting It All Together
# Author: Lyssette Williams

import sqlite3
from flask import g

def db_connect(dbfilename):
	con = sqlite3.connect(dbfilename)
	return con

def db_cursor(con):
	cur = con.cursor()
	return cur	

def view(cur,con):
	con.row_factory = sqlite3.Row
	cur.execute('SELECT * from students')
	rows = cur.fetchall()
	for row in rows:
		print(row)

def update(cur,con):
	List = [('Lyssette', '507 Santa Clara Ave','Alameda', '666')]
	cur.execute('INSERT INTO students VALUES (?,?,?)', List)
	print('Student has been added')
	con.commit()

#def search(nm,addr,city):
	#cur.execute('SELECT FROM students where (name, addr, city) VALUES =' nm, addr, city)
	#con.commit()

#def delete(cur,con):
	#cur.execute('DELETE FROM students WHERE name = ?', nm)
	#print('Student has been deleted.')
	#con.commit()


def main():
	dbfilename = 'roster.db'
	con = db_connect(dbfilename)
	cur = db_cursor(con)
	update(cur,con)
	view(cur,con)
	#db_update()
	#db_search()
	#db_delete()
	cur.close()
	con.close()

if __name__ == "__main__":
  main()	