from django.urls import path

from .views import ExecutionsView, ExecutionView

app_name = 'executions'
urlpatterns = [
    path('', ExecutionsView.as_view()),
    path('<int:execution_id>', ExecutionView.as_view()),
]
