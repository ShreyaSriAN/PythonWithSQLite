import sqlite3

#define connection and cursor

connection = sqlite3.connect('store_movies.db')

cursor = connection.cursor()

#create movies table

command = "CREATE TABLE IF NOT EXISTS movies(movie_name TEXT, lead_actor TEXT, actress TEXT, YearOfRelease INTEGER, Director TEXT)"

cursor.execute(command)


