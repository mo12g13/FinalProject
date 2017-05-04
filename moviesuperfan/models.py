from django.db import models
from django.contrib.auth.models import User

# User is provided by Django. The email field is not unique by
# default, so add this to prevent more than one user with the same email.
User._meta.get_field('email')._unique = True

#Require email, first name and last name
User._meta.get_field('email')._blank = False
User._meta.get_field('last_name')._blank = False
User._meta.get_field('first_name')._blank = False

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joined_date = models.DateTimeField(blank=False)
    user_profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    about_user = models.TextField(blank=False)

    def __str__(self):
        return self.user.username

    def publish(self):
        joined_date = datetime.datetime.today()
        self.save()

class UserMovie(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_preview = models.FileField(blank=True)
    user_movies = models.ForeignKey('auth.User', blank=False)
    movie_rating = models.CharField(max_length=200, blank=False)
    movie_cover_photo = models.ImageField(upload_to='movie_app/media/')
    movie_watch = models.BooleanField()


class NowPlayingMovie(models.Model):
    movie_title = models.CharField(max_length=1000)
    movie_overview = models.CharField(max_length=1000)
    movie_poster_url = models.CharField(max_length=1000)
    movie_release_date = models.DateField()
    movie_db_id = models.IntegerField()
    youtube_trailer_key = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk) + " " + self.movie_title + " " + self.youtube_trailer_key

class Comments(models.Model):
    movie = models.ForeignKey(NowPlayingMovie, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment= models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
