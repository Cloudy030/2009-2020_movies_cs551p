import csv
import sqlite3

# movie dataset from https://www.kaggle.com/datasets/danielgrijalvas/movies?resource=download
# with row number limitation, movies from 2009-2020 are extracted to be used
# rating movie data from https://www.filmratings.com/
# rating TV data from https://web.archive.org/web/20131215071047/http://transition.fcc.gov/vchip/ 
# genre data from https://www.masterclass.com/articles/how-to-identify-film-genres
# genre data from https://www.studiobinder.com/blog/movie-genres-list/
# genre data from https://www.nfi.edu/movie-genres/

conn=sqlite3.connect('movie.db')
cur=conn.cursor()

# drop all tables
conn.execute('DROP TABLE IF EXISTS movies')
conn.execute('DROP TABLE IF EXISTS rating')
conn.execute('DROP TABLE IF EXISTS genre')

print("table dropped successfully");

# create tables
conn.execute('CREATE TABLE rating (rating TEXT, system TEXT, definition TEXT, explaination TEXT)')
conn.execute('CREATE TABLE genre (genre TEXT, description TEXT)')
conn.execute('CREATE TABLE movies (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, rating TEXT, genre TEXT, year INTEGER, release_date_place TEXT, score TEXT, votes TEXT, director TEXT, writer TEXT, star TEXT, country TEXT, budget TEXT, gross TEXT, company TEXT, runtime TEXT, FOREIGN KEY (rating) REFERENCES rating(rating), FOREIGN KEY (genre) REFERENCES genre(genre))')

print("table created successfully");

# input rating data from csv
with open ('rating.csv', newline='') as f:
  reader = csv.reader(f,delimiter=",")
  next(reader) # not read first line
  for row in reader:
    print(row)
    
    rating=row[0]
    system=row[1]
    definition=row[2]
    explaination=row[3]

    cur.execute('INSERT INTO rating VALUES (?,?,?,?)',(rating, system, definition, explaination))
    conn.commit()
print("rating data parsed successfully");

# input genre data from csv
with open ('genre.csv', newline='') as f:
  reader = csv.reader(f,delimiter=",")
  next(reader) # not read first line
  for row in reader:
    print(row)
    
    genre=row[0]
    description=row[1]

    cur.execute('INSERT INTO genre VALUES (?,?)',(genre, description))
    conn.commit()
print("genre data parsed successfully");

# input movie data from csv
with open ('movies_edit.csv', newline='') as f:
  reader = csv.reader(f,delimiter=",")
  next(reader) # not read first line
  for row in reader:
    print(row)
    
    name=row[0]
    rating=row[1]
    genre=row[2]
    year=int(row[3])
    release_date_place=row[4]
    score=row[5]
    votes=row[6]
    director=row[7]
    writer=row[8]
    star=row[9]
    country=row[10]
    budget=row[11]
    gross=row[12]
    company=row[13]
    runtime=row[14]

    cur.execute('INSERT INTO movies VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(name, rating, genre, year, release_date_place, score, votes, director, writer, star, country, budget, gross, company, runtime))
    conn.commit()
print("movie data parsed successfully");

conn.close()

conn.close()