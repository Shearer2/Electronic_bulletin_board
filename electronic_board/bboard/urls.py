from django.urls import path
from .views import index, by_rubric


urlpatterns = [
    path('', index),
    # rubric_id это имя параметра контроллера, которому будет присвоено значение.
    path('<int:rubric_id>/', by_rubric),
]
