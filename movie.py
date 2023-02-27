import sqlite3
from flask import Flask, render_template

app=Flask(__name__)

db_name='data/movie.db'

@app.route('/')
def index():
  conn = sqlite3.connect(db_name)
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute('select name, rating, genre, year, score from movies')
  rows = cur.fetchall()
  print(rows)
  conn.close()
  return render_template('index.html', rows = rows)

@app.route('/movie_detail/<name>')
def movie_detail(name):
  conn = sqlite3.connect(db_name)
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute('select * from movies WHERE name=?', [name])
  rows = cur.fetchall()
  print(rows)
  conn.close()
  return render_template('movie_detail.html', rows = rows)

@app.route('/rating')
def rating():
  conn = sqlite3.connect(db_name)
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute('select * from rating')
  rows = cur.fetchall()
  print(rows)
  conn.close()
  return render_template('rating.html', rows = rows)

@app.route('/rating_movie/<rating>')
def rating_movie(rating):
  conn = sqlite3.connect(db_name)
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  # cur.execute('select rating from rating WHERE rating=?', [rating])
  cur.execute('select * from movies WHERE rating=?', [rating])
  rows = cur.fetchall()
  print(rows)
  conn.close()
  return render_template('rating_movie.html', rows = rows)

@app.route('/genre')
def genre():
  conn = sqlite3.connect(db_name)
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute('select * from genre')
  rows = cur.fetchall()
  print(rows)
  conn.close()
  return render_template('genre.html', rows = rows)