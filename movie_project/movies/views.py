from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import MovieForm, RegisterForm, LoginForm
from .models import Movie

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'movies/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'movies/login.html', {'form': form})

@login_required
def home_view(request):
    movies = Movie.objects.filter(user=request.user)
    return render(request, 'movies/home.html', {'movies': movies})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def add_movie_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('home')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após logout