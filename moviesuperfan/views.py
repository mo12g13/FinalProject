from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserRegistrationForm, UserProfileForm, LoginInForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from . models import NowPlayingMovie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
import requests

import tmdbsimple as tmdb

import os


def index(request):
    return render(request, 'moviesuperfan/index.html')



def register(request):
    registered = False
    if request.method == "POST":
        profile_form = UserProfileForm(data=request.POST)
        user_form= UserRegistrationForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'user_profile_pic' in request.FILES:
                profile.user_profile_pic = request.FILES['user_profile_pic']

            profile.save()
            subject = "Thank for Registering"
            fname = user.first_name
            lname = user.last_name
            uname = user.username
            contact_message= """Dear {} {}
            Thank you very much for signing up on our movie web app website.
            This webapp is consider a home for movies lovers. Members interact in
            groups and decide what they would like to see in the comming week or weeks.
            We hope that you full advantage of having fun exploring the website. Furthermore,
            if you have inquiry or concerns, please don't hesitate to contact us.

            Lastly, your username is {}.

            Respectfully yours,
            Momo Johnson
            Website Administrator""".format(fname, lname, uname)
            to_email = user.email
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject,
            contact_message,
            from_email, [to_email],
            fail_silently=False)
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        profile_form = UserProfileForm()
        user_form = UserRegistrationForm()

    return render(request, 'registration/register.html',{'registered':registered,
     'profile_form': profile_form,
     'user_form': user_form})


def logout_view(request):
    username = request.user.get_username()
    response = logout(request)
    return render(request, 'registration/logout.html', {'username':username})

# login view of the user
def login_view(request):
    form = LoginInForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username').lower()
        print(username)
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'registration/login.html', {'form':form})


def blog_view(request):
    message = "You have be signed before you can view our blog post"
    movies_in_theater = NowPlayingMovie.objects.all().order_by('-movie_release_date')
    # Paginate page with 10 movies at a time
    paginator = Paginator(movies_in_theater, 10)
    # Current page of the movie
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except:
        message = "You have be signed before you can view our blog post"
        movies = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog.html', {'movies': movies, 'message':message} )
