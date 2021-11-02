# !/usr/bin/env python3
# Assignment Week 5 - Data Visualization
# Author: Lyssette Williams

import sqlite3
import os
import matplotlib.pyplot as plt 
import numpy as np 
import logging

#debug logging config function
def debug_config():
	logging.basicConfig(level=logging.DEBUG,format = "[degrees2]:%(asctime)s:%(levelname)s:%(message)s")  

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

#Function for selecting data for graph - Education
def Education_data(cur,con):
	cur.execute('SELECT year, Education from degrees')
	return	fetch_data(cur,con)

#Function for selecting data for graph - Health Professionals	
def HP_data(cur,con):
	cur.execute('SELECT year, HealthProfessions from degrees')
	return fetch_data(cur,con)

#Function for selecting data for graph - Engineering
def Engineering(cur,con):
	cur.execute('SELECT year, Engineering from degrees')
	return fetch_data(cur,con)	

#Function for selecting data for graph - Computer Science
def ComputerSci(cur,con):
	cur.execute('SELECT year, ComputerScience from degrees')
	return fetch_data(cur,con) 	

#parameterized fetching the data and plugging it into dictionaries
def fetch_data(cur,con):
	data = cur.fetchall()
	x1 = [] #years
	y1 = [] #grads
	for row in data:
		x1.append(row[0])
		y1.append(row[1])
	return	x1,y1

#finally actually plotting the graph
#I originally was 'overengineering' this 
#Definitely jumped up with arms raised when everything worked
def print_graph(x1,x2,x3,x4,y1,y2,y3,y4):
	plt.plot(x1,y1,'-', label='HealthProfessions')
	plt.plot(x2,y2,'-', label='Education')
	plt.plot(x3,y3,'-',label = 'ComputerScience')
	plt.plot(x4,y4,'-', label='Engineering')
	plt.ylabel('Degrees')
	plt.xlabel('Year')
	plt.title("% of Bachelor\'s degrees for USA major (1970-2011)\n  Degrees Over Time")
	plt.legend()
	plt.show()

#Placing it all in main - including all the debugs, configs, log, printing the graph
def main():
	dbfilename = 'degrees2.db'
	debug_config()
	db_checkfile(dbfilename)
	try:
		con = db_connect(dbfilename)
		cur = db_cursor(con)
		x1,y1 = HP_data(cur,con)
		x2,y2 = Education_data(cur,con)
		x3,y3 = ComputerSci(cur,con)
		x4,y4 = Engineering(cur,con)
		print_graph(x1,x2,x3,x4,y1,y2,y3,y4)
	except sqlite3.Error as error:
		logging.error("Error executing query", error)
	finally:
		if con:
			con.close()
			logging.debug("[Info] DB Closed".format())

	print('Done - check completed')
	logging.info("Completed.")

if __name__ == "__main__":
  main() 			