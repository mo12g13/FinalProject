

import os
import requests
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_app.settings')
import django
django.setup()
from moviesuperfan.models import NowPlayingMovie



# You will need to get an API_KEY and set it as your environment variable to your API_KEY in order to make an API request to themoviedb.org
API_KEY = os.environ['API_KEY']

# Get number of pages of movies that are playing in USA from the themoviedb.org
def number_of_pages_of_movies_now_playing():

    url = "https://api.themoviedb.org/3/movie/now_playing?api_key={}&language=en-US&page=1&region=US".format(API_KEY)
    json_data = requests.get(url).json()
    pages = json_data['total_pages']
    return pages


# Get the list of movies that are playing in theaters in the USA
def list_of_movie_playing_urls():
    movies_playing_urls = list()
    for page_number in range(1, number_of_pages_of_movies_now_playing()+1):
        print("Page Number" + str(page_number))# For debugging purposes
        url = "https://api.themoviedb.org/3/movie/now_playing?api_key={}&language=en-US&page={}&region=US".format(API_KEY, page_number)
        movies_playing_urls.append(url)
    return movies_playing_urls

def movies_now_playing_data():
    movies_url = list_of_movie_playing_urls()
    for urls in movies_url:
        movies_playing_json = requests.get(urls).json()
        for i in range(len(movies_playing_json['results'])):
            movie_title = movies_playing_json['results'][i]['title']
            movie_db_id  = movies_playing_json['results'][i]['id']
            movie_overview = movies_playing_json['results'][i]['overview']
            movie_poster_url = "https://image.tmdb.org/t/p/w500"+ str(movies_playing_json['results'][i]['poster_path'])
            movie_release_date = movies_playing_json['results'][i]['release_date']
            print(movie_title, movie_db_id, movie_overview, movie_poster_url, movie_release_date)
            print()
            NowPlayingMovie.objects.get_or_create(movie_title=movie_title, movie_overview=movie_overview, movie_poster_url=movie_poster_url,movie_release_date=movie_release_date, movie_db_id=movie_db_id)

# Getting of the youtube. Movies are arranged differently so getting the youtube keys was difficult
# I have created this method to call it when a user wants to see detail information about a movie. I will pass the
# the movie id which will return the movie key for youtube if one exist.

def youtube_movie_trailer(movie_id):
    try:
        url = requests.get('http://api.themoviedb.org/3/movie/{}/videos?api_key={}'.format(movie_id, API_KEY))
        youtube_key = url.json()['results'][0]['key']
    except IndexError:
        youtube_key = None
        pass
    return youtube_key
if __name__=='__main__':
    movies_now_playing_data()
