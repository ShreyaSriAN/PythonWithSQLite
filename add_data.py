import sqlite3

#define connection and cursor

connection = sqlite3.connect('store_movies.db')

cursor = connection.cursor()

m1 = "INSERT INTO movies VALUES ('URI', 'Vicky Kaushal', 'Yami Gautham', 2019,'Aditya Dhar')"
m2 = "INSERT INTO movies VALUES ('Kirik Party','Rakshith Shetty','Rashmika Mandanna',2016,'Rishab Shetty')"
m3 = "INSERT INTO movies VALUES ('Yeh Jawani hai Deewani','Ranbir Kapoor','Deepika Padukone',2013,'Ayan Mukherji')"
m4 = "INSERT INTO movies VALUES ('Taare Zameen Par','Aamir Khan','Tisca Chopra',2007,'Amole Gupte')"
m5 = "INSERT INTO movies VALUES ('PK','Aamir Khan','Anushka Sharma',2014,'Rajkumar Hirani')"
m6 = "INSERT INTO movies VALUES ('Lagaan','Aamir Khan','Gracy Singh',2001,'Ashutosh Gowariker')"
# m2 = "INSERT INTO movies VALUES ()"
# m2 = "INSERT INTO movies VALUES ()"
# m2 = "INSERT INTO movies VALUES ()"
# m2 = "INSERT INTO movies VALUES ()"
cursor.execute(m1)
cursor.execute(m2)
cursor.execute(m3)
cursor.execute(m4)
cursor.execute(m5)
cursor.execute(m6)
connection.commit()