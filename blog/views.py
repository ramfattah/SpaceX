from django.shortcuts import render
import requests



def home(request):
    
    url = 'https://api.spacexdata.com/v3/info'
    comp_info = requests.get(url).json()

    context = {
        'info':comp_info
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')


def capsule(request):
    
    url = 'https://api.spacexdata.com/v3/capsules'
    info = requests.get(url).json()

    context = {
        'cap':info
    }

    return render(request, 'blog/capsule.html', context)

def core(request):
    
    url = 'https://api.spacexdata.com/v3/cores'
    info = requests.get(url).json()

    context = {
        'core':info
    }

    return render(request, 'blog/core.html', context)



def dragon(request):
    
    url = 'https://api.spacexdata.com/v3/dragons'
    info = requests.get(url).json()

    context = {
        'dra':info
    }

    return render(request, 'blog/dragon.html', context)

def history(request):
    
    url = 'https://api.spacexdata.com/v3/history'
    info = requests.get(url).json()

    context = {
        'his':info
    }

    return render(request, 'blog/history.html', context)

def landing_pads(request):
    
    url = 'https://api.spacexdata.com/v3/landpads'
    info = requests.get(url).json()

    context = {
        'lan':info
    }

    return render(request, 'blog/landing.html', context)

    
def launch(request):
    
    url = 'https://api.spacexdata.com/v3/launches'
    info = requests.get(url).json()

    context = {
        'laun':info
    }

    return render(request, 'blog/launch.html', context)

    
def mission(request):
    
    url = 'https://api.spacexdata.com/v3/missions'
    info = requests.get(url).json()

    context = {
        'mis':info
    }

    return render(request, 'blog/mission.html', context)

    
def payload(request):
    
    url = 'https://api.spacexdata.com/v3/payloads'
    info = requests.get(url).json()

    context = {
        'pay':info
    }

    return render(request, 'blog/payload.html', context)

def rocket(request):
    
    url = 'https://api.spacexdata.com/v3/rockets'
    info = requests.get(url).json()

    context = {
        'roc':info
    }

    return render(request, 'blog/rocket.html', context)

def roadster(request):
    
    url = 'https://api.spacexdata.com/v3/roadster'
    info = requests.get(url).json()

    context = {
        'road':info
    }

    return render(request, 'blog/roadster.html', context)

    
def ship(request):
    
    url = 'https://api.spacexdata.com/v3/ships'
    info = requests.get(url).json()

    context = {
        'ship':info
    }

    return render(request, 'blog/ship.html', context)

    