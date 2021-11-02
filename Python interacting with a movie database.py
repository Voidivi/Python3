# !/usr/bin/env python3
# Assignment Week 4 - Moar SQL!
# Author: Lyssette Williams

import sqlite3
#import os

#connecting to the database
def db_connect(dbfilename):
	con = sqlite3.connect(dbfilename)
	return con

#creating the cursor object
def db_cursor(con):
	cur = con.cursor()
	return cur	
#executing the deletion of Lawrence of Arabia from the database
def delete_movie(cur,con):
	cur.execute('DELETE FROM Movie WHERE movieID = 11')
	con.commit()

#updating the year of Toy Story's release
def change_year(cur,con):
	cur.execute('UPDATE Movie SET year = 1995 WHERE year = 1994')
	con.commit()	

#function houses display and some white space
def display():
	print('Welcome to the Movie Database!')
	print('  ')

#getting user input and then making sure that it's an integer and not a-z or special characters
#looping back asking for input if they give us input we don't want
#I got it done but I think it's ugly. Let me know if there is a nicer way of doing this!
def userquery():
	intuserinput = 0
	while intuserinput == 0:
		userinput = input('Please enter a year to lookup: ')
		print(' ')
		if len(userinput) > 4:
			print('Sorry, please try again.')
		else:	
			try:
				intuserinput = int(userinput)		
			except ValueError:
				print('Ooops! You must ONLY enter an integer.')
	return intuserinput		

#Joining the tables together and then printing the results or lack thereof
def get_data(cur,userinput,dbfilename):		
	sql = ('''SELECT movie.name, movie.year, movie.minutes,category.name from Movie INNER JOIN Category on movie.categoryID = category.categoryid WHERE year = ''' + str(userinput))
	cur.execute(sql)

	result = cur.fetchall()
	if len(result) > 0:
		print('Title   Year   Length   Genre')
		for row in result:
			print(row)
			print('\n')
	else:	
		print('Sorry, no movie in our database for ' + str(userinput))
		print(' ')			

#putting all the functions in main and also the program continuation
def main():
	display()
	dbfilename = 'dbmovies.sqlite'
	con = db_connect(dbfilename)
	cur = db_cursor(con)
	change_year(cur,con)
	delete_movie(cur,con)
	cont_progam = 'y'
	while cont_progam == 'y' or cont_progam == 'Y':
		userinput = userquery()
		get_data(cur,userinput,dbfilename)
		cont_progam = input('Look up another year? (y/n): ')
		print(' ')
	if con:
		cur.close()
		con.close()	
	print('Bye for now - see you at the movies!')

	
if __name__ == "__main__":
  main() 
