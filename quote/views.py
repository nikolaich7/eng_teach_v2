from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView
from word.models import Word_en


class RunTrainingQuote(DetailView):
    model = Word_en
    template_name = 'run_training_quote.html'


def choice_word(request):
    req = request.POST
    check_obj = Word_en.objects.get(pk=req['pk'])
    context = {}
    if 'answer' in req:
        alt = check_obj.translation.split(', ')
        answer = False
        for i in alt:
            if req['answer'] == i:
                answer = True
                break
        if answer:
            context['object'] = Word_en.objects.order_by("?").first()
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
        context['object'] = Word_en.objects.order_by("?").first()
        context['danger'] = False

    return render(request, 'run_training_quote.html', context)
