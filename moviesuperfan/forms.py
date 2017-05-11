from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from . models import  UserMovie, UserProfile

# The user registration form for this website
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

# Creation of date selector for the user profile form. From stack overflow
class DateInput(forms.DateInput):
    input_type = 'date'

# User profile form
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('joined_date', 'user_profile_pic', 'about_user')
        widgets = {
            'joined_date': DateInput(),
        }

# The user movie form
class UserMovieForm(forms.ModelForm):
    class Meta:
        model = UserMovie
        fields = ('movie_watch', 'movie_review')

# The user login form
class LoginInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    # A method that authenticate username, password
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username').lower()
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user doesn't exist")

            if not user.check_password(password):
                raise ValidationError('Incorrect password entered')

            if not user.is_active:
                raise form.ValidationError('This user is no longer active in our system')

        return super(LoginInForm, self).clean(*args, **kwargs)
