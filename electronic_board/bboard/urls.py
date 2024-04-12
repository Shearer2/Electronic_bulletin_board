from django.urls import path
from .views import index, by_rubric, BbCreateView


urlpatterns = [
    path('', index, name='index'),
    # rubric_id это имя параметра контроллера, которому будет присвоено значение.
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/', BbCreateView.as_view(), name='add'),
]
