from django.urls import path

from .views import ReactionsView, ReactionView

app_name = 'reactions'
urlpatterns = [
    path('', ReactionsView.as_view(), name='reactions'),
    path('<int:reaction_id>', ReactionView.as_view(), name='reaction'),
]
