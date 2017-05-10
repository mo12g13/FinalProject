from . models import UserMovie, NowPlayingMovie

# Get the total movies on that are now playing
def total_movies_now_playing():
    movies_count = NowPlayingMovie.objects.count()
    return movies_count

# The total amount of users movies reviews
def total_user_review():
    users_reviews_count = UserMovie.objects.filter('movie_review').count()
    return users_reviews_count
