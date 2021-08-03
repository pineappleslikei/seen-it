from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import movie_api as mov
import json

app = Flask(__name__)
CORS(app)
api = Api(app)


# sends real API call to the moviedb
class Movies(Resource):
    def get(self, search_term):
        external_results = mov.get_movies(search_term)
        return external_results


# return dummy data for working without network access
# class Movies(Resource):
#     def get(self, search_term):
#         with open('dummy.json') as dummy_data:
#             dummy_data_obj = json.load(dummy_data)
#         return dummy_data_obj


class A_Movie(Resource):
    def get(self, movie_id):
        external_results = mov.get_movie_details(movie_id)
        return external_results


api.add_resource(Movies, '/<search_term>')
api.add_resource(A_Movie, '/<movie_id>')


def add_json(json_data):
    with open('dummy.json', 'w') as json_output:
        json.dump(json_data, json_output, indent=3)


if __name__ == '__main__':
    app.run(debug=True)
