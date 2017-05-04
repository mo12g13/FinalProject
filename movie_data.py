

import os
import requests
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_app.settings')
import django
django.setup()
from moviesuperfan.models import NowPlayingMovie



# You will have to get an API Key from themoviedb and set it as your environment variable
PASSWORD = os.environ['API_KEY']



# This method query themoviedb.org for movies that are now playing in theater
def load_now_playing_movies():
    first_movies_page = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key="+PASSWORD+"&language=en-US&page=1&region=US")
    # convert the response to a json object
    data_receive =first_movies_page.json()
    # Getting the number of movie pages from the json object and using it loop through the number of pages
    number_of_pages_receive = data_receive['total_pages']
    # When the number of pages is 10, the json object return is 9. Therefore, I have to add 1 in order to get the total number of pages
    for page_number in range(number_of_pages_receive+2):
        print("Page Number" + str(page_number))# For debugging purposes
        data_receive = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key="+PASSWORD+"&language=en-US&page="+str(page_number+1)+"+&region=US")
        data_receive = data_receive.json()
        for i in range(len(data_receive['results'])):
            movie_poster_url="https://image.tmdb.org/t/p/w500"+ str(data_receive['results'][i]['poster_path'])
            movie_overview = data_receive['results'][i]['overview']
            movie_title = data_receive['results'][i]['title']
            movie_release_date = data_receive['results'][i]['release_date']

            moving_playing = NowPlayingMovie.objects.get_or_create(movie_title=movie_title, movie_overview=movie_overview, movie_poster_url=movie_poster_url,movie_release_date=movie_release_date )


if __name__=='__main__':
    load_now_playing_movies()
