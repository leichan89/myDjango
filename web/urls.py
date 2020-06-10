

from django.urls import path, include
from .views import basic

urlpatterns = [
    path('index/', basic.IndexView.as_view()),
]