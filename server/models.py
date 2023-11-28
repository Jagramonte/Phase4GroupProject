from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class User(db.Model,SerializerMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)

    #relationships 
    favoritemovies = db.relationship('FavoriteMovie', back_populates = 'user')


    #serialization rules

class FavoriteMovie(db.Model, SerializerMixin):
    __tablename__ = 'favoritemovies'

    movie_id = db.Column(db.Integer, primary_key = True)
    movie_name = db.Column(db.String)
    movie_details = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre_id'))


    #relationships 
    user = db.relationship('User', back_populates = 'favoritemovies')
    genre = db.relationship("Genre", back_populates = 'favoritemovies')



    #serialization rules

class Genre(db.Model, SerializerMixin):
    __tablename__ = 'genres'

    genre_id = db.Column(db.Integer, primary_key = True)
    genre_name = db.Column(db.String)

    #relationships
    favoritemovies = db.relationship('FavoriteMovie', back_populates = 'genre')


    #serlialization rules

