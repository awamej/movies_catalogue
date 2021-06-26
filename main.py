from flask import Flask, render_template, request

import tmdb_client

app = Flask(__name__)

movies_list_types = ["now_playing", "popular", "top_rated", "upcoming"]


@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    if selected_list not in movies_list_types:
        selected_list = "popular"
    movies = tmdb_client.get_movies_list(list_type=selected_list)["results"][:8]
    return render_template("homepage.html", movies=movies, current_list=selected_list,
                           movies_list_types=movies_list_types)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)[:12]
    return render_template("movie_details.html", movie=details, cast=cast)


@app.context_processor
def utility_processor():
    return {
        "tmdb_image_url": tmdb_client.get_poster_url,
        "tmdb_backdrop_url": tmdb_client.get_backdrop_url,
        "tmdb_profile_url": tmdb_client.get_profile_url
    }


if __name__ == "__main__":
    app.run(debug=True)
