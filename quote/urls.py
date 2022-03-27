from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>', RunTrainingQuote.as_view(), name='run'),
    path('', choice_word, name='choice'),
]