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
]
