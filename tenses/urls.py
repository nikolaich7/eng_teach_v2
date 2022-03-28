from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>', training_tenses_ru_en, name='run'),
    path('', training_tenses_ru_en, name='choice'),
    path('readtxt', read_txt)
]