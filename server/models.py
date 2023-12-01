from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class User(db.Model,SerializerMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    
    def __init__(self, username):
        self.username = username
    #relationships 
    movies = db.relationship('Movie', back_populates = 'user')


    #serialization rules
    serialization_rules = ('-movies')

class Movie(db.Model, SerializerMixin):
    __tablename__ = 'movies'

    movie_id = db.Column(db.Integer, primary_key = True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    movie_name = db.Column(db.String)
    movie_details = db.Column(db.String)
    img = db.Column(db.String)

    def __init__(self,genre_id, movie_name,movie_details,user_id,img):
        self.genre_id = genre_id
        self.movie_name = movie_name
        self.movie_details = movie_details
        self.user_id = user_id
        self.img = img


    #relationships 
    user = db.relationship('User', back_populates = 'movies')
    genre = db.relationship("Genre", back_populates = 'movies')



    #serialization rules
    serialization_rules = ('-user', 'genre')

class Genre(db.Model, SerializerMixin):
    __tablename__ = 'genres'

    genre_id = db.Column(db.Integer, primary_key = True)
    genre_name = db.Column(db.String)

    def __init__(self, genre_name):
        self.genre_name = genre_name

    #relationships
    movies = db.relationship('Movie', back_populates = 'genre')


    #serlialization rules
    serialization_rules = ('-movies')
