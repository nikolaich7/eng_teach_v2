import random

from django.http import HttpResponse
from django.shortcuts import render

from .models import Example, Tense

def training_tenses_ru_en(request):
    req = request.POST
    last_obj = Example.objects.get(pk=req['pk'])
    if last_obj.text.lower() != req['answer'].lower().strip():
        context = {
            'object': last_obj,
            'mistake': True,
            'last_answer': req['answer'].strip()
        }
        print(last_obj.text)
    else:
        rand_pk = random.randint(1, 45)
        context = {
            'object': Example.objects.filter(pk=rand_pk).first(),
            'mistake': False,
            'last_answer': None
        }
    with open("text.txt", "w") as file:
        file.write(context['object'].text)
    return render(request, 'training_tenses_ru_en.html', context)

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