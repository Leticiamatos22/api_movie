from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Movie, User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'copies']

