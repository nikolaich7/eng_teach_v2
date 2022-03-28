import random

from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView
from word.models import Word
from .models import Quote


class RunTrainingQuote(DetailView):
    model = Word
    template_name = 'run_training_quote.html'


def choice_word(request):
    req = request.POST
    check_obj = Word.objects.get(pk=req['pk'])
    context = {}
    if 'answer' in req:
        alt = check_obj.translation.split(', ')
        answer = False
        for i in alt:
            if req['answer'] == i:
                answer = True
                break
        if answer:
            context['object'] = get_next_word(check_obj)
            context['danger'] = False
            check_obj.lvl_know += 1
            check_obj.save()
        else:
            context['object'] = check_obj
            context['danger'] = True
            print(check_obj.translation)
            check_obj.lvl_know -= 1
            check_obj.save()
    else:
        context['object'] = get_next_word(check_obj)
        context['danger'] = False
    with open("text.txt", "w") as file:
        file.write(context['object'].word)
    return render(request, 'run_training_quote.html', context)

def get_next_word(last_word):
    rand = random.randint(1, 3)
    word = get_random3(rand)
    while word == last_word:
        word = get_random3(rand)
    return word

def get_random3(count):
    max_id = 68
    word = get_random1(max_id)
    for i in range(count):
        temp = get_random1(max_id)
        if temp.lvl_know < word.lvl_know:
            word = temp
    return word

def get_random1(max_id):
    while True:
        pk = random.randint(1, max_id)
        word = Word.objects.filter(pk=pk).first()
        if word:
            return word



def choice_quote(request):
    req = request.POST['pk']
    print(Quote.objects.get(pk=req).quote)
    rand_pk = random.randint(14, 31)
    context = {
        'object': Quote.objects.filter(pk=rand_pk).first(),
        'danger': False,
    }

    with open("text.txt", "w") as file:
        file.write(context['object'].quote)
    return render(request, 'run_training_for_quote.html', context)