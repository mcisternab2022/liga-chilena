from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Equipo, Jugador, Tabla
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')

@login_required
def campeonato(request):
    posiciones = Tabla.objects.all().order_by('-puntos','-diferencia','-goles_favor')
    posicion = 1
    data = {
        'posicion':posicion,
        'posiciones': posiciones,
    }

    return render(request, 'campeonato.html', data)

@login_required
def estadisticas(request):
    jugadores = Jugador.objects.all()
    data = {
        'jugadores': jugadores,
    }

    return render(request, 'estadisticas.html', data)

@login_required
def equipos(request):
    return render(request, 'equipos.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('campeonato')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Este usuario ya existe '
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('campeonato')

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')
