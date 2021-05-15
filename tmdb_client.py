import requests
import os

API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


base_url = "https://image.tmdb.org/t/p/"


def get_poster_url(poster_api_path, size="w185"):
    return f"{base_url}{size}/{poster_api_path}"


def get_backdrop_url(backdrop_api_path, size="w780"):
    return f"{base_url}{size}/{backdrop_api_path}"


def get_profile_url(profile_api_path, size="w185"):
    return f"{base_url}{size}/{profile_api_path}"
