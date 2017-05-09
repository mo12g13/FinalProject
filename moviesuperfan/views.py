from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserProfileForm, LoginInForm, UserMovieForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from . models import NowPlayingMovie, UserProfile, UserMovie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

""" blog view  of this site. I am still working on this part of website.
I going am include comment section so that users can be able start discussion about a particular movie """
def movie_suggestion_view(request):
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
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(UserProfile, pk=user.pk)
    movies_watch = UserMovie.objects.filter(movie_watch=True)
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
        movies = paginator.page(paginator.num_pages)

    return render(request, 'profile/profile.html', {'user':user, 'profile':profile, 'movies': movies, 'movies_watch':movies_watch})

# This view displays detail information regarding a speciific movie a user wants to learn about
def movie_details_view(request, pk):
    movie_details = get_object_or_404(NowPlayingMovie, pk=pk)
    return render(request, 'moviesuperfan/movie_details.html', {'movie_details': movie_details})

# This views allow the user to mark a movie as watch and add a review of the movie
def add_movie_review(request, pk):
    user = user = get_object_or_404(User, pk=request.user.pk)
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
# def edit_review_of_movie(request):
#     movie_review =
