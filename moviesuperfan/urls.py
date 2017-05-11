from django.conf.urls import url
from . import views

app_name = 'moviesuperfan'
urlpatterns = [
    url(r'^movieapp/register/$', views.register, name='register'),
    url(r'^movieapp/login/$', views.login_view, name="login_view"),
    url(r'^movieapp/movie/blog/$', views.blog_view, name="blog_view"),
    url(r'^movieapp/movie/details/(?P<pk>\d+)/$', views.movie_details_view, name="movie_details_view"),
    url(r'^movieapp/user/profile/(?P<pk>\d+)/$', views.user_profile, name="user_profile"),
    url(r'^movieapp/movie/review/(?P<pk>\d+)/$', views.add_movie_review, name='add_movie_review'),
    url(r'^movieapp/movie/review/edit/(?P<pk>\d+)/$', views.edit_review_of_movie, name='edit_review_of_movie'),
    url(r'^movieapp/movie/review/detail/(?P<pk>\d+)/$', views.movie_review, name='movie_review'),
]
