# !/usr/bin/env python3
# Assignment Week 3 - SQL Statements
# Author: Lyssette Williams

import sqlite3
import os
import logging

#importing sqlite3, os and logging. 

#debug logging config function
def debug_config():
	logging.basicConfig(level=logging.DEBUG,format = "[Movies]:%(asctime)s:%(levelname)s:%(message)s")  

#checking for database
def db_checkfile(dbfilename):
	if os.path.exists(dbfilename) and os.path.getsize(dbfilename) > 0:
		logging.debug("{a} found and not zero size".format(a=dbfilename))
	else:
		logging.error("{a} not found or zero size".format(a=dbfilename))

#connecting to and creating the database
def db_connect(dbfilename):
	con = sqlite3.connect(dbfilename)
	logging.debug("DB Connected".format())
	return con

#creating the cursor object
def db_cursor(con):
	cur = con.cursor()
	logging.debug('Cursor set'.format())
	return cur		

#creating both tables in database
def create_table(cur, con):
	cur.execute('PRAGMA foreign_keys = ON') #making sure foreign keys is on
	cur.execute('''CREATE TABLE IF NOT EXISTS movies_info_1 (show_id INTEGER AUTO_INCREMENT PRIMARY KEY, genre TEXT, title TEXT, director TEXT)''')
	con.commit()
	cur.execute('''CREATE TABLE IF NOT EXISTS movies_info_2 (show_id INTEGER, release_year NUMERIC, description TEXT, FOREIGN KEY(show_id) REFERENCES movies_info_1(show_id))''')
	con.commit()

#inserting data into table 1 - I considered doing all data entry in one function but found it easier to just turn on each function individually as I worked through debugging my own code
def data_entry_1(cur,con):
	List1 = [('1', 'Drama', 'The Fountain', 'Darren Aronofsky'), ('2', 'Sci Fi', 'Blade Runner', 'Ridley Scott'),('3','Biographical', 'Party Monster', 'Fenton Bailey and Randy Barbato')]
	cur.executemany('''INSERT INTO movies_info_1 VALUES(?,?,?,?)''', List1)
	con.commit()

#inserting data into table 2
def data_entry_2(cur, con):
	List2 = [('1','2006', 'As a modern-day scientist, Tommy is struggling with mortality, desperately searching for the medical breakthrough that will save the life of his cancer-stricken wife, Izzi.'),
			 ('2','1982', 'A blade runner must pursue and terminate four replicants who stole a ship in space, and have returned to Earth to find their creator.'),
			 ('3','2003', 'Based on the true story of Michael Alig, a Club Kid party organizer whose life was sent spiraling down when he bragged on television about killing his drug dealer and roommate. ')]	
	cur.executemany('''INSERT INTO movies_info_2 VALUES(?,?,?)''', List2)
	con.commit()		

#joining the two tables using primary key and foreign key, selecting results I want to display and then printing the results
def data_merge(cur):
	sql = '''SELECT movies_info_1.genre, movies_info_1.title, movies_info_1.director, movies_info_2.release_year, movies_info_2.description FROM movies_info_1 INNER JOIN movies_info_2 on movies_info_1.show_id = movies_info_2.show_id;'''
	cur.execute(sql)
	print('Genre       Title     Director    Year     Description')
	result = cur.fetchall()
	for row in result:
		print(row)
		print('\n')

#program name display and minor formatting
def display():
	print('Lyssette\'s Movie Database')
	print(' ')

#and now we run the whole thing and see what happens
def main():
	dbfilename = 'lyssettemoviedb.db'
	debug_config()
	db_checkfile(dbfilename)
	display()

	try:
		con = db_connect(dbfilename)
		cur = db_cursor(con)
		query = 'SELECT SQLITE_VERSION()'
		create_table(cur,con)
		data_entry_1(cur, con)
		data_entry_2(cur, con)
		data_merge(cur)
	except sqlite3.Error as error:
		logging.error('Error executing query ' + str(error))
	finally:
		if con:
			cur.close()
			con.close()
			logging.debug('[Info] DB Closed'.format())		

	print('  ')
	print('All Done!')
	logging.info("Completed")


if __name__ == "__main__":
  main() 
