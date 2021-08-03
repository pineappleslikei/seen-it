import requests
import json
from dotenv import load_dotenv
import os

from requests import api

load_dotenv()

BASE_URL = 'https://api.themoviedb.org/3'
AUTH = os.getenv('MOVIE_DB_API_KEY')


def get_movies(search_term):
    endpoint = '/search/movie'
    params = {
        'query': search_term,
        'api_key': AUTH,
    }
    response = requests.get(BASE_URL+endpoint, params=params).json()
    return response['results']


def get_movie_details(movie_id):
    endpoint = f'/movie/{movie_id}'
    params = {
        'api_key': AUTH,
    }
    response = requests.get(BASE_URL+endpoint, params=params).json()
    return response['results']
