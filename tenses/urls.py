from django.urls import path
from .views import *

urlpatterns = [
    path('training', training_tenses_ru_en, name='run'),
    path('', home, name='home'),
    path('readtxt', read_txt)
]