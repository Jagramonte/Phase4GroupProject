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

    #relationships 
    movies = db.relationship('Movie', back_populates = 'user')


    #serialization rules

class Movie(db.Model, SerializerMixin):
    __tablename__ = 'movies'

    movie_id = db.Column(db.Integer, primary_key = True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre_id'))
    movie_name = db.Column(db.String)
    movie_details = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'))


    #relationships 
    user = db.relationship('User', back_populates = 'movies')
    genre = db.relationship("Genre", back_populates = 'movies')



    #serialization rules

class Genre(db.Model, SerializerMixin):
    __tablename__ = 'genres'

    genre_id = db.Column(db.Integer, primary_key = True)
    genre_name = db.Column(db.String)

    #relationships
    movies = db.relationship('Movie', back_populates = 'genre')


    #serlialization rules
