from django.contrib import admin
from .models import Bb, Rubric


# Register your models here.
@admin.register(Bb)
class BbAdmin(admin.ModelAdmin):
    """Объявления."""

    # Поля, которые должны выводиться в админ-панели.
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    # Поля, которые должны вести на страницу исправления записей.
    list_display_links = ('title', 'content')
    # Поля, по которым должна выполняться фильтрация.
    search_fields = ('title', 'content')


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    """Рубрики."""

    list_display = ('name',)

