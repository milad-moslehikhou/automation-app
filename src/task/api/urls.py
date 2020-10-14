from django.urls import path

from .views import TasksView, TaskView

app_name = 'tasks'
urlpatterns = [
    path('', TasksView.as_view(), name='tasks'),
    path('<int:task_id>', TaskView.as_view(), name='task'),
]
