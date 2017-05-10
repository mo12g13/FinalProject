from django.db import models
from django.contrib.auth.models import User

# User is provided by Django. The email field is not unique by
# default, so add this to prevent more than one user with the same email.
User._meta.get_field('email')._unique = True
User._meta.get_field('username')._unique = True

#Require email, first name and last name
User._meta.get_field('email')._blank = False
User._meta.get_field('last_name')._blank = False
User._meta.get_field('first_name')._blank = False

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# This is the model for the user profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joined_date = models.DateTimeField(blank=False)
    user_profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    about_user = models.TextField(blank=False)

    def __str__(self):
        return self.user.username

# This the table for the user movies. It has relationship with the User and Movies Now Playing models
class UserMovie(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    movie= models.ForeignKey('NowPlayingMovie', on_delete=models.CASCADE)
    movie_watch = models.BooleanField()
    movie_review = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return str(self.movie)

# This is the table for the movies that are playing in theater in the USA
class NowPlayingMovie(models.Model):
    movie_title = models.CharField(max_length=1000)
    movie_overview = models.CharField(max_length=1000)
    movie_poster_url = models.CharField(max_length=1000)
    movie_release_date = models.DateField()
    movie_db_id = models.IntegerField()

    def __str__(self):
        return self.movie_title
