from django.urls import path

from .views import CollectorView

app_name = 'collector'
urlpatterns = [
    path('', CollectorView.as_view(), name='collector'),
]
