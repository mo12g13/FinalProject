from django.conf.urls import url
from . import views

app_name = 'moviesuperfan'
urlpatterns = [
    url(r'^movieapp/register/$', views.register, name='register'),
    url(r'^movieapp/login/$', views.login_view, name="login_view"),
    url(r'^movieapp/blog/$', views.blog_view, name="blog_view"),
    url(r'^movieapp/movie/(?P<pk>\d+)$', views.movie_detail_view, name="detail_view"),



]
