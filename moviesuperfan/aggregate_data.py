from . models import UserMovie, NowPlayingMovie
from django.db.models import Count

# Returns total numbers of moving that are now playing on this website
def total_movies_now_playing():
    movies_count = NowPlayingMovie.objects.count()
    return movies_count

# Returns total numbers of users movie reviews
def total_user_review():
    users_reviews_count = UserMovie.objects.filter(movie_watch=True).count()
    return users_reviews_count

# Returns the top five movies that are being watch on this website
def top_5_movies():
    top_5_watch_movies = UserMovie.objects.values('movie__movie_title').annotate(movie_review_count=Count('movie_review')).filter(movie_watch=True).order_by('-movie_review')[:5]
    return top_5_watch_movies

# Returns the total number of reviews for a particular user
def total_user_reviews(request):
    user_reviews_count = UserMovie.objects.all().values('movie_review').annotate(total=Count('movie_review')).filter(user=request.user).count()
    return user_reviews_count
