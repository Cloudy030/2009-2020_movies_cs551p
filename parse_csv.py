import csv
import sqlite3

conn.sqlite.connect('movie.db')
cur=conn.cursor()

conn.execute('DROP TABLE IF EXISTS movies')
print("table dropped successfully");

conn.execute('CREATE TABLE movies ()')
print("table created successfully")

# movie dataset from https://www.kaggle.com/datasets/danielgrijalvas/movies?resource=download