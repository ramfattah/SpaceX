from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('capsules/', views.capsule, name='capsule'),
    path('cores/', views.core, name='core'),
    path('dragons/', views.dragon, name='dragon'),
    path('history/', views.history, name='history'),
    path('landing/', views.landing_pads, name='landing'),
    path('launches/', views.launch, name='launch'),
    path('missions/', views.mission, name='mission'),
    path('payloads/', views.payload, name='payload'),
    path('rockets/', views.rocket, name='rocket'),
    path('roadster/', views.roadster, name='roadster'),
    path('ships/', views.ship, name='ship'),
]
