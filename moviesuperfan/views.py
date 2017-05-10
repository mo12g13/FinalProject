from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserProfileForm, LoginInForm, UserMovieForm
from django.contrib.auth.decorators import login_required
from . models import NowPlayingMovie, UserProfile, UserMovie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import aggregate_data


# index Home page of this website
def index(request):
    return render(request, 'moviesuperfan/index.html')


# The registration views for user of this website
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
            registered = True
            return redirect('moviesuperfan:login')

        else:
            print(user_form.errors, profile_form.errors)
    else:
        profile_form = UserProfileForm()
        user_form = UserRegistrationForm()

    return render(request, 'registration/register.html',{'registered':registered,
     'profile_form': profile_form,
     'user_form': user_form})

# The logout view for users of this website
def logout_view(request):
    user_full_name = request.user.get_full_name()
    response = logout(request)
    return render(request, 'registration/logout.html', {'user_full_name':user_full_name})


# login view for users of this website
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


def movie_suggestion_view(request):
    """ blog view  of this site. I am still working on this part of website.
    I going am include comment section so that users can be able start discussion about a particular movie """
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
        message = "You have be signed in before you can view our blog posts"
        movies = paginator.page(paginator.num_pages)
    return render(request, 'suggestion/movies_suggestion.html', {'movies': movies, 'message':message} )

@login_required
def user_profile(request, pk):
    # top 5 movies other are watching
    top_5_movies = aggregate_data.top_5_movies()
    # Total movies reviews
    total_users_reviews = aggregate_data.total_user_review()
    # Total movies on this movie site
    movie_count = aggregate_data.total_movies_now_playing()
    # A query that gets the total number of movies that a particular user have watched
    total_user_watch_movie = UserMovie.objects.filter(user=request.user).filter(movie_watch=True).count()
    user = get_object_or_404(User, pk=request.user.pk)
    profile = get_object_or_404(UserProfile, pk=request.user.pk)
    movies_watch = UserMovie.objects.filter(user=request.user).filter(movie_watch=True)
    movies_in_theater = NowPlayingMovie.objects.all().order_by('-movie_release_date')

    # Paginate page with 5 movies at a time
    paginator = Paginator(movies_in_theater, 5)
    # Current page of the movie
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except:
        movies = paginator.page(paginator.num_pages)

    context= {'user':user,
        'profile':profile, 'movies': movies,
        'movies_watch':movies_watch, 'movie_count':movie_count,
        'total_user_watch_movie': total_user_watch_movie,
        'total_users_reviews':total_users_reviews,
        'top_5_movies':top_5_movies,
    }

    return render(request, 'profile/profile.html', context=context)


# This view displays detail information regarding a speciific movie a user wants to learn about
@login_required
def movie_details_view(request, pk):
    movie_details = get_object_or_404(NowPlayingMovie, pk=pk)
    return render(request, 'moviesuperfan/movie_details.html', {'movie_details': movie_details})

# This views allow the user to mark a movie as watch and add a review of the movie
@login_required
def add_movie_review(request, pk):
    user = get_object_or_404(User, pk=request.user.pk)
    movie = get_object_or_404(NowPlayingMovie, pk=pk)
    movie_form = UserMovieForm(request.POST)
    if movie_form.is_valid():
        user_movie = movie_form.save(commit=False)
        user_movie.user = user
        user_movie.movie = movie
        user_movie.save()
        return redirect('index')
    else:
        movie_form = UserMovieForm()
        return render(request, 'moviesuperfan/movie_review.html', {'movie_form': movie_form})


# This view allows a user to edit review of a movie
@login_required
def edit_review_of_movie(request, pk):
    movie_review = get_object_or_404(UserMovie, pk=pk)
    movie_form = UserMovieForm(request.POST, instance=movie_review)
    if movie_form.is_valid():
        movie_review = movie_form.save(commit=False)
        movie_review.movie_watch=True
        movie_review.save()
        return redirect('index')
    else:
        movie_form = UserMovieForm(instance=movie_review)
        return render(request, 'moviesuperfan/movie_edit.html', {'movie_form': movie_form, 'movie_review':movie_review})

# This view deplays the review of a particular movie
def movie_review(request, pk):
    movie_review = get_object_or_404(UserMovie, pk=pk)
    return render(request, 'moviesuperfan/review_details.html', {'movie_review':movie_review})
