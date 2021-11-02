# !/usr/bin/env python3
# Assignment Week 1 - Intro to Databases
# Author: Lyssette Williams

#import at top of file
import sqlite3

#connecting to the db 
con = sqlite3.connect('chinook.db')
cur = con.cursor()  #creating the cursor object

#display the title and also adding some whitespace
def display():
	print('Musical Artist List')
	print('  ')


def main():
	display()
	#query to select all the elements from the  table
	query = '''SELECT * FROM artists'''
	#run the query
	cur.execute(query)
	#save the results in artists
	artists = cur.fetchall()
	#loop through and print all the artists
	for artist in artists:
		print(artist[1])
	#closing the file	
	if con:
		con.close()
	print('  ') #a bit of white space
	print('Done - See you next time!') #and letting the user know it's over!



if __name__ == "__main__":
  main() 

