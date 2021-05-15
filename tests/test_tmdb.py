import os

import requests

API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
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


# def test_get_poster_url_uses_default_size():
#     # Przygotowanie danych
#     poster_api_path = "some-poster-path"
#     expected_default_size = 'w185'
#     # Wywołanie kodu, który testujemy
#     poster_url = get_poster_url(poster_api_path=poster_api_path)
#     # Porównanie wyników
#     assert expected_default_size in poster_url
#
#
# def test_get_movies_list_type_popular():
#     movies_list = get_movies_list(list_type="popular")
#     assert movies_list is not None


from unittest.mock import Mock


def test_get_movies_list(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    response = requests_mock.return_value
    # Przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("requests.get", requests_mock)

    movies_list = get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list


def test_get_single_movie(monkeypatch):
    mock_single_movie = {"title": "Title", "tagline": "Tagline", "overview": "Overview", "budget": 1000000,
                         "genre": "Drama", "cast": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]}
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_single_movie
    monkeypatch.setattr("requests.get", requests_mock)

    single_movie = get_single_movie(movie_id=3)
    assert single_movie == mock_single_movie
