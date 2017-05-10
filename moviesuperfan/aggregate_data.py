from . models import UserMovie, NowPlayingMovie

# Get the total movies on that are now playing
def total_movies_now_playing():
    movies_count = NowPlayingMovie.objects.count()
    return movies_count
