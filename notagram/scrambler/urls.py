from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('scrambler/', views.scrambler, name='scrambler'),
    path('test/', views.testing, name='test')
]