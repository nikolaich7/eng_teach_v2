import random
import time

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from .models import Example, Tense, Word


def home(request):
    """
    Домашняя страница
    Направлять сюда после авторизации
    Данные не обновляет
    Передает user_pk
    """
    right_today, wrong_today = get_right_and_wrong_today(1)  # Сюда подставить id юзера переданное после авторизазии
    right_word_today, wrong_word_today = get_right_and_wrong_word_today(1)

    context = {
        'right_today': right_today,
        'wrong_today': wrong_today,
        'right_word_today': right_word_today,
        'wrong_word_today': wrong_word_today,
    }
    return render(request, 'home.html', context)


def training_tenses_ru_en(request):
    req = request.POST
    user = User.objects.get(pk=req['user'])
    history = user.profile.history
    if 'answer' in req:
        time_str = time.strftime('%Y-%m-%d')
        question_pk = history['list_question'].pop(0)
        last_question = Example.objects.get(pk=question_pk)
        last_answer = req['answer'].strip()
        if not time_str in history:
            create_history_new_day(user.pk)
        if last_question.text.lower() == last_answer:
            history[time_str]['right'] += 1
            last_answer_is_true = True
        else:
            history[time_str]['wrong'] += 1
            last_answer_is_true = False
        if len(history['list_question']) == 0:
            history.update({'list_question': get_list_question_word()})
        question_pk = history['list_question'][0]
        user.profile.save()
    else:
        if 'list_question' in history and len(history['list_question']) > 0:
            list_question = history['list_question']
        else:
            history.update({'list_question': get_list_question_word()})
            user.profile.save()
        question_pk = history['list_question'][0]
        last_question = None
        last_answer = None
        last_answer_is_true = None
    right_today, wrong_today = get_right_and_wrong_today(1)
    context = {
        'question': Example.objects.get(pk=question_pk),
        'last_question': last_question,
        'last_answer': last_answer,
        'last_answer_is_true': last_answer_is_true,
        'right_today': right_today,
        'wrong_today': wrong_today,
    }

    return render(request, 'training_tenses_ru_en.html', context)


def training_word(request):
    req = request.POST
    user = User.objects.get(pk=req['user'])
    history = user.profile.history_word
    if 'answer' in req:
        time_str = time.strftime('%Y-%m-%d')
        question_pk = history['list_question'].pop(0)
        last_question = Word.objects.get(pk=question_pk)
        last_answer = req['answer'].strip()
        if not time_str in history:
            create_history_new_day(user.pk)
        if last_question.word.lower() == last_answer:
            history[time_str]['right'] += 1
            last_answer_is_true = True
        else:
            history[time_str]['wrong'] += 1
            last_answer_is_true = False
        if len(history['list_question']) == 0:
            history.update({'list_question': get_list_question_word()})
        question_pk = history['list_question'][0]
        user.profile.save()
    else:
        if 'list_question' in history and len(history['list_question']) > 0:
            list_question = history['list_question']
        else:
            history.update({'list_question': get_list_question_word()})
            user.profile.save()
        question_pk = history['list_question'][0]
        last_question = None
        last_answe= None
        last_answer_is_true = None
    right_today, wrong_today = get_right_and_wrong_word_today(1)
    context = {
        'question': Word.objects.get(pk=question_pk),
        'last_question': last_question,
        'last_answer': last_answer,
        'last_answer_is_true': last_answer_is_true,
        'right_today': right_today,
        'wrong_today': wrong_today,
    }
    return render(request, 'training_word.html', context)


def training_audio(request):
    pass


def get_right_and_wrong_today(user_pk):
    time_str = time.strftime('%Y-%m-%d')
    history = User.objects.get(pk=user_pk).profile.history
    if history == None:
        create_history_new_day(user_pk)
    if not time_str in history:
        create_history_new_day(user_pk)
        right, wrong = 0, 0
    else:
        history_today = history.get(time_str)
        right, wrong = history_today['right'], history_today['wrong']
    return (right, wrong)


def get_right_and_wrong_word_today(user_pk):
    time_str = time.strftime('%Y-%m-%d')
    history = User.objects.get(pk=user_pk).profile.history_word
    if history == None:
        create_history_word_new_day(user_pk)
    if not time_str in history:
        create_history_new_day(user_pk)
        right, wrong = 0, 0
    else:
        history_today = history.get(time_str)
        right, wrong = history_today['right'], history_today['wrong']
    return (right, wrong)


def create_history_new_day(user_pk):
    profile = User.objects.get(pk=user_pk).profile
    if profile.history == None:
        profile.history_word = {}
    profile.history.update({time.strftime('%Y-%m-%d'): {'right': 0, 'wrong': 0}})
    profile.save()


def create_history_word_new_day(user_pk):
    profile = User.objects.get(pk=user_pk).profile
    if profile.history_word == None:
        profile.history_word = {}
    profile.history_word.update({time.strftime('%Y-%m-%d'): {'right': 0, 'wrong': 0}})
    profile.save()


def get_list_question():
    list_currect_pk = [i for i in range(1, 248+1) if (152 >= i) or (i >= 198)]
    return(random.choices(list_currect_pk, k=10))


def get_list_question_word():
    list_currect_pk = [i for i in range(1, 91+1)]
    return(random.choices(list_currect_pk, k=10))
