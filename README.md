# Movies from 2009-2020

Movies is a Flask web application the provide details of movies from 2009-2020. Data displayed in the web application is obtained from DANIEL GRIJALVA's movie industry database on Kaggle (https://www.kaggle.com/datasets/danielgrijalvas/movies?resource=download).

## Main features
There are six templates in the web application where three of them are main pages and three remaining are detail pages.
- Main pages
  - Movie page
    - showing all movies from 2009-2020 saved in the database
  - Rating System page
    - showing all ratings used in the database with system, definition and explanation of the rating
  - Genre page
    - showing all genre used in the database with the genre name and description.
- Detail pages
  - Movie detail page
    - By clicking a particular movie name on any web pages, details of the movie will be shown.
  - Rating movie page
    - By clicking a particular rating on movie page, rating page and genre movie page, details of the rating including system, definition and explanation will be shown along with all movies with that rating
  - Genre movie page
    - By clicking a particular genre on movie page, genre page and rating movie page, description of the genre will be shown along with all movies inside that genre

A horizontal navigation bar is showing in every web page allow users to navigate to the respective main pages.
Links are embedded into the data shown in the table columns movie title, rating and genre.

## Where to view
Web application link: https://cs551p-movie.onrender.com/

## Dependencies
behave==1.2.6

click==8.0.4

dataclasses==0.6

Faker==14.2.1

Flask==2.0.3

gunicorn==20.1.0

importlib-metadata==4.8.3

itsdangerous==2.0.1

Jinja2==3.0.3

MarkupSafe==2.0.1

parse==1.19.0

parse-type==0.6.0

python-dateutil==2.8.2

selenium==3.141.0

six==1.16.0

typing_extensions==4.1.1

urllib3==1.26.14

Werkzeug==2.0.3

zipp==3.6.0

## Running in virtual environment
pyenv install 3.7.9

python3 -m venv .venv

source .venv/bin/activate

pip install --upgrade pip

pip install flask

export FLASK_APP=movie.py

export FLASK_ENV=development

python3 -m flask run -h 0.0.0.0

## License
MIT License
Copyright (c) 2023 Cloudy030

## Documentation
Documentation is placed in the code's comments.

## Background
This is an assessment of course Advanced Programming (CS551P) for Master of Information Technology (MScIT) from University of Aberdeen (UoA).
It is required to develop a database-driven web application using Flask and deploy the developed website with Render.

This is a production of Ho Pok Nga in March 2023.
