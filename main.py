from flask import Flask, render_template, request
import tmdb_client
import random

app = Flask(__name__)


# keys = list(tmdb_client.get_popular_movies())
# random.shuffle(keys)
# shuffled_movies = dict()
# for key in keys:
#     shuffled_movies.update({key: tmdb_client.get_popular_movies()[key]})
# movies = shuffled_movies["results"][:8]


@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    movies = tmdb_client.get_movies_list(list_type=selected_list)["results"][:8]
    return render_template("homepage.html", movies=movies, current_list=selected_list)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)[:12]
    return render_template("movie_details.html", movie=details, cast=cast)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.context_processor
def utility_processor_1():
    def tmdb_image_url(path, size):
        return tmdb_client.get_backdrop_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.context_processor
def utility_processor_2():
    def tmdb_image_url(path, size):
        return tmdb_client.get_profile_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


if __name__ == "__main__":
    app.run(debug=True)