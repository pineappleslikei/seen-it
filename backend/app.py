from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import movie_api as mov

app = Flask(__name__)
CORS(app)
api = Api(app)


class Movies(Resource):
    def get(self, search_term):
        external_results = mov.get_movies(search_term)
        return external_results


class Movie_Detail(Resource):
    def get(self, movie_id):
        external_results = mov.get_movie_details(movie_id)
        return external_results


api.add_resource(Movies, '/<search_term>')
api.add_resource(Movie_Detail, '/<movie_id>')

if __name__ == '__main__':
    app.run(debug=True)
