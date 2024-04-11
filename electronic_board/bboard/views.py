from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb, Rubric


# Create your views here.
def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
    }
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    # Список объявлений с фильтрацией по номеру рубрики.
    bbs = Bb.objects.filter(rubric=rubric_id)
    # Список всех рубрик.
    rubrics = Rubric.objects.all()
    # Список текущей рубрики.
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
    }
    return render(request, 'bboard/by_rubric.html', context)
