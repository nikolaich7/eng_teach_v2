import random
import time

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from .models import Example, Tense

def training_tenses_ru_en(request):
    req = request.POST
    print(req)
    user = User.objects.get(pk=req['user_pk'])
    if 'answer' in req:
        user.profile.total_answers += 1
        last_obj = user.profile.last_example = user.profile.now_example
        answer = user.profile.last_answer = req['answer'].strip()
        last_answer = last_obj.text.lower().strip() == answer.lower()
        if last_answer:
            user.profile.right_answers += 1
        else:
            user.profile.wrong_answers += 1
            print(last_obj.text)
        update_history(1)
    else:
        last_answer = user.profile.last_example.text.strip() == user.profile.last_answer

    rand_pk = random.randint(1, 152)
    example = Example.objects.get(pk=rand_pk)
    while example == user.profile.now_example:
        rand_pk = random.randint(1, 95)
        example = Example.objects.get(pk=rand_pk)
    user.profile.now_example = example
    user.profile.save()
    with open("text.txt", "w") as file:
        file.write(user.profile.now_example.text)
    return render(request, 'training_tenses_ru_en.html', {'last_answer': last_answer})

def read_txt(request):
    value = ''
    i = 0
    dict_ex = {}
    with open("1.txt", "r") as file1:
        for line in file1:
            if not line.strip():
                print('Пустпя строка')
                break
            if i%2 == 0:
                value = line
            else:
                dict_ex[line.strip()] = value.strip()
            i += 1
    for en, ru in dict_ex.items():
        e = Example(text=en, translation=ru, tense=Tense.objects.get(id=1))
        e.save()
    return HttpResponse('done')


def home(request):
    update_history(1)
    return render(request, 'home.html')


def update_history(user_pk):
    user = User.objects.get(pk=user_pk)
    time_str = time.strftime('%Y-%m-%d')
    if not time_str in user.profile.history:
        user.profile.total_answers = 0
        user.profile.right_answers = 0
        user.profile.wrong_answers = 0
        user.profile.history.update({time_str: {'total': 0, 'right': 0, 'wrong': 0}})
        user.profile.save()
    else:
        user.profile.history.update({time_str: {'total': user.profile.total_answers,
                                                'right': user.profile.right_answers,
                                                'wrong': user.profile.wrong_answers
                                                }})
        user.profile.save()
    return HttpResponse('done')