from django.urls import path

from .views import ActionsView, ActionView

app_name = 'actions'
urlpatterns = [
    path('', ActionsView.as_view()),
    path('<int:action_id>', ActionView.as_view()),
]
