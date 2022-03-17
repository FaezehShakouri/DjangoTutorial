from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Favorite
from django.db import IntegrityError
from .forms import FavoriteForm, FavForm

def home(request):
    return render(request, 'user/home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html', {'form': UserCreationForm()})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                newuser = CustomUser(username=request.POST['username'], password=request.POST['password1'])
                newuser.save()
                return redirect('favorites', user_id=newuser.id)

            except IntegrityError:
                return render(request, 'user/signup.html', {'form': UserCreationForm(), 'error': 'This username has already been taken.'})

        else:
            return render(request, 'user/signup.html', {'form': UserCreationForm(), 'error': 'passwords didnt match'})


def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html', {'form': AuthenticationForm()})

    else:
        try:
            theuser = CustomUser.objects.get(username=request.POST['username'], password=request.POST['password'])
            if theuser is not None:
                return redirect('favorites', user_id=theuser.id)

        except:
            return render(request, 'user/login.html', {'form': AuthenticationForm(), 'error': 'Username or password is wrong!'})


def addFavorite(request, user_id):
    if request.method == 'GET':
        return render(request, 'user/addfavorite.html', {'form': FavForm()})

    else:
        user = CustomUser.objects.get(pk=user_id)
        user.favorites.add(request.POST['favs'])
        return redirect('favorites', user_id=user.id)


def favorites(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    queryset = user.favorites.all()
    
    data = {
        'queryset': queryset,
        'user': user
    }

    return render(request, 'user/favorites.html', {'data': data})

