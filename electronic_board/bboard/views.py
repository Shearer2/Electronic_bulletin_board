from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Bb, Rubric
from .forms import BbForm


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


# Базовый класс сам создаёт форму, выводит её на сайте, получает занесённые данные, проверяет их, сохраняет в модели и
# перенаправляет пользователя дальше.
class BbCreateView(CreateView):
    # Путь к шаблону, создающего страницу с формой.
    template_name = 'bboard/create.html'
    # Ссылка на класс формы, связанной с моделью.
    form_class = BbForm
    # Адрес для перенаправления после успешного сохранения данных. reverse_lazy принимает имя маршрута
    # и значения всех входящих в маршрут url-параметров.
    success_url = reverse_lazy('index')

    # Переопределяем метод с добавлением списка рубрик и возвратом его.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

