import sqlite3

connection = sqlite3.connect('store_movies.db')
cursor = connection.cursor()

#query the movie details (name, actor, actress, director, year of release) using a SELECT statement
print("Quering all records of the movies table\n")
cursor.execute("SELECT * FROM movies")
results = cursor.fetchall()
for i in range(len(results)):
    print(results[i])

print("\n\n")
print("Quering all movies of a particular Actor\n")
cursor.execute("SELECT * FROM movies WHERE lead_actor LIKE 'Aamir Khan'")
results = cursor.fetchall()
for i in range(len(results)):
    print(results[i])