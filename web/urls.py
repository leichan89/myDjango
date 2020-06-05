from django.urls import path
from web import views

urlpatterns = [
    path('myindex/', views.myindex, name='index'),
]