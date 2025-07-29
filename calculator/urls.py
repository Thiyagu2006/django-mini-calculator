from django.urls import path
from mysimplecalculator import views

urlpatterns = [
        path('thiyagu/mysimplecalulator/app', views.calculator, name='calculator'),
]
