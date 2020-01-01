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

    