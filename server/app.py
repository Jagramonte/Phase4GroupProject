#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, make_response, jsonify, request
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from models import User, Movie, Genre 


# Local imports
from config import app, db, api
# Add your model imports


# Views go here!

   # GET endpoint for users
# class Users(Resource):
#     def get(self):
#         users = [user.to_dict() for user in User.query.all()]
#         return make_response(users,200)
    
# api.add_resource(Users,'/users')

    
   

# DELETE endpoint for users
# @app.route('/users/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     user = User.query.get(user_id)
#     if user:
#         db.session.delete(user)
#         db.session.commit()
#         return jsonify({'message': 'User deleted successfully'})
#     return jsonify({'message': 'User not found'}), 404

# # Similar GET and DELETE endpoints for FavoriteMovie and Genre

# # GET endpoint for favorite movies
class Movies(Resource):
    def get(self):
        movies = [movie.to_dict() for movie in Movie.query.all()]
        return make_response(movies,200)
    
api.add_resource(Movies,'/movies') 

class MoviesById(Resource):
    def delete(self,id):
        movie = Movie.query.get(id)
        if not movie:
            return make_response({'error':'movie not found'},404)
        try:
            db.session.delete(movie)
            db.session.commit()
        except:
            return make_response({'error':'something went wrong'},400)
        
api.add_resource(MoviesById,'/movies/<int:id>')



# # DELETE endpoint for favorite movies
# @app.route('/favoritemovies/<int:movie_id>', methods=['DELETE'])
# def delete_favorite_movie(movie_id):
#     movie = FavoriteMovie.query.get(movie_id)
#     if movie:
#         db.session.delete(movie)
#         db.session.commit()
#         return jsonify({'message': 'Favorite movie deleted successfully'})
#     return jsonify({'message': 'Favorite movie not found'}), 404

# # GET endpoint for genres
class Genres(Resource):
    def get(self):
        genres = [genre.to_dict() for genre in Genre.query.all()]
        return make_response(genres,200)
    
api.add_resource(Genres,'/genres')


# # DELETE endpoint for genres
# @app.route('/genres/<int:genre_id>', methods=['DELETE'])
# def delete_genre(genre_id):
#     genre = Genre.query.get(genre_id)
#     if genre:
#         db.session.delete(genre)
#         db.session.commit()
#         return jsonify({'message': 'Genre deleted successfully'})
#     return jsonify({'message': 'Genre not found'}), 404

@app.route('/')
def index():
    return '<h1>Project Server</h1>' 

if __name__ == '__main__':
    app.run(port=5555, debug=True)
