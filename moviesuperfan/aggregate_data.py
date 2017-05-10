from . models import UserMovie, NowPlayingMovie
from django.db.models import Count

# Get the total movies on that are now playing
def total_movies_now_playing():
    movies_count = NowPlayingMovie.objects.count()
    return movies_count

# The total amount of users movies reviews
def total_user_review():
    users_reviews_count = UserMovie.objects.filter(movie_watch=True).count()
    return users_reviews_count


def top_5_movies():
    top_5_watch_movies = UserMovie.objects.values('movie__movie_title').annotate(movie_review_count=Count('movie_review')).filter(movie_watch=True).order_by('-movie_review')[:6]
    print(top_5_watch_movies[0])
    return top_5_watch_movies
